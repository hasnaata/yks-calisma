import sys; sys.path.insert(0, "tools")
from cizim import *

# 3 günde bir kursa giden biri: 1. gidiş 0. gün, 10. gidiş 27. gün. 10 gidiş arasında 9 aralık var.
fig, ax = sekil(6.4, 2.5)
ax.axis("off")
ax.annotate("", xy=(29.5, 0), xytext=(-1.2, 0), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.4))
for k in range(10):
    g = 3 * k
    ilk_son = k in (0, 9)
    renk = KIRMIZI if k == 9 else MAVI
    ax.plot(g, 0, "o", ms=9, mfc=renk if ilk_son else "white", mec=renk, mew=1.8, zorder=5)
    ax.text(g, 0.55, f"{k + 1}.", ha="center", va="bottom", fontsize=11.5, color=renk,
            fontweight="bold" if ilk_son else "normal")
    if k in (0, 3, 6, 9):
        ax.text(g, -0.95, str(g), ha="center", va="top", fontsize=11.5, color=YAZI)
for k in range(9):
    ax.add_patch(patches.Arc((3 * k + 1.5, -0.05), 2.6, 1.4, theta1=180, theta2=360, color=SARI, lw=1.4))
ax.text(13.5, -1.85, "9 aralık × 3 gün = 27 gün", ha="center", va="top", fontsize=13, color=SARI)
ax.text(29.6, -0.95, "gün", ha="left", va="top", fontsize=11.5, color=SOLUK)
ax.set_xlim(-1.5, 31.5); ax.set_ylim(-2.6, 1.3)
kaydet(fig, __file__)
