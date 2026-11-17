import sys; sys.path.insert(0, "tools")
from cizim import *

# g: [−3, 5] → R, köşeler (−3, 2), (−1, −2), (2, 4), (5, 1). Tanım kümesi [−3, 5], görüntü kümesi [−2, 4].
fig, ax = sekil(5.8, 4.6)
eksenler(ax, x=(-4.6, 6.4), y=(-3.4, 5.4))
ax.set_aspect("equal")
ax.set_xticks([-3, -1, 1, 2, 3, 5]); ax.set_xticklabels(["−3", "−1", "1", "2", "3", "5"])
ax.set_yticks([-2, -1, 1, 2, 3, 4]); ax.set_yticklabels(["", "", "", "2", "", "4"])
ax.text(0.2, -2.15, "−2", color=SOLUK, fontsize=13, va="top")
X = [-3, -1, 2, 5]; Y = [2, -2, 4, 1]
# izdüşümler
ax.plot([-3, 5], [-0.0, 0.0], color=YESIL, lw=6, alpha=0.55, solid_capstyle="butt", zorder=2)
ax.plot([0, 0], [-2, 4], color=SARI, lw=6, alpha=0.55, solid_capstyle="butt", zorder=2)
for xv, yv in [(-3, 2), (5, 1)]:
    ax.plot([xv, xv], [0, yv], color=YESIL, ls="--", lw=1.2)
for xv, yv in [(-1, -2), (2, 4)]:
    ax.plot([0, xv], [yv, yv], color=SARI, ls="--", lw=1.2)
ax.plot(X, Y, color=MAVI, zorder=4)
for xv, yv in zip(X, Y):
    nokta(ax, xv, yv, renk=MAVI)
ax.text(2.6, -0.95, "Tanım kümesi", color=YESIL, fontsize=12, ha="center", fontweight="bold")
ax.text(-0.3, 4.75, "Görüntü kümesi", color=SARI, fontsize=12, ha="right", fontweight="bold")
ax.text(3.6, 3.4, "y = g(x)", color=MAVI, fontsize=13)
kaydet(fig, __file__)
