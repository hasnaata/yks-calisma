import sys; sys.path.insert(0, "tools")
from cizim import *

# Sınıfın %30'u 12 kişi. Şerit 10 parçaya (her biri %10) bölünür: 3 parça = 12 -> 1 parça = 4 -> 10 parça = 40.
fig, ax = sekil(6.2, 2.6)
ax.axis("off"); ax.set_aspect("equal")
for i in range(10):
    dolu = i < 3
    ax.add_patch(patches.Rectangle((i, 0), 1, 1, facecolor=SARI_ACIK if dolu else MAVI_ACIK,
                 edgecolor=SARI if dolu else MAVI, lw=1.4))
    ax.text(i + 0.5, 0.5, "4", ha="center", va="center", fontsize=13, color=SARI if dolu else MAVI)
    ax.text(i + 0.5, 1.15, "%10", ha="center", va="bottom", fontsize=9, color=SOLUK)
ax.annotate("", xy=(0.03, -0.3), xytext=(2.97, -0.3), arrowprops=dict(arrowstyle="<->", color=SARI, lw=1.3))
ax.text(1.5, -0.5, "%30 = 12 kişi", ha="center", va="top", fontsize=12, color=SARI)
ax.annotate("", xy=(0.03, -1.35), xytext=(9.97, -1.35), arrowprops=dict(arrowstyle="<->", color=MAVI, lw=1.3))
ax.text(5, -1.55, "%100 = 10 · 4 = 40 kişi", ha="center", va="top", fontsize=12, color=MAVI)
ax.set_xlim(-0.1, 10.1); ax.set_ylim(-2.3, 1.7)
kaydet(fig, __file__)
