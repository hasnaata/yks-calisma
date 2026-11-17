import sys; sys.path.insert(0, "tools")
from cizim import *

# 3 sıra × 3 sütun, eşit aralıklı 9 fidan (kare ızgara).
fig, ax = sekil(3.2, 3.2)
ax.set_aspect("equal"); ax.axis("off")
for i in range(3):
    for j in range(3):
        ax.plot(i, j, "o", color=YESIL, markersize=13, zorder=5)
ax.annotate("", xy=(1, -0.55), xytext=(0, -0.55), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(0.5, -0.7, "2 m", ha="center", va="top", color=SOLUK, fontsize=12)
ax.annotate("", xy=(-0.55, 1), xytext=(-0.55, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(-0.7, 0.5, "2 m", ha="right", va="center", color=SOLUK, fontsize=12)
ax.set_xlim(-1.4, 2.4); ax.set_ylim(-1.1, 2.4)
kaydet(fig, __file__)
