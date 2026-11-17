import sys; sys.path.insert(0, "tools")
from cizim import *

# x = 4 için kenarlar 7 ve 3 (ölçekli)
fig, ax = sekil(5, 2.8)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Rectangle((0, 0), 7, 3, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
for (px, py) in [(0, 0), (7, 0), (0, 3), (7, 3)]:
    pass
# dik açı işaretleri
for (cx, cy, sx, sy) in [(0, 0, 1, 1), (7, 0, -1, 1), (0, 3, 1, -1), (7, 3, -1, -1)]:
    ax.plot([cx + sx * 0.35, cx + sx * 0.35, cx], [cy, cy + sy * 0.35, cy + sy * 0.35], color=MAVI, lw=1.2)
ax.text(3.5, -0.45, "x + 3", ha="center", va="top", fontsize=14)
ax.text(-0.3, 1.5, "x − 1", ha="right", va="center", fontsize=14)
ax.text(3.5, 1.5, "Alan = 21 m²", ha="center", va="center", fontsize=14, color=MAVI)
ax.set_xlim(-1.8, 7.4); ax.set_ylim(-1.2, 3.4)
kaydet(fig, __file__)
