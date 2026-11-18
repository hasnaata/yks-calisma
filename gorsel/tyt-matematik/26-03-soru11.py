import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Alıştırma 11: ayrıtı 6 olan küp; T üst yüzün merkezi, piramidin tabanı küpün alt yüzü
a = 6
A, B, C, D = (0, 0, 0), (a, 0, 0), (a, a, 0), (0, a, 0)
E, F, Gk, Hk = (0, 0, a), (a, 0, a), (a, a, a), (0, a, a)
T = (a / 2, a / 2, a)
fig, ax = sekil(4.6, 4.6)
# önce piramidin yüzleri (açık sarı), sonra küp
for p, q in ((A, B), (B, C)):
    ax.add_patch(patches.Polygon([P(T), P(p), P(q)], closed=True, facecolor=SARI_ACIK, edgecolor="none", zorder=0.5))
cokyuzlu(ax, [A, B, C, D, E, F, Gk, Hk], [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7]])
for p in (A, B, C): cizgi(ax, T, p, renk=KIRMIZI, lw=2.2)
cizgi(ax, T, D, renk=KIRMIZI, lw=1.6, ls=(0, (4, 3)))
nk(ax, T, KIRMIZI)
for p, s, dx, dy in ((A, "A", -0.4, -0.3), (B, "B", 0.4, -0.3), (C, "C", 0.4, 0.0), (D, "D", -0.45, 0.15), (T, "T", 0, 0.4)):
    yaz(ax, p, s, dx, dy)
yaz(ax, (a / 2, 0, 0), "6", 0, -0.45); yaz(ax, (0, 0, a / 2), "6", -0.4, 0)
ax.set_xlim(-1, a + CX * a + 1); ax.set_ylim(-1, a + SY * a + 0.8); bitir(ax)
kaydet(fig, __file__)
