import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 10: a < b < 0 < c ve |a| > |c| > |b| (yalnızca 0 numaralı).
A, B, C = -2.8, -0.7, 1.5
fig, ax = sekil(6, 1.3)
ax.set_xlim(-3.6, 2.6); ax.set_ylim(-0.9, 0.7); ax.axis("off")
ax.annotate("", xy=(2.55, 0), xytext=(-3.55, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
for x, ad in ((A, "a"), (B, "b"), (0, "0"), (C, "c")):
    ax.plot([x, x], [-0.1, 0.1], color=SOLUK, lw=1.2)
    if ad == "0":
        ax.text(x, -0.3, "0", ha="center", va="top", fontsize=14)
    else:
        ax.plot(x, 0, "o", color=MAVI, markersize=8, zorder=5)
        ax.text(x, -0.3, ad, ha="center", va="top", fontsize=15, color=MAVI, style="italic")
kaydet(fig, __file__)
