import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 2: E = sınıf (24 kişi), A = bisiklet, B = paten. Yalnız A 9, ikisi 4, yalnız B 6, hiçbiri 5.
fig, ax = sekil(5.4, 3.6)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.2, 10.2); ax.set_ylim(-0.2, 6.4)
ax.add_patch(patches.Rectangle((0, 0), 10, 6.2, facecolor="white", edgecolor=SOLUK, lw=1.6))
ax.add_patch(patches.Ellipse((3.7, 3.2), 4.8, 4.2, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.add_patch(patches.Ellipse((6.3, 3.2), 4.8, 4.2, facecolor="none", edgecolor=YESIL, lw=2))
ax.text(9.4, 5.55, "E", fontsize=17, fontweight="bold", color=YAZI)
ax.text(0.5, 5.3, "Bisiklet", fontsize=14, fontweight="bold", color=MAVI)
ax.text(7.2, 5.3, "Paten", fontsize=14, fontweight="bold", color=YESIL)
for x0, y0, h in ((2.6, 3.2, "9"), (5.0, 3.2, "4"), (7.4, 3.2, "6"), (9.2, 0.6, "5")):
    ax.text(x0, y0, h, fontsize=22, ha="center", va="center", color=YAZI, fontweight="bold")
kaydet(fig, __file__)
