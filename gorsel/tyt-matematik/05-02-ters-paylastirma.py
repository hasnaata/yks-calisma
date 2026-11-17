import sys; sys.path.insert(0, "tools")
from cizim import *

# 180, 2, 3 ve 6 ile ters orantılı: 1/2, 1/3, 1/6 -> 6 ile genişlet -> 3 : 2 : 1 parça. Bir parça 30.
fig, ax = sekil(6.2, 2.6)
ax.axis("off"); ax.set_aspect("equal")
P = 1.0  # bir parçanın genişliği
kisiler = [("2 ile", 3, MAVI, MAVI_ACIK), ("3 ile", 2, YESIL, YESIL_ACIK), ("6 ile", 1, SARI, SARI_ACIK)]
x = 0
for ad, n, renk, acik in kisiler:
    for i in range(n):
        ax.add_patch(patches.Rectangle((x + i * P, 0), P, 0.8, facecolor=acik, edgecolor=renk, lw=1.4))
        ax.text(x + i * P + P / 2, 0.4, "30", ha="center", va="center", fontsize=12, color=renk)
    orta = x + n * P / 2
    ax.annotate("", xy=(x + 0.05, -0.25), xytext=(x + n * P - 0.05, -0.25),
                arrowprops=dict(arrowstyle="<->", color=renk, lw=1.3))
    ax.text(orta, -0.55, f"{n * 30}", ha="center", va="top", fontsize=14, color=renk, fontweight="bold")
    ax.text(orta, 1.05, f"{ad}\n{n} parça", ha="center", va="bottom", fontsize=11, color=YAZI)
    x += n * P
ax.text(x / 2, -1.25, "Toplam 6 parça = 180, bir parça = 30", ha="center", va="top", fontsize=11, color=SOLUK)
ax.set_xlim(-0.1, x + 0.1); ax.set_ylim(-1.6, 2.0)
kaydet(fig, __file__)
