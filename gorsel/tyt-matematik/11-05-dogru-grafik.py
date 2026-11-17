import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = (2/3)x + 2 doğrusu: y eksenini (0, 2), x eksenini (−3, 0) noktasında keser.
# Adım üçgeni: (0, 2) noktasından 3 birim sağa, 2 birim yukarı -> (3, 4).
fig, ax = sekil(5.2, 4.4)
eksenler(ax, x=(-4.6, 5.4), y=(-1.6, 5.8))
ax.set_aspect("equal")
ax.set_xticks([-4, -3, -2, -1, 1, 2, 3, 4, 5]); ax.set_xticklabels(["−4", "−3", "−2", "−1", "1", "2", "3", "4", "5"])
ax.set_yticks([-1, 1, 2, 3, 4, 5]); ax.set_yticklabels(["−1", "1", "2", "3", "4", "5"])
xs = np.linspace(-4.4, 5.2, 50)
ax.plot(xs, 2 / 3 * xs + 2, color=MAVI)
ax.plot([0, 3], [2, 2], "--", color=YESIL, lw=1.6); ax.plot([3, 3], [2, 4], "--", color=YESIL, lw=1.6)
ax.text(1.5, 1.55, "3 sağa", ha="center", va="top", color=YESIL, fontsize=12)
ax.text(3.2, 3.0, "2 yukarı", ha="left", va="center", color=YESIL, fontsize=12)
nokta(ax, 0, 2, "(0, 2)", dx=-1.55, dy=0.2, renk=KIRMIZI)
nokta(ax, -3, 0, "(−3, 0)", dx=-0.9, dy=0.35, renk=KIRMIZI)
nokta(ax, 3, 4, "", renk=YESIL)
ax.text(1.6, 5.0, "y = f(x)", color=MAVI, fontsize=13)
kaydet(fig, __file__)
