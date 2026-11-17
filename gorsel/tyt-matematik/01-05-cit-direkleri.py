import sys; sys.path.insert(0, "tools")
from cizim import *

# 7, 11, 15, 19, 23: 5 terim, aralarında 4 boşluk. Terim sayısı = boşluk sayısı + 1.
fig, ax = sekil(6, 2.4)
ax.axis("off")
terimler = [7, 11, 15, 19, 23]
xs = [0, 1.5, 3, 4.5, 6]
ax.plot([xs[0], xs[-1]], [0.55, 0.55], color=SOLUK, lw=2)
ax.plot([xs[0], xs[-1]], [0.25, 0.25], color=SOLUK, lw=2)
for x, t in zip(xs, terimler):
    ax.add_patch(patches.Rectangle((x - 0.12, 0), 0.24, 0.85, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6, zorder=3))
    ax.text(x, 1.05, str(t), ha="center", va="bottom", fontsize=15, color=MAVI, fontweight="bold")
for a, b in zip(xs[:-1], xs[1:]):
    ax.text((a + b) / 2, -0.12, "+4", ha="center", va="top", fontsize=13, color=SARI)
ax.text(3, -0.62, "5 direk (terim), 4 boşluk (ortak fark)", ha="center", va="top", fontsize=13, color=YAZI)
ax.set_xlim(-0.5, 6.5); ax.set_ylim(-1.05, 1.5)
kaydet(fig, __file__)
