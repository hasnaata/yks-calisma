import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 11: 4 x 3 ızgara, D kavşağı (A'dan 2 sağ 1 yukarı) kapalı.
fig, ax = sekil(5, 3.9)
ax.axis("off"); ax.set_aspect("equal")
M, N = 4, 3
for x in range(M + 1): ax.plot([x, x], [0, N], color=SOLUK, lw=1.4)
for y in range(N + 1): ax.plot([0, M], [y, y], color=SOLUK, lw=1.4)
nokta(ax, 0, 0, "A", dx=-0.32, dy=-0.32, renk=YESIL)
ax.plot(2, 1, "X", color=KIRMIZI, markersize=13, zorder=6)
ax.text(2.13, 1.12, "D", color=KIRMIZI, fontsize=13)
nokta(ax, M, N, "B", dx=0.12, dy=0.08, renk=YAZI)
ax.set_xlim(-0.5, M + 0.5); ax.set_ylim(-0.5, N + 0.45)
kaydet(fig, __file__)
