import sys; sys.path.insert(0, "tools")
from cizim import *

# Kare masalar yan yana: 1 masa 4, 2 masa 6, 3 masa 8 kişi (2n + 2).
fig, ax = sekil(6.2, 2.6)
ax.axis("off")

def sandalye(x, y):
    ax.add_patch(patches.Circle((x, y), 0.17, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))

bas = [0.4, 2.3, 5.1]
for n, x0 in zip((1, 2, 3), bas):
    for k in range(n):
        x = x0 + 0.8 * k
        ax.add_patch(patches.Rectangle((x, 0), 0.8, 0.8, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.6))
        sandalye(x + 0.4, 1.08); sandalye(x + 0.4, -0.28)
    sandalye(x0 - 0.28, 0.4); sandalye(x0 + 0.8 * n + 0.28, 0.4)
    ax.text(x0 + 0.4 * n, -0.6, f"{n} masa", ha="center", va="top", fontsize=12)
ax.set_xlim(-0.1, 8.25); ax.set_ylim(-1.05, 1.4); ax.set_aspect("equal")
kaydet(fig, __file__)
