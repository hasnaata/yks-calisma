import sys; sys.path.insert(0, "tools")
from cizim import *

# 5 yatay cadde (birbirine paralel) ve bunlara dik 4 sokak (birbirine paralel).
# Örnek olarak bir dikdörtgen bölge taranır: 2 cadde + 2 sokak seçimi.
fig, ax = sekil(5, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ys = [0, 1, 2, 3, 4]; xs = [0, 1.8, 3.6, 5.4]
ax.add_patch(patches.Rectangle((1.8, 1), 3.6, 2, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2.4, zorder=1))
for i, y in enumerate(ys):
    ax.plot([-0.5, 5.9], [y, y], color=SOLUK, lw=2, zorder=2)
    ax.text(6.0, y, f"{i + 1}. cadde", va="center", fontsize=11, color=SOLUK)
for j, x in enumerate(xs):
    ax.plot([x, x], [-0.5, 4.5], color=YAZI, lw=2, zorder=2)
    ax.text(x, -0.65, f"{j + 1}. sokak", ha="center", va="top", fontsize=11, color=YAZI)
ax.set_xlim(-0.6, 7.3); ax.set_ylim(-1.2, 4.6)
kaydet(fig, __file__)
