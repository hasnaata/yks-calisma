import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Kare dik piramit (T, ABCD): taban ayrıtı 6, yükseklik 7 (adlar için, ölçü yok)
a, h = 6, 7
A, B, C, D = (0, 0, 0), (a, 0, 0), (a, a, 0), (0, a, 0); G = (a / 2, a / 2, 0); T = (a / 2, a / 2, h)
fig, ax = sekil(6, 4.8)
piramit(ax, [A, B, C, D], T, renkler={1: SARI_ACIK, 2: MAVI_ACIK})
cizgi(ax, T, G, renk=MAVI, lw=2.2, ls=(0, (5, 3)))
dik(ax, G, (1, 0, 0), (0, 0, 1), r=0.5, renk=MAVI); nk(ax, G, MAVI)
cizgi(ax, T, B, renk=KIRMIZI, lw=3); cizgi(ax, A, B, renk=YESIL, lw=3)
for p, s, dx, dy in ((A, "A", -0.35, -0.25), (B, "B", 0.35, -0.25), (C, "C", 0.35, 0.05), (D, "D", -0.35, 0.15), (T, "T", 0, 0.4), (G, "G", -0.35, -0.2)):
    yaz(ax, p, s, dx, dy, boy=13)
def ok(p, metin, xy, renk):
    q = P(p); ax.annotate(metin, xy=q, xytext=xy, color=renk, fontsize=12, ha="center", va="center",
        arrowprops=dict(arrowstyle="-", color=renk, lw=1.2, shrinkA=2, shrinkB=2), zorder=8)
ok(T, "tepe noktası", (-1.2, 7.6), YAZI)
ok((a * 0.82, a * 0.15, h * 0.35), "yanal ayrıt", (9.6, 3.2), KIRMIZI)
ok((a * 0.33, 0.5, h * 0.25), "yanal yüz", (-2.4, 3.0), SARI)
ok((a * 0.3, 0, 0), "taban ayrıtı", (1.0, -1.3), YESIL)
ok((a / 2, a / 2, h * 0.55), "yükseklik", (-2.0, 5.6), MAVI)
ok((a * 0.75, a * 0.7, 0), "taban", (9.4, 0.6), SOLUK)
ax.set_xlim(-4, 11); ax.set_ylim(-1.8, 8.2); bitir(ax)
kaydet(fig, __file__)
