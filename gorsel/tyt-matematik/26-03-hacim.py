import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Örnek 4: aynı taban (6 · 6) ve aynı yükseklik (4): prizma 144, piramit 48
a, h = 6, 4
fig, ax = sekil(5.4, 4.2)
A, B, C, D = (0, 0, 0), (a, 0, 0), (a, a, 0), (0, a, 0)
# prizmanın ayrıtları ince ve soluk
kose = [A, B, C, D, (0, 0, h), (a, 0, h), (a, a, h), (0, a, h)]
for i, j in ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)):
    gizli = 3 in (i, j)
    cizgi(ax, kose[i], kose[j], renk=SOLUK, lw=1.2, ls=(0, (4, 3)) if gizli else "-", z=1 if gizli else 3)
T = (a / 2, a / 2, h)
piramit(ax, [A, B, C, D], T, renkler={1: SARI_ACIK, 2: SARI_ACIK})
cizgi(ax, T, (a / 2, a / 2, 0), renk=MAVI, lw=2, ls=(0, (5, 3))); dik(ax, (a / 2, a / 2, 0), (1, 0, 0), (0, 0, 1), r=0.45, renk=MAVI)
yaz(ax, (a / 2, a / 2, h / 2), "4", -0.35, 0.0, renk=MAVI)
yaz(ax, (a / 2, 0, 0), "6", 0, -0.4); yaz(ax, (a, a / 2, 0), "6", 0.45, -0.1)
ax.text(10.0, 3.6, "prizma:\n36 · 4 = 144", ha="left", va="center", fontsize=12, color=SOLUK)
ax.text(10.0, 1.3, "piramit:\n144 : 3 = 48", ha="left", va="center", fontsize=12, color=SARI)
ax.set_xlim(-0.8, 14.5); ax.set_ylim(-1, 6.5); bitir(ax)
kaydet(fig, __file__)
