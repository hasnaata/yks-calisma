import sys; sys.path.insert(0, "tools")
from cizim import *

# f: x < 2 için x/2 + 1 ((−2, 0) ve (0, 1) noktalarından geçer, (2, 2) boş);
# x ≥ 2 için 4 (sabit, (2, 4) dolu). f(−4) = −1, f(0) = 1, f(2) = 4.
fig, ax = sekil(5.6, 3.9)
eksenler(ax, x=(-5.6, 6.4), y=(-2.6, 5.4))
ax.set_aspect("equal")
ax.set_xticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]); ax.set_xticklabels(["", "−4", "", "−2", "", "", "2", "", "4", "", "6"])
ax.set_yticks([-2, -1, 1, 2, 3, 4, 5]); ax.set_yticklabels(["−2", "−1", "", "2", "3", "4", ""])
xs = np.linspace(-5.4, 2, 20); ax.plot(xs, xs / 2 + 1, color=MAVI)
ax.plot([2, 6.2], [4, 4], color=MAVI)
nokta(ax, 2, 2, renk=MAVI, dolu=False)
nokta(ax, 2, 4, renk=MAVI)
ax.text(3.6, 4.3, "y = f(x)", color=MAVI, fontsize=13)
kaydet(fig, __file__)
