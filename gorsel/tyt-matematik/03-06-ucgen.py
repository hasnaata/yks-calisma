import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: x > 0, y > 0, 2x + 3y < 12. Bütün sınırlar kesikli; içteki 7 tam sayı noktası yeşil, doğru üzerindeki (3, 2) boş.
fig, ax = sekil(5.2, 4.2)
eksenler(ax, x=(-0.8, 7), y=(-0.8, 5))
ax.set_xticks(range(1, 7)); ax.set_yticks(range(1, 5))
ax.add_patch(patches.Polygon([(0, 0), (6, 0), (0, 4)], closed=True, facecolor=MAVI_ACIK, edgecolor="none", zorder=0.2))
kes = dict(color=MAVI, ls=(0, (6, 4)), lw=2.2, zorder=3)
ax.plot([0, 6], [0, 0], **kes); ax.plot([0, 0], [0, 4], **kes); ax.plot([0, 6], [4, 0], **kes)
for x in range(1, 6):
    for y in range(1, 4):
        if 2 * x + 3 * y < 12: ax.plot(x, y, "o", color=YESIL, markersize=8, zorder=5)
nokta(ax, 3, 2, "", renk=KIRMIZI, dolu=False)
ax.text(3.2, 2.25, "(3, 2)", color=KIRMIZI, fontsize=12)
ax.text(4.1, 1.75, "2x + 3y = 12", color=MAVI, fontsize=12)
kaydet(fig, __file__)
