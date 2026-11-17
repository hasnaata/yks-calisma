import sys; sys.path.insert(0, "tools")
from cizim import *

# d1 // d2 (yatay), d3 kesen yatayla 65° yapar. A'da 1-4, B'de 5-8 numaralı açılar.
# Dar açılar (65°) mavi, geniş açılar (115°) kırmızı.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
h = 3.0; t = 65
B = np.array([0.0, 0.0]); A = B + h / np.sin(np.radians(t)) * yon(t)
fig, ax = sekil(6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
for y, ad in ((h, "d₁"), (0, "d₂")):
    ax.plot([-3.6, 5.4], [y, y], color=YAZI)
    ax.plot(4.6, y, ">", color=YAZI, markersize=7)
    ax.text(-3.9, y, ad, ha="right", va="center", fontsize=13)
u = yon(t); s0, s1 = B - 1.7 * u, A + 1.7 * u
ax.plot(*zip(s0, s1), color=YAZI)
ax.text(*(s1 + 0.25 * u), "d₃", ha="left", va="bottom", fontsize=13)
nokta(ax, *A); nokta(ax, *B)
for P, n in ((A, 1), (B, 5)):
    yonler = [(0, t), (t, 180), (180, 180 + t), (180 + t, 360)]
    for i, (a1, a2) in enumerate(yonler):
        renk = MAVI if i % 2 == 0 else KIRMIZI
        r = 0.55 if i % 2 == 0 else 0.42
        aci(ax, P, P + yon(a1), P + yon(a2), r=r, ad=str(n + i), renk=renk)
ax.text(5.6, 1.5, "d₁ ∥ d₂", fontsize=13, ha="right", color=SOLUK)
ax.set_xlim(-4.4, 5.9); ax.set_ylim(-1.9, h + 1.9)
kaydet(fig, __file__)
