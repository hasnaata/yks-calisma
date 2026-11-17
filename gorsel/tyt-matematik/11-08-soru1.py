import sys; sys.path.insert(0, "tools")
from cizim import *

# f: [−4, 4] → R, köşeler (−4, −1), (−2, 3), (1, 3), (4, −3). f(−2) = 3, f(4) = −3.
fig, ax = sekil(5.4, 4.4)
eksenler(ax, x=(-5.2, 5.4), y=(-4.2, 4.6))
ax.set_aspect("equal")
ax.set_xticks([-4, -3, -2, -1, 1, 2, 3, 4]); ax.set_xticklabels(["", "", "−2", "", "1", "", "", ""])
ax.set_yticks([-3, -2, -1, 1, 2, 3, 4]); ax.set_yticklabels([])
ax.text(-4, 0.15, "−4", color=SOLUK, fontsize=13, ha="center", va="bottom")
ax.text(4, 0.15, "4", color=SOLUK, fontsize=13, ha="center", va="bottom")
ax.text(0.15, 3.15, "3", color=SOLUK, fontsize=13, ha="left", va="bottom")
ax.text(0.15, -1, "−1", color=SOLUK, fontsize=13, ha="left", va="center")
ax.text(-0.15, -3, "−3", color=SOLUK, fontsize=13, ha="right", va="center")
X = [-4, -2, 1, 4]; Y = [-1, 3, 3, -3]
ax.plot(X, Y, color=MAVI)
nokta(ax, -4, -1, renk=MAVI); nokta(ax, 4, -3, renk=MAVI)
for xv, yv in [(-2, 3), (4, -3), (-4, -1)]:
    ax.plot([xv, xv], [0, yv], color=SOLUK, ls="--", lw=1)
    ax.plot([0, xv], [yv, yv], color=SOLUK, ls="--", lw=1)
ax.text(1.4, 3.3, "y = f(x)", color=MAVI, fontsize=13)
kaydet(fig, __file__)
