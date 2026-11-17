import sys; sys.path.insert(0, "tools")
from cizim import *

# A = 2·2·5·3·7 = 420, B = 2·2·5·2·11 = 440. Ortak: 2, 2, 5; yalnız A: 3, 7; yalnız B: 2, 11.
fig, ax = sekil(5.4, 3.2)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Circle((-1.1, 0), 2.0, fc=MAVI_ACIK, ec=MAVI, lw=2, alpha=0.7))
ax.add_patch(patches.Circle((1.1, 0), 2.0, fc=SARI_ACIK, ec=SARI, lw=2, alpha=0.7))
ax.text(-1.9, 2.25, "A", ha="center", fontsize=17, color=MAVI, fontweight="bold")
ax.text(1.9, 2.25, "B", ha="center", fontsize=17, color=SARI, fontweight="bold")
ax.text(-2.05, 0.4, "3", ha="center", va="center", fontsize=18); ax.text(-2.05, -0.4, "7", ha="center", va="center", fontsize=18)
ax.text(2.05, 0.4, "2", ha="center", va="center", fontsize=18); ax.text(2.05, -0.4, "11", ha="center", va="center", fontsize=18)
for y, t in ((0.55, "2"), (0, "2"), (-0.55, "5")):
    ax.text(0, y, t, ha="center", va="center", fontsize=18)
ax.set_xlim(-3.4, 3.4); ax.set_ylim(-2.3, 2.7)
kaydet(fig, __file__)
