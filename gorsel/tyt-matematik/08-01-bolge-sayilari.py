import sys; sys.path.insert(0, "tools")
from cizim import *

# s(A) = 15, s(B) = 11, s(A ∪ B) = 20  ->  s(A ∩ B) = 6, yalnız A = 9, yalnız B = 5.
fig, ax = sekil(5.8, 3.6)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 10); ax.set_ylim(-0.4, 5.8)
ax.add_patch(patches.Ellipse((3.6, 2.7), 5.0, 4.4, facecolor=MAVI_ACIK, edgecolor="none"))
ax.add_patch(patches.Ellipse((6.4, 2.7), 5.0, 4.4, facecolor=YESIL_ACIK, edgecolor="none", alpha=0.7))
ax.add_patch(patches.Ellipse((3.6, 2.7), 5.0, 4.4, facecolor="none", edgecolor=MAVI, lw=2))
ax.add_patch(patches.Ellipse((6.4, 2.7), 5.0, 4.4, facecolor="none", edgecolor=YESIL, lw=2))
ax.text(1.0, 5.1, "A", fontsize=17, fontweight="bold", color=MAVI)
ax.text(8.6, 5.1, "B", fontsize=17, fontweight="bold", color=YESIL)
ax.text(2.4, 2.7, "9", fontsize=24, ha="center", va="center", color=MAVI, fontweight="bold")
ax.text(5.0, 2.7, "6", fontsize=24, ha="center", va="center", color=YAZI, fontweight="bold")
ax.text(7.6, 2.7, "5", fontsize=24, ha="center", va="center", color=YESIL, fontweight="bold")
ax.text(5.0, 0.05, "9 + 6 = 15     6 + 5 = 11     9 + 6 + 5 = 20", fontsize=12.5, ha="center", color=SOLUK)
kaydet(fig, __file__)
