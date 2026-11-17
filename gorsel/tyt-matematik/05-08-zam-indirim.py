import sys; sys.path.insert(0, "tools")
from cizim import *

# 100 TL -> %20 zam -> 120 TL -> %20 indirim -> 96 TL. Zammın tabanı 100, indirimin tabanı 120.
fig, ax = sekil(6.0, 3.6)
ax.axis("off")
G = 1.2
cubuklar = [(0, 100, "ilk fiyat", MAVI, MAVI_ACIK), (2.6, 120, "%20 zam", SARI, SARI_ACIK), (5.2, 96, "%20 indirim", KIRMIZI, KIRMIZI_ACIK)]
for x, h, ad, renk, acik in cubuklar:
    ax.add_patch(patches.Rectangle((x, 0), G, h, facecolor=acik, edgecolor=renk, lw=1.5))
    if h < 100:
        ax.add_patch(patches.Rectangle((x, h), G, 100 - h, facecolor="none", edgecolor=KIRMIZI, lw=1.4, ls="--"))
        ax.text(x + G / 2, h - 3, f"{h} TL", ha="center", va="top", fontsize=12, color=YAZI, fontweight="bold")
    else:
        ax.text(x + G / 2, h + 3, f"{h} TL", ha="center", va="bottom", fontsize=12, color=YAZI, fontweight="bold")
    ax.text(x + G / 2, -5, ad, ha="center", va="top", fontsize=11, color=renk)
ax.plot([-0.2, 6.5], [100, 100], ls="--", color=SOLUK, lw=1)
ax.annotate("", xy=(2.55, 110), xytext=(1.25, 104), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.3))
ax.text(1.9, 113, "+20", ha="center", va="bottom", fontsize=11, color=SARI)
ax.annotate("", xy=(5.15, 106), xytext=(3.85, 118), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.3))
ax.text(4.6, 118, "−24", ha="center", va="bottom", fontsize=11, color=KIRMIZI)
ax.text(6.55, 98, "4 TL eksik", ha="left", va="center", fontsize=11, color=KIRMIZI)
ax.set_xlim(-0.3, 8.6); ax.set_ylim(-20, 135)
kaydet(fig, __file__)
