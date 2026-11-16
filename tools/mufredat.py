#!/usr/bin/env python3
"""raw/mebi/agac.txt -> data/mufredat.json ve index.md. Ders dosyalarının varlığına göre durum yazar.
Her içerik değişikliğinden sonra çalıştır: python3 tools/mufredat.py"""
import json, re, pathlib, datetime
K = pathlib.Path(__file__).resolve().parent.parent
TR = str.maketrans("çğıöşüâîûÇĞİÖŞÜÂÎÛ", "cgiosuaiucgiosuaiu")
def slug(s):
    s = s.translate(TR).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60].strip("-")
dersler, d, k = [], None, None
for l in (K / "raw/mebi/agac.txt").read_text(encoding="utf8").splitlines():
    if l.startswith("# "):
        sinav, ad = l[2:].split("|")
        ad = re.sub(r"\s*\((TYT|AYT|TYT/AYT)\)", "", ad)
        d = {"id": f"{sinav.lower()}-{slug(ad)}", "sinav": sinav, "ad": ad, "konular": []}
        dersler.append(d)
    elif l.startswith("## "):
        k = {"no": len(d["konular"]) + 1, "ad": l[3:], "altkonular": []}
        k["slug"] = f"{k['no']:02d}-{slug(k['ad'])}"
        d["konular"].append(k)
    elif l.startswith("- "):
        ad, pdf, cikmis, mebi, _video = l[2:].split("|")
        no = len(k["altkonular"]) + 1
        yol = f"dersler/{d['id']}/{k['slug']}/{no:02d}-{slug(ad)}"
        k["altkonular"].append({"no": no, "ad": ad, "yol": yol, "pdf": pdf, "mebi": mebi,
            "cikmis": cikmis == "1",
            "ders": (K / (yol + ".md")).exists(),
            "alistirma": (K / (yol + ".alistirma.md")).exists()})
(K / "data/mufredat.json").write_text(json.dumps(dersler, ensure_ascii=False, indent=1), encoding="utf8")
# index.md: wiki kataloğu
out = ["# İçerik Kataloğu (index.md)", "",
       "Bu dosyayı `tools/mufredat.py` üretir; elle düzenleme. ✅ = ders ve alıştırma hazır, ⬜ = sırada.", ""]
top = hazir = 0
for d in dersler:
    n = sum(len(k["altkonular"]) for k in d["konular"])
    h = sum(a["ders"] and a["alistirma"] for k in d["konular"] for a in k["altkonular"])
    top += n; hazir += h
    out += [f"## {d['sinav']} {d['ad']} ({h}/{n})", ""]
    for k in d["konular"]:
        out.append(f"- **{k['no']}. {k['ad']}**")
        for a in k["altkonular"]:
            if a["ders"] and a["alistirma"]:
                out.append(f"  - ✅ [{a['ad']}]({a['yol']}.md) · [alıştırma]({a['yol']}.alistirma.md)")
            else:
                out.append(f"  - ⬜ {a['ad']} — `{a['yol']}.md`")
    out.append("")
out.insert(3, f"**Toplam: {hazir}/{top} ders hazır.** Son güncelleme: {datetime.date.today()}")
(K / "index.md").write_text("\n".join(out), encoding="utf8")
print(f"{len(dersler)} ders, {top} alt konu, {hazir} hazır")
