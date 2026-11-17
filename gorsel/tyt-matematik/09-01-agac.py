import sys; sys.path.insert(0, "tools")
from cizim import *

# Ağaç şeması: 3 tişört (K, M, Y) ve 2 pantolon (S, G) ile 3 · 2 = 6 kombin.
fig, ax = sekil(6, 5.6)
ax.axis("off")
kok = (0, 0)
tis = {"K": 2.4, "M": 0, "Y": -2.4}
renk = {"K": KIRMIZI, "M": MAVI, "Y": YESIL}
nokta(ax, *kok)
ax.text(2.2, 4.15, "Tişört\n(3 yol)", ha="center", color=SOLUK, fontsize=12, va="center")
ax.text(4.6, 4.15, "Pantolon\n(her dalda 2 yol)", ha="center", color=SOLUK, fontsize=12, va="center")
ax.text(6.9, 4.15, "Kombin\n(6 tane)", ha="center", color=SOLUK, fontsize=12, va="center")
for t, y in tis.items():
    ax.plot([0, 2.2], [0, y], color=CIZGI, lw=1.8, zorder=1)
    ax.add_patch(patches.Circle((2.2, y), 0.34, facecolor="white", edgecolor=renk[t], lw=2, zorder=3))
    ax.text(2.2, y, t, ha="center", va="center", color=renk[t], fontsize=14, fontweight="bold", zorder=4)
    for p, dy in (("S", 0.6), ("G", -0.6)):
        y2 = y + dy
        ax.plot([2.55, 4.3], [y, y2], color=CIZGI, lw=1.8, zorder=1)
        ax.add_patch(patches.Circle((4.6, y2), 0.3, facecolor="white", edgecolor=SOLUK, lw=1.6, zorder=3))
        ax.text(4.6, y2, p, ha="center", va="center", color=YAZI, fontsize=13, zorder=4)
        ax.text(6.9, y2, f"({t}, {p})", ha="center", va="center", color=renk[t], fontsize=13)
ax.set_xlim(-0.6, 8.0); ax.set_ylim(-3.3, 4.8); ax.set_aspect("equal")
kaydet(fig, __file__)
