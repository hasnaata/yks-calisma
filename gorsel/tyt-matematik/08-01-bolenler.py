import sys; sys.path.insert(0, "tools")
from cizim import *

# A = 12'nin pozitif bölenleri, B = 18'in pozitif bölenleri. Ortak: 1, 2, 3, 6.
fig, ax = sekil(5.8, 3.4)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 10); ax.set_ylim(0, 5.8)
ax.add_patch(patches.Ellipse((3.6, 2.7), 5.0, 4.4, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2, alpha=0.9))
ax.add_patch(patches.Ellipse((6.4, 2.7), 5.0, 4.4, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2, alpha=0.6))
ax.add_patch(patches.Ellipse((3.6, 2.7), 5.0, 4.4, facecolor="none", edgecolor=MAVI, lw=2))
ax.add_patch(patches.Ellipse((6.4, 2.7), 5.0, 4.4, facecolor="none", edgecolor=YESIL, lw=2))
ax.text(1.0, 5.1, "A", fontsize=17, fontweight="bold", color=MAVI)
ax.text(8.6, 5.1, "B", fontsize=17, fontweight="bold", color=YESIL)
for x, y, t in [(1.9, 3.4, "4"), (2.0, 2.0, "12")]:
    ax.text(x, y, t, fontsize=16, ha="center", va="center", color=MAVI)
for x, y, t in [(4.5, 3.6, "1"), (5.5, 3.6, "2"), (4.5, 2.0, "3"), (5.5, 2.0, "6")]:
    ax.text(x, y, t, fontsize=16, ha="center", va="center", color=YAZI, fontweight="bold")
for x, y, t in [(8.0, 3.4, "9"), (8.0, 2.0, "18")]:
    ax.text(x, y, t, fontsize=16, ha="center", va="center", color=YESIL)
kaydet(fig, __file__)
