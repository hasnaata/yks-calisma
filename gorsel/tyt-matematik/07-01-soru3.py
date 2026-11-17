import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 3: E evrensel kümesi, A kümesi. A içinde k, l, m, n; dışında p, r.
fig, ax = sekil(4.6, 3.0)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 9); ax.set_ylim(0, 5.8)
ax.add_patch(patches.FancyBboxPatch((0.2, 0.2), 8.6, 5.2, boxstyle="round,pad=0,rounding_size=0.3",
                                    linewidth=2, edgecolor=SOLUK, facecolor="white"))
ax.text(0.45, 4.95, "E", fontsize=17, fontweight="bold", color=SOLUK, va="center")
ax.add_patch(patches.Ellipse((3.6, 2.7), 4.2, 3.6, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.text(1.7, 4.65, "A", fontsize=17, fontweight="bold", color=MAVI, va="center")
for x, y, t in [(2.7, 3.5, "k"), (4.4, 3.5, "l"), (2.8, 1.9, "m"), (4.5, 1.9, "n")]:
    nokta(ax, x, y, renk=MAVI); ax.text(x + 0.22, y, t, fontsize=15, va="center", color=MAVI)
for x, y, t in [(6.9, 3.7, "p"), (7.0, 1.6, "r")]:
    nokta(ax, x, y, renk=YAZI); ax.text(x + 0.22, y, t, fontsize=15, va="center")
kaydet(fig, __file__)
