import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 6: 5 x 3 ızgara, C noktası A'dan 2 sağ 1 yukarıda.
fig, ax = sekil(5.6, 3.6)
ax.axis("off"); ax.set_aspect("equal")
M, N = 5, 3
for x in range(M + 1): ax.plot([x, x], [0, N], color=SOLUK, lw=1.4)
for y in range(N + 1): ax.plot([0, M], [y, y], color=SOLUK, lw=1.4)
nokta(ax, 0, 0, "A", dx=-0.32, dy=-0.32, renk=YESIL)
nokta(ax, 2, 1, "C", dx=0.1, dy=0.1, renk=MAVI)
nokta(ax, M, N, "B", dx=0.12, dy=0.08, renk=KIRMIZI)
ax.set_xlim(-0.5, M + 0.5); ax.set_ylim(-0.5, N + 0.45)
kaydet(fig, __file__)
