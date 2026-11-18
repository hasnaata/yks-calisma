import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Üçgen, kare ve altıgen dik piramit; yükseklik 4,5
fig, ax = sekil(6.4, 4.2)
h = 4.5
s3 = 3.2
t3 = [(0, 0, 0), (s3, 0, 0), (s3 / 2, s3 * np.sqrt(3) / 2, 0)]
t4 = [(5, 0, 0), (8, 0, 0), (8, 3, 0), (5, 3, 0)]
r6 = 1.7; m6 = (12.3, r6 * np.sqrt(3) / 2)
t6 = [(m6[0] + r6 * np.cos(np.radians(60 * i - 120)), m6[1] + r6 * np.sin(np.radians(60 * i - 120)), 0) for i in range(6)]
for t in (t3, t4, t6):
    t = [np.array(p, float) for p in t]; g = sum(t) / len(t)
    n = len(t)
    piramit(ax, t, (g[0], g[1], h), renkler={**{k: MAVI_ACIK for k in range(1, n + 1)}, 1: SARI_ACIK})
yazilar = [(1.9, "üçgen piramit", "4 köşe · 6 ayrıt · 4 yüz"),
           (7.0, "kare piramit", "5 köşe · 8 ayrıt · 5 yüz"),
           (12.7, "altıgen piramit", "7 köşe · 12 ayrıt · 7 yüz")]
for x, s1, s2 in yazilar:
    ax.text(x, -0.6, s1.replace(" ", "\n"), ha="center", va="top", fontsize=11.5, color=YAZI, linespacing=1.2)
    ax.text(x, -2.6, s2.replace(" · ", "\n"), ha="center", va="top", fontsize=11, color=SOLUK, linespacing=1.25)
ax.set_xlim(-0.6, 15); ax.set_ylim(-6.4, 5.0); bitir(ax)
kaydet(fig, __file__)
