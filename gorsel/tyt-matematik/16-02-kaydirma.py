import sys; sys.path.insert(0, "tools")
from cizim import *

# Aynı veri: olduğu gibi, her veriye +2, her veri ×2. Ortalama işaretli.
SATIRLAR = [("veri", [3, 5, 9, 10, 13], MAVI, "S = 4"),
            ("her veri + 2", [5, 7, 11, 12, 15], YESIL, "S = 4"),
            ("her veri × 2", [6, 10, 18, 20, 26], KIRMIZI, "S = 8")]
fig, ax = sekil(6, 3.6)
ax.set_xlim(-1, 36); ax.set_ylim(-0.6, 3.6); ax.axis("off")
for i, (ad, veri, renk, s) in enumerate(SATIRLAR):
    y = 3 - 1.25 * i
    ax.hlines(y, 0, 28, color=CIZGI, lw=1.2)
    for t in range(0, 29, 2):
        ax.plot([t, t], [y - 0.06, y + 0.06], color=CIZGI, lw=1)
    ort = sum(veri) / len(veri)
    ax.plot(veri, [y] * len(veri), "o", color=renk, markersize=9, zorder=4)
    ax.plot(ort, y - 0.25, "^", color=SARI, markersize=9, zorder=4)
    ax.text(0, y + 0.3, ad, fontsize=12, color=renk)
    ax.text(29.5, y, s, fontsize=13, color=renk, va="center")
for t in (0, 10, 20):
    ax.text(t, 0.2, str(t), ha="center", va="top", color=SOLUK, fontsize=11)
ax.text(14, -0.45, "▲ ortalama", ha="center", color=SARI, fontsize=11)
kaydet(fig, __file__)
