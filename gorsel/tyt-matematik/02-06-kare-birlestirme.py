import sys; sys.path.insert(0, "tools")
from cizim import *

# 18 cm x 12 cm eş dikdörtgenler; EKOK(18, 12) = 36 cm kenarlı en küçük kare: 2 x 3 = 6 parça.
fig, ax = sekil(6, 4.6)
ax.axis("off"); ax.set_aspect("equal")
# Solda tek parça
ax.add_patch(patches.Rectangle((0, 12), 18, 12, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.8))
ax.text(9, 10.5, "18 cm", ha="center", va="top", fontsize=12)
ax.text(-1.5, 18, "12 cm", ha="right", va="center", fontsize=12, rotation=90)
ax.text(9, 26, "1 parça", ha="center", va="bottom", fontsize=12, color=SARI)
ax.annotate("", xy=(30, 18), xytext=(22, 18), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.6))
# Sağda 36 x 36 kare
x0 = 34
for i in range(2):
    for j in range(3):
        ax.add_patch(patches.Rectangle((x0 + i * 18, j * 12), 18, 12, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.4))
ax.add_patch(patches.Rectangle((x0, 0), 36, 36, fill=False, edgecolor=MAVI, lw=2.6))
ax.text(x0 + 18, -1.5, "36 = 2 · 18", ha="center", va="top", fontsize=12)
ax.text(x0 + 37.5, 18, "36 = 3 · 12", ha="left", va="center", fontsize=12, rotation=90)
ax.text(x0 + 18, 38, "EKOK(18, 12) = 36 → 2 · 3 = 6 parça", ha="center", va="bottom", fontsize=12, color=MAVI, fontweight="bold")
ax.set_xlim(-5, x0 + 42); ax.set_ylim(-7, 44)
kaydet(fig, __file__)
