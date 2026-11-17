import sys; sys.path.insert(0, "tools")
from cizim import *

# 72 m x 48 m bahçe, EBOB(72, 48) = 24 m kenarlı kare parsellere ayrılır: 3 x 2 = 6 parsel.
fig, ax = sekil(6, 4.2)
ax.axis("off"); ax.set_aspect("equal")
G, Y, k = 72, 48, 24
for i in range(G // k):
    for j in range(Y // k):
        ax.add_patch(patches.Rectangle((i * k, j * k), k, k, facecolor=YESIL_ACIK if (i + j) % 2 == 0 else MAVI_ACIK,
                                       edgecolor=MAVI, lw=1.4))
        ax.text(i * k + k / 2, j * k + k / 2, "24 × 24", ha="center", va="center", fontsize=12, color=YAZI)
ax.add_patch(patches.Rectangle((0, 0), G, Y, fill=False, edgecolor=YAZI, lw=2.4))
ax.annotate("", xy=(G, -5), xytext=(0, -5), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(G / 2, -7.5, "72 m = 3 · 24", ha="center", va="top", fontsize=13)
ax.annotate("", xy=(G + 5, Y), xytext=(G + 5, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(G + 7.5, Y / 2, "48 m = 2 · 24", ha="left", va="center", fontsize=13, rotation=90)
ax.text(G / 2, Y + 3, "EBOB(72, 48) = 24 → 3 · 2 = 6 parsel", ha="center", va="bottom", fontsize=13, color=MAVI, fontweight="bold")
ax.set_xlim(-3, G + 14); ax.set_ylim(-16, Y + 10)
kaydet(fig, __file__)
