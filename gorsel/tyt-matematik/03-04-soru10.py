import sys; sys.path.insert(0, "tools")
from cizim import *

# d1: (3, 0) ve (0, 6) noktalarından geçer, 2x + y = 6.  d2: (−3, 0) ve (0, 3) noktalarından geçer, y = x + 3.
# Kesim noktası P(1, 4). Izgara yok; öğrenci denklemleri kurup bulmalı.
fig, ax = sekil(5.2, 5.0)
eksenler(ax, x=(-4.2, 4.2), y=(-1.5, 7.2), izgara=False)
ax.set_xticks([]); ax.set_yticks([])
xs = np.linspace(-0.6, 3.6, 10)
ax.plot(xs, 6 - 2 * xs, color=MAVI, lw=2.4)
xs2 = np.linspace(-4, 2.8, 10)
ax.plot(xs2, xs2 + 3, color=KIRMIZI, lw=2.4)
ax.text(2.0, 2.6, "d₁", color=MAVI, fontsize=15, fontweight="bold")
ax.text(2.55, 6.0, "d₂", color=KIRMIZI, fontsize=15, fontweight="bold")
for px, py, ad, dx, dy in [(3, 0, "3", -0.45, -0.75), (-3, 0, "−3", -0.2, -0.75), (0, 6, "6", 0.2, 0.05), (0, 3, "3", -0.5, 0.05)]:
    ax.plot(px, py, "o", color=YAZI, markersize=5, zorder=5)
    ax.text(px + dx, py + dy, ad, fontsize=13)
nokta(ax, 1, 4, "P", dx=-0.12, dy=0.4, renk=YESIL)
ax.text(-0.35, -0.65, "O", fontsize=13)
kaydet(fig, __file__)
