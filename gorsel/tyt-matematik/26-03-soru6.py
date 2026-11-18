import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# 40° eğiklikte sağ arka yan yüz kenardan görünüp tek çizgi gibi kalıyor; 60° kullan.
TETA = np.radians(60); CX, SY = KD * np.cos(TETA), KD * np.sin(TETA); GOZ = np.array([CX, -1.0, SY])
# Alıştırma 6: düzgün altıgen dik piramit, taban ayrıtı 4, yükseklik 6
a, h = 4, 6
taban = [(a * np.cos(np.radians(60 * i - 120)), a * np.sin(np.radians(60 * i - 120)), 0) for i in range(6)]
G = (0, 0, 0); T = (0, 0, h)
fig, ax = sekil(4.6, 4.6)
piramit(ax, taban, T, renkler={1: SARI_ACIK, 2: MAVI_ACIK, 6: MAVI_ACIK})
cizgi(ax, T, G, renk=MAVI, lw=2.4, ls=(0, (5, 2.5))); nk(ax, G); dik(ax, G, (1, 0, 0), (0, 0, 1), r=0.5)
yaz(ax, G, "G", -0.45, -0.3)
yaz(ax, T, "T", 0, 0.45)
yaz(ax, (0, 0, h / 2), "6", 0.45, 0, renk=MAVI)
yaz(ax, ((taban[0][0] + taban[1][0]) / 2, taban[0][1], 0), "4", 0, -0.5)
xs = [P(p)[0] for p in taban]; ys = [P(p)[1] for p in taban]
ax.set_xlim(min(xs) - 0.8, max(xs) + 0.8); ax.set_ylim(min(ys) - 1.0, h + 0.9); bitir(ax)
kaydet(fig, __file__)
