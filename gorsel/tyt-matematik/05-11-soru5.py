import sys; sys.path.insert(0, "tools")
from cizim import *

# Kibritten evler: 1 ev 6, 2 ev 11, 3 ev 16 kibrit (5n + 1).
fig, ax = sekil(6.2, 2.8)
ax.axis("off")

def kibrit(x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], color=SARI, lw=4, solid_capstyle="round")
    ax.plot(x2, y2, "o", color=KIRMIZI, markersize=5)

bas = [0, 1.7, 4.3]
for n, x0 in zip((1, 2, 3), bas):
    for k in range(n):
        x = x0 + k
        if k == 0: kibrit(x, 0, x, 1)
        kibrit(x, 0, x + 1, 0); kibrit(x + 1, 0, x + 1, 1); kibrit(x, 1, x + 1, 1)
        kibrit(x, 1, x + 0.5, 1.866); kibrit(x + 1, 1, x + 0.5, 1.866)
    ax.text(x0 + n / 2, -0.3, f"{n}. şekil", ha="center", va="top", fontsize=12)
ax.set_xlim(-0.2, 7.5); ax.set_ylim(-0.8, 2.1); ax.set_aspect("equal")
kaydet(fig, __file__)
