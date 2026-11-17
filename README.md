# YKS Çalışma Sistemi

2027 YKS (TYT + AYT Eşit Ağırlık) için konu anlatımı, alıştırma ve aralıklı tekrar sitesi. Müfredat MEBİ ile aynı: 13 ders, 231 konu, 740 alt konu.

- **Site:** GitHub Pages üzerinden yayınlanır (repo ayarlarındaki adres).
- **İçerik kataloğu:** [index.md](index.md) · **Değişiklik günlüğü:** [log.md](log.md)
- **Claude için kurallar:** [CLAUDE.md](CLAUDE.md)

## Nasıl güncellenir?

Repoyu Claude Code ile aç ve örneğin şunu söyle: "TYT Biyoloji'de sıradaki 5 dersi yaz." Claude `CLAUDE.md`'deki iş akışını izler: MEBİ konu özetini okur, dersi ve alıştırmayı yazar, kataloğu ve günlüğü günceller. Öğrenciler için `/teach` komutu soru-cevap biçiminde özel ders verir.

```
python3 tools/indir.py tyt-biyoloji   # ham kaynakları indir (yalnızca yerelde durur)
python3 tools/mufredat.py             # kataloğu yeniden üret
python3 tools/denetle.py              # biçim denetimi
python3 -m http.server 8799           # yerelde aç
```

Matematik şekilleri için bir kez: `python3 -m venv --without-pip .venv`, pip kur, sonra `.venv/bin/python -m pip install matplotlib sympy` (ayrıntı: `tools/cizim.py`).

## Telif

Dersler ve sorular bu repo için özgün olarak yazılmıştır. MEB ve ÖSYM içerikleri kopyalanmaz; yalnızca resmî kaynaklara bağlantı verilir. `.claude/skills/teach` Matt Pocock'un MIT lisanslı becerisidir.
