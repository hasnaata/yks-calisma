import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 7: A-B arası 3 yol, B-C arası 2 yol, A-C arası doğrudan 4 yol.
fig, ax = sekil(6, 3.4)
ax.axis("off"); ax.set_aspect("equal")
A, B, C = (0, 0), (3, 0), (6, 0)
def yollar(p, q, egimler, renk):
    for e in egimler:
        x = np.linspace(p[0], q[0], 60); t = (x - p[0]) / (q[0] - p[0])
        ax.plot(x, p[1] + e * 4 * t * (1 - t), color=renk, lw=2)
yollar(A, B, [0.9, 0.0, -0.9], MAVI)
yollar(B, C, [0.6, -0.6], YESIL)
yollar(A, C, [-1.6, -2.1, -2.6, -3.1], SARI)
for p, ad in ((A, "A"), (B, "B"), (C, "C")):
    ax.add_patch(patches.Circle(p, 0.32, facecolor="white", edgecolor=YAZI, lw=1.8, zorder=5))
    ax.text(*p, ad, ha="center", va="center", fontsize=15, fontweight="bold", zorder=6)
ax.set_xlim(-0.5, 6.5); ax.set_ylim(-3.4, 1.2)
kaydet(fig, __file__)
