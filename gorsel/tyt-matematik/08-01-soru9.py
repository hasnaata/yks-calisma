import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 9: yalnız A = x + 3, A ∩ B = x, yalnız B = 2x − 1.
fig, ax = sekil(5.4, 3.2)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 10); ax.set_ylim(0.2, 5.6)
ax.add_patch(patches.Ellipse((3.6, 2.8), 5.0, 4.4, facecolor="none", edgecolor=MAVI, lw=2))
ax.add_patch(patches.Ellipse((6.4, 2.8), 5.0, 4.4, facecolor="none", edgecolor=MAVI, lw=2))
ax.text(1.0, 5.2, "A", fontsize=17, fontweight="bold", color=MAVI)
ax.text(8.6, 5.2, "B", fontsize=17, fontweight="bold", color=MAVI)
ax.text(2.4, 2.8, "x + 3", fontsize=16, ha="center", va="center")
ax.text(5.0, 2.8, "x", fontsize=17, ha="center", va="center")
ax.text(7.6, 2.8, "2x − 1", fontsize=16, ha="center", va="center")
kaydet(fig, __file__)
