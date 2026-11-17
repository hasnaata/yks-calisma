import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = x (birim), g(x) = c (sabit), c = 6 ile ölçekli; sayılar yazılmaz.
# Üçgen: O(0, 0), K(0, c), P(c, c). Alan = c^2 / 2 = 18.
c = 6
fig, ax = sekil(4.6, 4.2)
eksenler(ax, (-1.5, 9), (-1.5, 9), izgara=False)
ax.set_xticks([]); ax.set_yticks([])
x = np.linspace(-1.3, 8.6, 50)
ax.fill([0, 0, c], [0, c, c], color=SARI_ACIK, zorder=1)
ax.plot(x, x, color=MAVI, zorder=3)
ax.plot(x, 0 * x + c, color=YESIL, zorder=3)
nokta(ax, c, c, "P", dx=0.15, dy=0.3, renk=YAZI)
nokta(ax, 0, c, "K", dx=-0.75, dy=0.3, renk=YAZI)
ax.text(-0.75, -0.75, "O", fontsize=13)
ax.text(1.4, 4.4, "18", fontsize=14, color=SARI, fontweight="bold")
ax.text(7.0, 8.4, "y = f(x)", color=MAVI, fontsize=12, ha="center")
ax.text(7.9, c - 0.8, "y = g(x)", color=YESIL, fontsize=12, ha="center")
kaydet(fig, __file__)
