import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders: A ⊆ B ve B ⊆ C ise A ⊆ C (iç içe üç küme).
fig, ax = sekil(5.0, 3.4)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 10); ax.set_ylim(0, 6.6)
ax.add_patch(patches.Ellipse((5.0, 3.1), 9.4, 6.0, facecolor="white", edgecolor=SOLUK, lw=2))
ax.text(1.2, 5.7, "C", fontsize=18, fontweight="bold", color=SOLUK, va="center")
ax.add_patch(patches.Ellipse((4.4, 3.0), 6.6, 4.4, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2))
ax.text(1.75, 4.85, "B", fontsize=18, fontweight="bold", color=YESIL, va="center")
ax.add_patch(patches.Ellipse((3.9, 3.0), 3.4, 2.4, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.text(3.75, 3.0, "A", fontsize=18, fontweight="bold", color=MAVI, va="center")
kaydet(fig, __file__)
