import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 10: üzerinde 4, 9, 10, 15, 21, 25 yazan altı kart.
fig, ax = sekil(5.6, 1.6)
ax.axis("off"); ax.set_aspect("equal")
for i, r in enumerate([4, 9, 10, 15, 21, 25]):
    x = i * 1.35
    ax.add_patch(patches.FancyBboxPatch((x, 0), 1.0, 1.4, boxstyle="round,pad=0.02,rounding_size=0.12",
                                        facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
    ax.text(x + 0.5, 0.7, str(r), ha="center", va="center", fontsize=22, color=MAVI, fontweight="bold")
ax.set_xlim(-0.1, 5 * 1.35 + 1.1); ax.set_ylim(-0.1, 1.5)
kaydet(fig, __file__)
