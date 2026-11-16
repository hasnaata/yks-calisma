#!/usr/bin/env python3
"""Ders görselleri için yardımcı araç.

  python3 tools/gorsel.py ara "glucose 3D model"        Wikimedia Commons'ta ara (yalnızca özgür lisanslılar listelenir)
  python3 tools/gorsel.py indir "File:Ad.jpg" gorsel/tyt-biyoloji/03-01-glikoz.jpg
                                                         900 px genişlikte indir, gorsel/ATIF.md'ye atıf satırı ekle
  python3 tools/gorsel.py renk gorsel/.../sema.svg ...   Pele'nin ürettiği şemayı site renklerine çevir
  python3 tools/gorsel.py bak gorsel/.../dosya.svg       Görseli telefondaki boyutunda PNG'ye çevir (yolu yazar); sonra o PNG'ye bak

Yalnızca özgür lisanslı (kamu malı, CC0, CC BY, CC BY-SA) görseller indirilir; başka kaynaktan görsel alma."""
import json, re, sys, pathlib, urllib.parse, urllib.request, html
K = pathlib.Path(__file__).resolve().parent.parent
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "study-site-image-fetcher/1.0 (educational, non-commercial)"}
OZGUR = re.compile(r"^(cc0|public domain|pd\b|cc[ -]by([ -]sa)?[ -]\d)", re.I)

def api(**p):
    p.update(format="json")
    with urllib.request.urlopen(urllib.request.Request(API + "?" + urllib.parse.urlencode(p), headers=UA), timeout=30) as r:
        return json.load(r)
def temiz(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s or ""))).strip()
def bilgi(sayfalar):
    for s in sayfalar:
        ii = (s.get("imageinfo") or [{}])[0]; m = ii.get("extmetadata", {})
        yield {"ad": s["title"], "lisans": temiz(m.get("LicenseShortName", {}).get("value")),
               "yazar": temiz(m.get("Artist", {}).get("value"))[:80], "aciklama": temiz(m.get("ImageDescription", {}).get("value"))[:140],
               "en": ii.get("width"), "boy": ii.get("height"), "kucuk": ii.get("thumburl"), "sayfa": ii.get("descriptionurl")}
ORTAK = dict(action="query", prop="imageinfo", iiprop="url|size|extmetadata", iiurlwidth=900)

def ara(sorgu):
    r = api(generator="search", gsrsearch=sorgu + " filetype:bitmap|drawing", gsrnamespace=6, gsrlimit=25, **ORTAK)
    for b in bilgi(sorted(r.get("query", {}).get("pages", {}).values(), key=lambda x: x.get("index", 0))):
        if OZGUR.match(b["lisans"]):
            print(f"{b['ad']}\n   {b['lisans']} · {b['yazar']} · {b['en']}x{b['boy']}\n   {b['aciklama']}")

def indir(ad, hedef):
    b = next(bilgi(api(titles=ad, **ORTAK)["query"]["pages"].values()))
    if not b["kucuk"]: sys.exit("Dosya bulunamadı: " + ad)
    if not OZGUR.match(b["lisans"]): sys.exit(f"Lisans özgür değil ({b['lisans']}); indirilmedi.")
    hedef = pathlib.Path(hedef)
    uz = pathlib.Path(urllib.parse.urlparse(b["kucuk"]).path).suffix.lower()   # svg küçük resimleri .png gelir
    if hedef.suffix.lower() != uz: hedef = hedef.with_suffix(uz)
    hedef.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(urllib.request.Request(b["kucuk"], headers=UA), timeout=60) as r: hedef.write_bytes(r.read())
    hedef = kucult(hedef)
    atif = K / "gorsel/ATIF.md"
    if not atif.exists():
        atif.write_text("# Görsel Atıfları\n\nBu sitedeki fotoğraf ve çizimler Wikimedia Commons'tan alınmıştır. Şemalar (.svg) bu site için üretilmiştir.\n\n| Dosya | Eser | Yazar | Lisans |\n|---|---|---|---|\n", encoding="utf8")
    satir = f"| `{hedef.relative_to(K) if hedef.is_absolute() else hedef}` | [{b['ad'][5:]}]({b['sayfa']}) | {b['yazar'].replace('|', '/')} | {b['lisans']} |\n"
    with atif.open("a", encoding="utf8") as f: f.write(satir)
    print(f"{hedef}  ({b['lisans']}; {b['yazar']})")

def kucult(yol):
    """Saydam olmayan büyük PNG'leri JPEG'e çevirir, hepsini en çok 900 px genişliğe indirir."""
    try: from PIL import Image
    except ImportError: return yol
    g = Image.open(yol); g.load()
    if g.width > 900: g = g.resize((900, round(g.height * 900 / g.width)))
    saydam = g.mode in ("RGBA", "LA", "P") and g.convert("RGBA").getextrema()[3][0] < 250
    if yol.suffix.lower() == ".png" and saydam: g.save(yol, optimize=True); return yol
    yeni = yol.with_suffix(".jpg"); g.convert("RGB").save(yeni, quality=82, optimize=True, progressive=True)
    if yeni != yol: yol.unlink()
    return yeni

RENK = {"--pele-bg": "transparent", "--pele-fg": "#1d1f24", "--pele-muted": "#636a76", "--pele-line": "#636a76",
        "--pele-surface": "#e8f0fc", "--pele-surface-alt": "#dbe7fa", "--pele-border": "#1f5fbf", "--pele-accent": "#1f5fbf"}
def renk(dosyalar):
    for d in dosyalar:
        p = pathlib.Path(d); s = p.read_text(encoding="utf8")
        if 'class="pele' not in s: print("Pele şeması değil, atlandı:", d); continue
        for k, v in RENK.items(): s = re.sub(re.escape(k) + r":[^;\"]+", f"{k}:{v}", s, count=1)
        s = s.replace("font:16px sans-serif", "font:16px system-ui,-apple-system,'Segoe UI',sans-serif")
        p.write_text(s, encoding="utf8"); print("renklendi:", d)

def bak(dosya):
    """Görselin telefonda (340 px genişlik) nasıl göründüğünü PNG olarak üretir."""
    import subprocess, tempfile, hashlib
    d = pathlib.Path(dosya).resolve(); t = pathlib.Path(tempfile.gettempdir()) / ("onizleme-" + hashlib.md5(str(d).encode()).hexdigest()[:10])
    t.mkdir(exist_ok=True); h = t / "s.html"; png = t / (d.stem + ".png")
    h.write_text(f'<body style="margin:0;background:#fff"><img src="file://{d}" style="width:340px;display:block">', encoding="utf8")
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--window-size=340,900", f"--user-data-dir={t}/p", f"--screenshot={png}", f"file://{h}"], capture_output=True, timeout=90)
    try:
        from PIL import Image, ImageChops
        g = Image.open(png).convert("RGB"); kutu = ImageChops.difference(g, Image.new("RGB", g.size, (255, 255, 255))).getbbox()
        if kutu: g.crop((0, 0, g.width, min(g.height, kutu[3] + 10))).save(png)
    except Exception: pass
    print(png)

if __name__ == "__main__":
    k = sys.argv[1:] or [""]
    if k[0] == "ara" and len(k) == 2: ara(k[1])
    elif k[0] == "indir" and len(k) == 3: indir(k[1], k[2])
    elif k[0] == "renk" and len(k) > 1: renk(k[1:])
    elif k[0] == "bak" and len(k) == 2: bak(k[1])
    else: print(__doc__)
