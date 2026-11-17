import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 9: y = 2x (düz), x + y = 6 (kesikli) ve x ekseni (düz) arasındaki üçgen bölge; köşeler (0,0), (6,0), (2,4).
fig, ax = sekil(5.2, 4.6)
eksenler(ax, x=(-1, 7.5), y=(-1, 6.5))
ax.set_xticks(range(1, 8)); ax.set_yticks(range(1, 7))
ax.add_patch(patches.Polygon([(0, 0), (6, 0), (2, 4)], closed=True, facecolor=MAVI_ACIK, edgecolor="none", zorder=0.2))
xs = np.linspace(-0.5, 3.2, 50); ax.plot(xs, 2 * xs, color=MAVI, zorder=3)
xs = np.linspace(0.5, 7, 50); ax.plot(xs, 6 - xs, color=MAVI, ls=(0, (6, 4)), zorder=3)
ax.plot([0, 6], [0, 0], color=MAVI, zorder=3)
ax.text(0.2, 3.3, "y = 2x", color=MAVI, fontsize=12)
ax.text(4.3, 2.3, "x + y = 6", color=MAVI, fontsize=12)
kaydet(fig, __file__)
