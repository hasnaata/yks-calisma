#!/usr/bin/env python3
"""Bir alıştırma dosyasını cevap ve çözümleri silinmiş olarak yazdırır (kör çözüm denetimi için).
Kullanım: python3 tools/kor.py <yol>      (yol: mufredat.json'daki 'yol', uzantısız)"""
import re, sys, pathlib
K = pathlib.Path(__file__).resolve().parent.parent
s = (K / (sys.argv[1] + ".alistirma.md")).read_text(encoding="utf8")
print(re.sub(r"\*\*Cevap:\*\*.*?(?=^#{2,3} |\Z)", "\n", s, flags=re.S | re.M))
