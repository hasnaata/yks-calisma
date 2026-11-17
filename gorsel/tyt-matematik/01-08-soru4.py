import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 4: 2,4 ile 2,5 arası 4 eş parçaya bölünmüş; K üçüncü çentikte (2,475).
fig, ax = sekil(6, 1.6)
a, b = 2.4, 2.5
ax.set_xlim(a - 0.02, b + 0.02); ax.set_ylim(-0.9, 0.9); ax.axis("off")
ax.annotate("", xy=(b + 0.018, 0), xytext=(a - 0.018, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
for i in range(5):
    t = a + i * 0.025
    ax.plot([t, t], [-0.12, 0.12], color=SOLUK, lw=1.4)
for t in (a, b):
    ax.text(t, -0.3, f"{t:.1f}".replace(".", ","), ha="center", va="top", fontsize=14)
nokta(ax, a + 3 * 0.025, 0, "")
ax.text(a + 3 * 0.025, 0.3, "K", ha="center", va="bottom", fontsize=15, color=MAVI, fontweight="bold")
kaydet(fig, __file__)
