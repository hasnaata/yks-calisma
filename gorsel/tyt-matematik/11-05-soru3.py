import sys; sys.path.insert(0, "tools")
from cizim import *

# Doğrusal f: (0, −2) ve (4, 0) noktalarından geçer. f(x) = x/2 − 2.
fig, ax = sekil(5, 3.6)
eksenler(ax, x=(-2.6, 6.6), y=(-3.6, 2.6))
ax.set_aspect("equal")
ax.set_xticks([]); ax.set_yticks([])
ax.grid(False)
xs = np.linspace(-2.4, 6.4, 30); ax.plot(xs, xs / 2 - 2, color=MAVI)
nokta(ax, 0, -2, "−2", dx=-1.05, dy=-0.15, renk=YAZI)
nokta(ax, 4, 0, "4", dx=-0.15, dy=0.3, renk=YAZI)
ax.text(-0.3, -0.45, "O", fontsize=12, color=YAZI)
ax.text(4.6, 1.6, "y = f(x)", color=MAVI, fontsize=13)
kaydet(fig, __file__)
