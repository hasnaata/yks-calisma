import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Bu basik piramitte 40° eğiklikte sol yan yüz kenardan görünüp TA ile üst üste biniyor; 30° kullan.
TETA = np.radians(30); CX, SY = KD * np.cos(TETA), KD * np.sin(TETA); GOZ = np.array([CX, -1.0, SY])
# Kendini dene 3: taban ayrıtı 8, yan yüz yüksekliği 5; hacim soruluyor
a, hy = 8, 5; h = (hy**2 - (a / 2)**2) ** 0.5   # h = 3
fig, ax = sekil(4.8, 3.4)
k = kare(ax, a, h); s = k["s"]; M = (a, a / 2, 0)
cizgi(ax, k["T"], M, renk=KIRMIZI, lw=2.8); dik(ax, M, (0, 1, 0), (-a / 2, 0, h), r=0.45, renk=KIRMIZI)
yaz(ax, M, "M", 0.9 * s, -0.4 * s)
yaz(ax, (a * 0.75, a / 2, h / 2), "5", 0.8 * s, 0.5 * s, renk=KIRMIZI)
yaz(ax, (a / 2, 0, 0), "8", 0, -0.8 * s)
kaydet(fig, __file__)
