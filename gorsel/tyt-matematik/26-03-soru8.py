import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Bu basik piramitte 40° eğiklikte sol yan yüz kenardan görünüp TA ile üst üste biniyor; 30° kullan.
TETA = np.radians(30); CX, SY = KD * np.cos(TETA), KD * np.sin(TETA); GOZ = np.array([CX, -1.0, SY])
# Alıştırma 8: kare dik piramit biçiminde çatı, taban ayrıtı 8 m, yükseklik 3 m
a, h = 8, 3
fig, ax = sekil(5, 3.2)
k = kare(ax, a, h, adlar=False); s = k["s"]
cizgi(ax, k["T"], k["G"], renk=MAVI, lw=2.4, ls=(0, (5, 2.5))); dik(ax, k["G"], (1, 0, 0), (0, 0, 1), r=0.4)
yaz(ax, (a / 2, a / 2, h * 0.12), "3 m", -1.75 * s, 0, renk=MAVI)
yaz(ax, (a / 2, 0, 0), "8 m", 0, -0.8 * s)
yaz(ax, (a, a / 2, 0), "8 m", 1.6 * s, -0.4 * s)
kaydet(fig, __file__)
