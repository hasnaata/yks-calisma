import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = 4 − x: (0, 4), (4, 0). g(x) = x − 2: (0, −2), (2, 0). Kesişim (3, 1).
fig, ax = sekil(5.4, 4.6)
eksenler(ax, x=(-2.4, 6.4), y=(-3.4, 5.4), izgara=False)
ax.set_aspect("equal")
ax.set_xticks([]); ax.set_yticks([])
xs = np.linspace(-1.2, 6.2, 20)
ax.plot(xs, 4 - xs, color=MAVI); ax.plot(xs, xs - 2, color=YESIL)
nokta(ax, 0, 4, renk=MAVI); nokta(ax, 4, 0, renk=MAVI)
nokta(ax, 0, -2, renk=YESIL); nokta(ax, 2, 0, renk=YESIL)
ax.text(-0.2, 4, "4", ha="right", va="center", fontsize=13)
ax.text(4.1, -0.25, "4", ha="left", va="top", fontsize=13)
ax.text(-0.2, -2, "−2", ha="right", va="center", fontsize=13)
ax.text(2.0, 0.25, "2", ha="right", va="bottom", fontsize=13)
ax.text(0.4, 4.9, "y = f(x)", color=MAVI, fontsize=13)
ax.text(6.3, 4.7, "y = g(x)", ha="right", color=YESIL, fontsize=13)
kaydet(fig, __file__)
