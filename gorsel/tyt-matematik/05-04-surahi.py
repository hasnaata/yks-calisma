import sys; sys.path.insert(0, "tools")
from cizim import *

# Sürahi 12 eşit parçaya bölünmüş. 1/3 dolu (4 parça) iken 900 g, 3/4 dolu (9 parça) iken 1400 g.
# Fark 5 parça su = 500 g, 1 parça = 100 g; dolu suyun tamamı 1200 g, boş sürahi 900 − 400 = 500 g.
fig, ax = sekil(5.2, 4.2)
ax.axis("off"); ax.set_aspect("equal")
H, W = 0.4, 2.0
def kap(x0, dolu, baslik, kutle):
    for i in range(12):
        renk = MAVI_ACIK if i < dolu else "white"
        ax.add_patch(patches.Rectangle((x0, i * H), W, H, facecolor=renk, edgecolor=CIZGI, lw=0.8))
    ax.add_patch(patches.Rectangle((x0, 0), W, 12 * H, fill=False, edgecolor=SOLUK, lw=1.8))
    ax.text(x0 + W / 2, 12 * H + 0.2, baslik, ha="center", va="bottom", fontsize=12, color=YAZI)
    ax.text(x0 + W / 2, -0.25, kutle, ha="center", va="top", fontsize=13, color=MAVI, fontweight="bold")
kap(0, 4, "1/3 dolu", "900 g")
kap(3.6, 9, "3/4 dolu", "1400 g")
# fark: 5 parça
ax.add_patch(patches.Rectangle((3.6, 4 * H), W, 5 * H, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.6))
ax.annotate("", xy=(5.85, 4 * H), xytext=(5.85, 9 * H), arrowprops=dict(arrowstyle="<->", color=YESIL, lw=1.4))
ax.text(6.05, 6.5 * H, "5 parça\n= 500 g", ha="left", va="center", fontsize=12, color=YESIL, fontweight="bold")
ax.plot([W, 3.6], [4 * H, 4 * H], color=SOLUK, lw=1, ls="--")
ax.set_xlim(-0.2, 8.0); ax.set_ylim(-0.9, 12 * H + 0.8)
kaydet(fig, __file__)
