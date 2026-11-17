import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: x + 2y ≤ 6 bölgesi; x ve y pozitif tam sayı olan 6 nokta yeşil.
fig, ax = sekil(5.4, 4.2)
eksenler(ax, x=(-1, 7.5), y=(-1, 4.5))
ax.set_xticks(range(1, 8)); ax.set_yticks(range(1, 5))
xs = np.linspace(-1, 7.5, 200)
ax.fill_between(xs, -1, 3 - xs / 2, color=MAVI_ACIK, zorder=0.2)
ax.plot(xs, 3 - xs / 2, color=MAVI, zorder=3)
for i in range(1, 7):
    for j in range(1, 4):
        if i + 2 * j <= 6:
            ax.plot(i, j, "o", color=YESIL, markersize=8, zorder=5)
ax.text(3.6, 2.0, "x + 2y = 6", color=MAVI, fontsize=12)
kaydet(fig, __file__)
