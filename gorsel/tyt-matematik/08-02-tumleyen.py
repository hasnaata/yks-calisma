import sys; sys.path.insert(0, "tools")
from cizim import *

# E = {1, ..., 10}, A = asal sayılar = {2, 3, 5, 7}. A' (A'nın dışı) boyalı.
fig, ax = sekil(5.6, 3.5)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.2, 9.2); ax.set_ylim(-0.3, 5.6)
ax.add_patch(patches.Rectangle((0, 0), 9, 5, facecolor=SARI_ACIK, edgecolor=SARI, lw=2))
ax.add_patch(patches.Circle((3.3, 2.5), 1.75, facecolor="white", edgecolor=MAVI, lw=2))
ax.text(8.55, 5.15, "E", fontsize=16, fontweight="bold", color=SARI, ha="center")
ax.text(1.85, 3.95, "A", fontsize=16, fontweight="bold", color=MAVI, ha="center")
ax.text(3.3, 2.5, "2   3\n5   7", fontsize=15, ha="center", va="center", linespacing=1.6, color=MAVI)
for x, y, t in ((6.1, 3.9, "1"), (7.6, 3.4, "4"), (6.3, 2.5, "6"), (7.9, 1.9, "8"), (6.4, 1.0, "9"), (0.7, 0.6, "10")):
    ax.text(x, y, t, fontsize=15, ha="center", va="center", color=SARI, fontweight="bold")
ax.text(7.6, 0.55, "A′", fontsize=16, fontweight="bold", color=SARI, ha="center")
kaydet(fig, __file__)
