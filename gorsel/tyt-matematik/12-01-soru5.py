import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 5. f(x) = 3 − x (mavi), g(x) = 2x − 1 (yeşil). Kurallar soruda verilmez.
fig, ax = sekil(5.0, 4.8)
eksenler(ax, x=(-1.6, 4.6), y=(-1.6, 4.6))
ax.set_aspect("equal")
ax.set_xticks(range(-1, 5)); ax.set_xticklabels(["", "", "1", "2", "3", "4"])
ax.set_yticks(range(-1, 5)); ax.set_yticklabels(["−1", "", "1", "2", "3", "4"])
xs = np.linspace(-1.2, 4.3, 20); ax.plot(xs, 3 - xs, color=MAVI)
xs = np.linspace(-0.3, 2.6, 20); ax.plot(xs, 2 * xs - 1, color=YESIL)
for p in ((0, 3), (3, 0)): nokta(ax, *p, renk=MAVI)
for p in ((0, -1), (2, 3)): nokta(ax, *p, renk=YESIL)
ax.text(-1.25, 3.7, "f", color=MAVI, fontsize=15, fontweight="bold")
ax.text(2.75, 3.55, "g", color=YESIL, fontsize=15, fontweight="bold")
kaydet(fig, __file__)
