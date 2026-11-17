import sys; sys.path.insert(0, "tools")
from cizim import *

# İki zar: 6 · 6 = 36 sıralı ikili. "Toplam 7" olayının 6 elemanı yeşil.
fig, ax = sekil(6, 6.2)
ax.axis("off")
for a in range(1, 7):            # satır: 1. zar
    for b in range(1, 7):        # sütun: 2. zar
        x, y = b - 1, 6 - a
        yesil = a + b == 7
        ax.add_patch(patches.Rectangle((x, y), 1, 1, facecolor=YESIL_ACIK if yesil else "white",
                                       edgecolor=YESIL if yesil else CIZGI, lw=2 if yesil else 1, zorder=2 if yesil else 1))
        ax.text(x + 0.5, y + 0.5, f"{a},{b}", ha="center", va="center", fontsize=14,
                color=YESIL if yesil else YAZI, fontweight="bold" if yesil else "normal", zorder=3)
for i in range(1, 7):
    ax.text(i - 0.5, 6.25, str(i), ha="center", va="bottom", color=MAVI, fontsize=14, fontweight="bold")
    ax.text(-0.25, 6.5 - i, str(i), ha="right", va="center", color=KIRMIZI, fontsize=14, fontweight="bold")
ax.text(3, 6.85, "2. zar", ha="center", color=MAVI, fontsize=13)
ax.text(-0.85, 3, "1. zar", ha="center", va="center", rotation=90, color=KIRMIZI, fontsize=13)
ax.text(3, -0.45, "Yeşil kutular: toplam 7 (6 çıktı)", ha="center", va="top", color=YESIL, fontsize=13)
ax.set_xlim(-1.2, 6.1); ax.set_ylim(-1.1, 7.3); ax.set_aspect("equal")
kaydet(fig, __file__)
