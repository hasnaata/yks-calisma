import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Kendini dene 2: taban ayrıtı 10, yükseklik 12; yan yüz yüksekliği (TM) soruluyor
a, h = 10, 12
fig, ax = sekil(4.6, 5)
k = kare(ax, a, h); s = k["s"]; M = (a, a / 2, 0)
cizgi(ax, k["T"], k["G"], renk=MAVI, lw=2.4, ls=(0, (5, 2.5))); dik(ax, k["G"], (1, 0, 0), (0, 0, 1), r=0.8)
cizgi(ax, k["T"], M, renk=KIRMIZI, lw=2.8); dik(ax, M, (0, 1, 0), (-a / 2, 0, h), r=0.7, renk=KIRMIZI)
yaz(ax, M, "M", 1.0 * s, -0.4 * s)
yaz(ax, (a / 2, a / 2, h / 2), "12", -0.9 * s, 0, renk=MAVI)
yaz(ax, (a * 0.75, a / 2, h / 2), "?", 1.0 * s, 0.4 * s, renk=KIRMIZI, boy=15)
yaz(ax, (a / 2, 0, 0), "10", 0, -0.8 * s)
kaydet(fig, __file__)
