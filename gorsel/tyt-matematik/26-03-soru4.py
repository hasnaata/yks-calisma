import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Alıştırma 4: taban ayrıtı 10, yanal ayrıt 13
a, l = 10, 13; h = (l**2 - a**2 / 2) ** 0.5
fig, ax = sekil(4.6, 5)
k = kare(ax, a, h, G_goster=False); s = k["s"]
cizgi(ax, k["T"], k["B"], renk=KIRMIZI, lw=2.8)
yaz(ax, (a * 0.75, a / 4, h / 2), "13", 1.0 * s, 0.2 * s, renk=KIRMIZI)
yaz(ax, (a / 2, 0, 0), "10", 0, -0.8 * s)
kaydet(fig, __file__)
