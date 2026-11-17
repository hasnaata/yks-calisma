import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders: E = {1, 2, ..., 10} evrensel kümesi, A = 10'dan küçük ya da eşit asal sayılar = {2, 3, 5, 7}.
fig, ax = sekil(5.6, 3.6)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 10); ax.set_ylim(0, 6.4)
ax.add_patch(patches.FancyBboxPatch((0.2, 0.2), 9.6, 5.6, boxstyle="round,pad=0,rounding_size=0.3",
                                    linewidth=2, edgecolor=SOLUK, facecolor="white"))
ax.text(0.45, 5.35, "E", fontsize=17, fontweight="bold", color=SOLUK, va="center")
ax.add_patch(patches.Ellipse((4.0, 3.0), 4.6, 4.0, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.text(2.0, 5.15, "A", fontsize=17, fontweight="bold", color=MAVI, va="center")
for x, y, t in [(3.0, 3.8, "2"), (4.9, 3.9, "3"), (3.2, 2.1, "5"), (5.0, 2.2, "7")]:
    nokta(ax, x, y, renk=MAVI); ax.text(x + 0.22, y, t, fontsize=15, va="center", color=MAVI)
for x, y, t in [(7.2, 4.7, "1"), (8.5, 3.9, "4"), (7.1, 3.0, "6"), (8.6, 2.1, "8"), (7.3, 1.1, "9"), (1.0, 1.0, "10")]:
    nokta(ax, x, y, renk=YAZI); ax.text(x + 0.22, y, t, fontsize=15, va="center")
kaydet(fig, __file__)
