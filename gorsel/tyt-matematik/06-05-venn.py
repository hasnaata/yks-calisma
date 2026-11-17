import sys; sys.path.insert(0, "tools")
from cizim import *

# E = {1, ..., 10}; p(x): x asal, q(x): x tek. Kesişim (p ∧ q) vurgulu.
fig, ax = sekil(5.6, 3.9)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Rectangle((-3.2, -2.1), 6.4, 4.2, facecolor="white", edgecolor=SOLUK, lw=1.2))
cp, cq, r = (-0.8, 0), (0.8, 0), 1.5
ax.add_patch(patches.Circle(cp, r, facecolor=MAVI_ACIK, edgecolor="none", alpha=0.7))
ax.add_patch(patches.Circle(cq, r, facecolor=MAVI_ACIK, edgecolor="none", alpha=0.7))
# kesişim: iki dairenin ortak bölgesi yeşil
ara = patches.Circle(cq, r, transform=ax.transData)
kes = patches.Circle(cp, r, facecolor=YESIL_ACIK, edgecolor="none")
ax.add_patch(kes); kes.set_clip_path(ara)
ax.add_patch(patches.Circle(cp, r, facecolor="none", edgecolor=MAVI, lw=2))
ax.add_patch(patches.Circle(cq, r, facecolor="none", edgecolor=MAVI, lw=2))
ax.text(-2.1, 1.4, "p: asal", fontsize=13, color=MAVI, fontweight="bold", ha="center")
ax.text(2.1, 1.4, "q: tek", fontsize=13, color=MAVI, fontweight="bold", ha="center")
ax.text(-2.85, 1.7, "E", fontsize=14, color=SOLUK, fontweight="bold", ha="center")
for x, y, s in [(-1.55, 0, "2")]:
    ax.text(x, y, s, fontsize=17, ha="center", va="center")
for x, y, s in [(0, 0.55, "3"), (0, 0, "5"), (0, -0.55, "7")]:
    ax.text(x, y, s, fontsize=17, ha="center", va="center", color=YESIL, fontweight="bold")
for x, y, s in [(1.55, 0.35, "1"), (1.55, -0.35, "9")]:
    ax.text(x, y, s, fontsize=17, ha="center", va="center")
for x, y, s in [(-2.75, -1.65, "4"), (-1.4, -1.8, "6"), (1.4, -1.8, "8"), (2.75, -1.65, "10")]:
    ax.text(x, y, s, fontsize=17, ha="center", va="center", color=SOLUK)
ax.set_xlim(-3.3, 3.3); ax.set_ylim(-2.2, 2.2)
kaydet(fig, __file__)
