import sys; sys.path.insert(0, "tools")
from cizim import *

# 9 kişi. 6'şar verilince 8 artar, 8'er verilince 10 eksik kalır.
# Kişi başı 2 fazla vermek 8 + 10 = 18 ek ister: 18 ÷ 2 = 9 kişi.
fig, ax = sekil(6.4, 3.4)
ax.axis("off"); ax.set_aspect("equal")
N, W = 9, 0.62
y1, y2, h6, h2 = 1.75, 0.0, 0.9, 0.3
ax.text(-0.15, y1 + h6 / 2, "6'şar", ha="right", va="center", fontsize=13)
ax.text(-0.15, y2 + (h6 + h2) / 2, "8'er", ha="right", va="center", fontsize=13)
for i in range(N):
    x = i * W
    ax.add_patch(patches.Rectangle((x, y1), W, h6, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.2))
    ax.text(x + W / 2, y1 + h6 / 2, "6", ha="center", va="center", fontsize=12, color=MAVI)
    ax.add_patch(patches.Rectangle((x, y2), W, h6, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.2))
    ax.text(x + W / 2, y2 + h6 / 2, "6", ha="center", va="center", fontsize=12, color=MAVI)
    ax.add_patch(patches.Rectangle((x, y2 + h6), W, h2, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.2))
    ax.text(x + W / 2, y2 + h6 + h2 / 2, "+2", ha="center", va="center", fontsize=9.5, color=YESIL)
xe = N * W + 0.25
ax.add_patch(patches.Rectangle((xe, y1), 1.1, h6, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.4))
ax.text(xe + 0.55, y1 + h6 / 2, "8\nartar", ha="center", va="center", fontsize=11, color=SARI)
ax.add_patch(patches.Rectangle((xe, y2), 1.1, h6 + h2, facecolor="none", edgecolor=KIRMIZI, lw=1.4, ls="--"))
ax.text(xe + 0.55, y2 + (h6 + h2) / 2, "10\neksik", ha="center", va="center", fontsize=11, color=KIRMIZI)
ax.text((N * W) / 2, -0.3, "Kişi başı +2 için gereken: 8 + 10 = 18,  18 ÷ 2 = 9 kişi", ha="center", va="top", fontsize=11.5)
ax.set_xlim(-1.3, xe + 1.2); ax.set_ylim(-0.8, y1 + h6 + 0.1)
kaydet(fig, __file__)
