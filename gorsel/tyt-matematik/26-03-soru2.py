import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Bu basik piramitte 40° eğiklikte sol yan yüz kenardan görünüp TA ile üst üste biniyor; 30° kullan.
TETA = np.radians(30); CX, SY = KD * np.cos(TETA), KD * np.sin(TETA); GOZ = np.array([CX, -1.0, SY])
# Alıştırma 2: taban ayrıtı 16, yükseklik 6; yan yüz yüksekliği soruluyor
a, h = 16, 6
fig, ax = sekil(5.4, 3.6)
k = kare(ax, a, h); s = k["s"]; M = (a, a / 2, 0)
cizgi(ax, k["T"], k["G"], renk=MAVI, lw=2.4, ls=(0, (5, 2.5))); dik(ax, k["G"], (1, 0, 0), (0, 0, 1), r=0.7)
cizgi(ax, k["T"], M, renk=KIRMIZI, lw=2.8); dik(ax, M, (0, 1, 0), (-a / 2, 0, h), r=0.7, renk=KIRMIZI)
yaz(ax, M, "M", 0.9 * s, -0.4 * s)
yaz(ax, (a / 2, a / 2, h / 2), "6", -0.7 * s, 0, renk=MAVI)
yaz(ax, (a * 0.75, a / 2, h / 2), "?", 0.6 * s, 0.6 * s, renk=KIRMIZI, boy=15)
yaz(ax, (a / 2, 0, 0), "16", 0, -0.8 * s)
kaydet(fig, __file__)
