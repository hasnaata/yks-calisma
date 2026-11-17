import sys; sys.path.insert(0, "tools")
from cizim import *

# Kenarları x² − 7x + 11 = 0 denkleminin kökleri: (7 ± √5)/2 ≈ 4,618 ve 2,382 (ölçekli)
u, k = (7 + 5**0.5) / 2, (7 - 5**0.5) / 2
fig, ax = sekil(5, 3.2)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Rectangle((0, 0), u, k, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.plot([0, u], [0, k], color=SARI, lw=1.8, ls="--")
ax.text(u / 2, -0.3, "x₁", ha="center", va="top", fontsize=14)
ax.text(u + 0.2, k / 2, "x₂", ha="left", va="center", fontsize=14)
ax.text(u / 2 - 0.25, k / 2 + 0.25, "d", ha="center", va="center", fontsize=14, color=SARI)
ax.set_xlim(-0.3, u + 0.7); ax.set_ylim(-0.8, k + 0.3)
kaydet(fig, __file__)
