#!/usr/bin/env python3
"""MEBİ konu özeti PDF'lerini raw/mebi/pdf'e indirir ve raw/mebi/metin'e düz metin çıkarır.
Kullanım: python3 tools/indir.py [ders-id ...]   (boşsa hepsi). PDF'ler telifli: repoya girmez."""
import json, subprocess, sys, pathlib, concurrent.futures as cf
K = pathlib.Path(__file__).resolve().parent.parent
sec = set(sys.argv[1:])
isler = [a["pdf"] for d in json.loads((K / "data/mufredat.json").read_text(encoding="utf8"))
         if not sec or d["id"] in sec for k in d["konular"] for a in k["altkonular"] if a["pdf"]]
def al(p):
    pdf, txt = K / f"raw/mebi/pdf/{p}.pdf", K / f"raw/mebi/metin/{p}.txt"
    if not pdf.exists():
        r = subprocess.run(["curl", "-sfL", "--retry", "3", "-o", str(pdf),
                            f"https://ogm-large-cdn.eba.gov.tr/mebi/pdf/{p}.pdf"])
        if r.returncode: pdf.unlink(missing_ok=True); return p
    if not txt.exists():
        subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)])
    return None
with cf.ThreadPoolExecutor(3) as ex:
    hata = [x for x in ex.map(al, isler) if x]
print(f"{len(isler)} dosya, {len(hata)} hata", hata[:10])
