import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = ax + b doğrusu (0, −2) ve (3, 4) noktalarından geçer: b = −2, a = 2, f(x) = 2x − 2.
fig, ax = sekil(5, 4.6)
eksenler(ax, x=(-1.6, 5.2), y=(-2.8, 6.4))
ax.set_aspect("equal")
ax.set_xticks([-1, 1, 2, 3, 4, 5]); ax.set_yticks([-2, -1, 1, 2, 3, 4, 5, 6])
ax.set_xticklabels(["−1", "1", "2", "3", "4", "5"]); ax.set_yticklabels(["−2", "−1", "1", "2", "3", "4", "5", "6"])
xs = np.linspace(-0.35, 4.1, 50)
ax.plot(xs, 2 * xs - 2, color=MAVI)
ax.plot([3, 3], [0, 4], "--", color=SOLUK, lw=1.2); ax.plot([0, 3], [4, 4], "--", color=SOLUK, lw=1.2)
nokta(ax, 0, -2, "(0, −2)", dx=0.25, dy=-0.55, renk=KIRMIZI)
nokta(ax, 3, 4, "(3, 4)", dx=0.3, dy=-0.5, renk=KIRMIZI)
ax.text(1.0, 5.4, "y = f(x)", color=MAVI, fontsize=13)
kaydet(fig, __file__)
