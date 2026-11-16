#!/usr/bin/env python3
"""Ders ve alıştırma dosyalarının biçimini denetler. Hata varsa 1 ile çıkar."""
import json, re, sys, pathlib, collections
K = pathlib.Path(__file__).resolve().parent.parent
hata, sayac = [], collections.Counter()
def sorular(metin):
    return re.split(r"^### Soru[^\n]*\n", metin, flags=re.M)[1:]
for d in json.loads((K / "data/mufredat.json").read_text(encoding="utf8")):
    for k in d["konular"]:
        for a in k["altkonular"]:
            ders, alis = K / (a["yol"] + ".md"), K / (a["yol"] + ".alistirma.md")
            if ders.exists() != alis.exists():
                hata.append(f"{a['yol']}: ders ve alıştırma birlikte olmalı")
            for dosya, enaz in ((ders, 3), (alis, 10)):
                if not dosya.exists(): continue
                m = dosya.read_text(encoding="utf8")
                if not m.startswith("---\n"): hata.append(f"{dosya.name}: ön madde yok")
                s = sorular(m)
                if len(s) < enaz: hata.append(f"{dosya.name}: {len(s)} soru var, en az {enaz} olmalı")
                for i, b in enumerate(s, 1):
                    b = re.split(r"^## ", b, flags=re.M)[0]
                    sec = re.findall(r"^([A-E])\) ", b, flags=re.M)
                    c = re.search(r"\*\*Cevap:\*\*\s*([A-E])\s*$", b, flags=re.M)
                    if sec != list("ABCDE"): hata.append(f"{dosya.name} soru {i}: seçenekler A–E değil ({''.join(sec)})")
                    if not c: hata.append(f"{dosya.name} soru {i}: **Cevap:** yok")
                    elif dosya is alis: sayac[c.group(1)] += 1
                    if "**Çözüm:**" not in b: hata.append(f"{dosya.name} soru {i}: **Çözüm:** yok")
                if m.count("$") % 2: hata.append(f"{dosya.name}: eşleşmeyen $ işareti")
print("Cevap dağılımı:", dict(sorted(sayac.items())))
if sayac and max(sayac.values()) > 0.3 * sum(sayac.values()) + 2:
    hata.append("Cevap harfleri dengesiz dağılmış")
print("\n".join(hata) or "Biçim denetimi: sorun yok")
sys.exit(1 if hata else 0)
