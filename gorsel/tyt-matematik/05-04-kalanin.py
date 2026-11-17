import sys; sys.path.insert(0, "tools")
from cizim import *

# Harçlık 12 parça (EKOK(3, 4) = 12). 1/3'ü kitap: 4 parça. Kalan 8 parçanın 1/4'ü sinema: 2 parça. Kalan 6 parça = 150 TL.
fig, ax = sekil(6.2, 2.9)
ax.axis("off"); ax.set_aspect("equal")
P = 1.0
gruplar = [("kitap", "tümün 1/3'ü", 4, MAVI, MAVI_ACIK), ("sinema", "kalanın 1/4'ü", 2, SARI, SARI_ACIK),
           ("kalan", "150 TL", 6, YESIL, YESIL_ACIK)]
x = 0
for ad, alt, n, renk, acik in gruplar:
    for i in range(n):
        ax.add_patch(patches.Rectangle((x + i * P, 0), P, 0.9, facecolor=acik, edgecolor=renk, lw=1.4))
    orta = x + n * P / 2
    ax.annotate("", xy=(x + 0.05, -0.25), xytext=(x + n * P - 0.05, -0.25),
                arrowprops=dict(arrowstyle="<->", color=renk, lw=1.3))
    ax.text(orta, -0.5, f"{n} parça", ha="center", va="top", fontsize=12, color=renk, fontweight="bold")
    ax.text(orta, 1.1, f"{ad}\n{alt}", ha="center", va="bottom", fontsize=11, color=YAZI)
    x += n * P
# kitaptan sonra kalan 8 parça
ax.annotate("", xy=(4.05, 2.55), xytext=(12 - 0.05, 2.55), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(8, 2.7, "kitaptan sonra kalan: 8 parça", ha="center", va="bottom", fontsize=11, color=SOLUK)
ax.text(6, -1.25, "6 parça = 150 TL  →  1 parça = 25 TL  →  harçlık = 300 TL", ha="center", va="top", fontsize=11, color=YAZI)
ax.set_xlim(-0.1, 12.1); ax.set_ylim(-1.7, 3.3)
kaydet(fig, __file__)
