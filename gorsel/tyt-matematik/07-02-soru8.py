import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 8: A = {1, 2}, B = {1, 2, 3, 4, 5}; A ⊆ B.
fig, ax = sekil(5.0, 3.4)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 10); ax.set_ylim(0, 6.6)
ax.add_patch(patches.Ellipse((5.0, 3.1), 9.4, 6.0, facecolor="white", edgecolor=SOLUK, lw=2))
ax.text(1.2, 5.7, "B", fontsize=18, fontweight="bold", color=SOLUK, va="center")
ax.add_patch(patches.Ellipse((3.6, 3.1), 3.8, 3.0, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.text(2.0, 4.65, "A", fontsize=18, fontweight="bold", color=MAVI, va="center")
for x, y, t in [(2.8, 3.1, "1"), (4.2, 3.1, "2")]:
    nokta(ax, x, y, renk=MAVI); ax.text(x + 0.25, y, t, fontsize=16, va="center", color=MAVI)
for x, y, t in [(6.9, 4.5, "3"), (7.7, 3.1, "4"), (6.9, 1.7, "5")]:
    nokta(ax, x, y); ax.text(x + 0.25, y, t, fontsize=16, va="center")
kaydet(fig, __file__)
