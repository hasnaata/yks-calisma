import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Alıştırma 5: taban ayrıtı 8√2, yanal ayrıt 10 (yükseklik 6)
a, l = 8 * 2**0.5, 10; h = (l**2 - a**2 / 2) ** 0.5
fig, ax = sekil(5.2, 3.8)
k = kare(ax, a, h, G_goster=False); s = k["s"]
cizgi(ax, k["T"], k["B"], renk=KIRMIZI, lw=2.8)
yaz(ax, (a * 0.75, a / 4, h / 2), "10", 1.2 * s, 0.9 * s, renk=KIRMIZI)
yaz(ax, (a / 2, 0, 0), r"$8\sqrt{2}$", 0, -0.9 * s)
kaydet(fig, __file__)
