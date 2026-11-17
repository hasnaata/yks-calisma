import sys; sys.path.insert(0, "tools")
from cizim import *

# 3 x 3 boş tablo; satır toplamları sağda, sütun toplamları altta.
fig, ax = sekil(4.4, 4.0)
ax.axis("off"); ax.set_aspect("equal")
for i in range(4):
    ax.plot([0, 3], [i, i], color=YAZI, lw=1.6)
    ax.plot([i, i], [0, 3], color=YAZI, lw=1.6)
for r in range(3):
    y = 2.5 - r
    ax.annotate("", xy=(3.75, y), xytext=(3.1, y), arrowprops=dict(arrowstyle="-|>", color=MAVI, lw=1.6))
ax.text(3.9, 1.5, "satır\ntoplamları", va="center", ha="left", fontsize=13, color=MAVI)
for c in range(3):
    x = 0.5 + c
    ax.annotate("", xy=(x, -0.7), xytext=(x, -0.1), arrowprops=dict(arrowstyle="-|>", color=YESIL, lw=1.6))
ax.text(1.5, -0.95, "sütun toplamları", va="top", ha="center", fontsize=13, color=YESIL)
ax.set_xlim(-0.2, 5.6); ax.set_ylim(-1.5, 3.2)
kaydet(fig, __file__)
