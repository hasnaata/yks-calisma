import sys; sys.path.insert(0, "tools")
from cizim import *

# %10'luk 200 g (20 g tuz) + %25'lik 100 g (25 g tuz) = %15'lik 300 g (45 g tuz). Yükseklik kütleyle orantılı.
fig, ax = sekil(6.0, 4.0)
ax.axis("off")
G = 1.3
kaplar = [(0, 200, 20, "%10"), (2.5, 100, 25, "%25"), (5.0, 300, 45, "%15")]
for x, m, t, yuzde in kaplar:
    ax.add_patch(patches.Rectangle((x, 0), G, t, facecolor=MAVI, edgecolor=MAVI, lw=1.2))
    ax.add_patch(patches.Rectangle((x, t), G, m - t, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.2))
    ax.text(x + G / 2, t / 2, f"{t} g tuz", ha="center", va="center", color="white", fontsize=10, fontweight="bold")
    ax.text(x + G / 2, m + 8, f"{m} g", ha="center", va="bottom", color=YAZI, fontsize=12, fontweight="bold")
    ax.text(x + G / 2, -10, yuzde, ha="center", va="top", color=MAVI, fontsize=13, fontweight="bold")
ax.text(1.9, 60, "+", ha="center", va="center", fontsize=22, color=SOLUK)
ax.text(4.4, 60, "=", ha="center", va="center", fontsize=22, color=SOLUK)
ax.set_xlim(-0.2, 6.5); ax.set_ylim(-45, 330)
kaydet(fig, __file__)
