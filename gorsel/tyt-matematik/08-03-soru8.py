import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 8: 50 kişi; yalnız A 2x, ikisi x, yalnız B x + 4, hiçbiri 6. 4x + 10 = 50 -> x = 10.
fig, ax = sekil(5.4, 3.6)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.2, 10.2); ax.set_ylim(-0.2, 6.4)
ax.add_patch(patches.Rectangle((0, 0), 10, 6.2, facecolor="white", edgecolor=SOLUK, lw=1.6))
ax.add_patch(patches.Ellipse((3.7, 3.2), 4.8, 4.2, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.add_patch(patches.Ellipse((6.3, 3.2), 4.8, 4.2, facecolor="none", edgecolor=YESIL, lw=2))
ax.text(9.4, 5.55, "E", fontsize=17, fontweight="bold", color=YAZI)
ax.text(1.2, 5.3, "A", fontsize=17, fontweight="bold", color=MAVI)
ax.text(8.4, 5.3, "B", fontsize=17, fontweight="bold", color=YESIL)
for x0, y0, h in ((2.6, 3.2, "2x"), (5.0, 3.2, "x"), (7.5, 3.2, "x + 4"), (9.2, 0.6, "6")):
    ax.text(x0, y0, h, fontsize=20, ha="center", va="center", color=YAZI, fontweight="bold")
kaydet(fig, __file__)
