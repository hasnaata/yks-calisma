import sys; sys.path.insert(0, "tools")
from cizim import *

# f: [−4, 5] → R, köşeler (−4, 0), (−2, 3), (0, 1), (2, 4), (5, 1).
# f(x) = 2 → 4 kök; f(x) = k üç kök → k = 1 ya da k = 3.
fig, ax = sekil(5.6, 4.0)
eksenler(ax, x=(-5.0, 6.2), y=(-1.4, 5.0))
ax.set_aspect("equal")
ax.set_xticks([-4, -3, -2, -1, 1, 2, 3, 4, 5]); ax.set_xticklabels(["−4", "", "−2", "", "", "2", "", "", "5"])
ax.set_yticks([1, 2, 3, 4]); ax.set_yticklabels(["1", "2", "3", "4"])
X = [-4, -2, 0, 2, 5]; Y = [0, 3, 1, 4, 1]
ax.plot(X, Y, color=MAVI)
nokta(ax, -4, 0, renk=MAVI); nokta(ax, 5, 1, renk=MAVI)
ax.text(2.7, 3.7, "y = f(x)", color=MAVI, fontsize=13)
kaydet(fig, __file__)
