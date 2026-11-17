import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = 2x − 1: (0, −1) ve (2, 3) noktalarından geçer. g(x) = 4 − x: (0, 4) ve (4, 0).
# f(0) = −1, g(0) = 4, f(4) = 7, g(4) = 0.
fig, ax = sekil(4.6, 5.2)
eksenler(ax, x=(-1.6, 5.6), y=(-2.6, 8.4))
ax.set_aspect("equal")
ax.set_xticks([-1, 1, 2, 3, 4, 5]); ax.set_xticklabels(["", "1", "2", "3", "4", "5"])
ax.set_yticks([-2, -1, 1, 2, 3, 4, 5, 6, 7, 8]); ax.set_yticklabels(["", "−1", "1", "", "3", "4", "", "", "7", ""])
xs = np.linspace(-0.6, 4.6, 20); ax.plot(xs, 2 * xs - 1, color=MAVI)
xs = np.linspace(-1.4, 5.4, 20); ax.plot(xs, 4 - xs, color=YESIL)
ax.text(1.2, 7.6, "y = f(x)", color=MAVI, fontsize=13)
ax.text(4.0, -1.9, "y = g(x)", color=YESIL, fontsize=13)
kaydet(fig, __file__)
