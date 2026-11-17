import sys; sys.path.insert(0, "tools")
from cizim import *

# 72 + 27: onluk çubuklar (mavi) ve birlik küpler (yeşil). Toplam 9 onluk + 9 birlik = 9 · 11.
S = 0.32  # küp kenarı
fig, ax = sekil(6, 4.6)
ax.axis("off"); ax.set_aspect("equal")

def cubuk(x, y):
    ax.add_patch(patches.Rectangle((x, y), S, 10 * S, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.2))
    for k in range(1, 10):
        ax.plot([x, x + S], [y + k * S, y + k * S], color=MAVI, lw=0.6)

def kup(x, y):
    ax.add_patch(patches.Rectangle((x, y), S, S, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.2))

def satir(y, onluk, birlik, sayi):
    ax.text(1.0, y + 5 * S, f"{sayi} =", ha="right", va="center", fontsize=16, fontweight="bold")
    x = 1.3
    for _ in range(onluk):
        cubuk(x, y); x += S + 0.12
    x += 0.25
    for k in range(birlik):
        kup(x + (k % 5) * (S + 0.08), y + (k // 5) * (S + 0.08))
    ax.text(5.6, y + 5 * S, f"{onluk} onluk + {birlik} birlik", ha="left", va="center", fontsize=13,
            color=YAZI)

satir(4.4, 7, 2, 72)
satir(0.6, 2, 7, 27)
ax.plot([0, 10.6], [0.15, 0.15], color=CIZGI, lw=1.2)
ax.text(5.3, -0.35, "Toplam: 9 onluk + 9 birlik", ha="center", va="center", fontsize=14)
ax.text(5.3, -1.05, "9 · 10 + 9 · 1 = 9 · 11 = 99", ha="center", va="center", fontsize=15,
        color=MAVI, fontweight="bold")
ax.set_xlim(-0.1, 10.7); ax.set_ylim(-1.45, 4.4 + 10 * S + 0.1)
kaydet(fig, __file__)
