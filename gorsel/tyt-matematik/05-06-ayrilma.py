import sys; sys.path.insert(0, "tools")
from cizim import *

# A işi 10 günde, B 15 günde. İş = EKOK(10, 15) = 30 birim; A günde 3, B günde 2 birim.
# Birlikte 4 gün: 4 * 5 = 20 birim. A ayrılır; kalan 10 birimi B 10 / 2 = 5 günde yapar. Toplam 9 gün.
fig, ax = sekil(6.2, 3.0)
ax.axis("off")
h = 0.7
ax.add_patch(patches.Rectangle((0, 2), 4, h, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))
ax.text(-0.25, 2 + h / 2, "A", ha="right", va="center", fontsize=13, color=MAVI, fontweight="bold")
ax.text(2, 2 + h / 2, "günde 3 birim", ha="center", va="center", fontsize=11, color=MAVI)
ax.add_patch(patches.Rectangle((0, 1), 9, h, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.4))
ax.text(-0.25, 1 + h / 2, "B", ha="right", va="center", fontsize=13, color=SARI, fontweight="bold")
ax.text(6.5, 1 + h / 2, "günde 2 birim", ha="center", va="center", fontsize=11, color=SARI)
ax.plot([4, 4], [0.75, 3.0], color=KIRMIZI, lw=1.4, ls="--")
ax.text(4, 3.05, "A ayrılıyor", ha="center", va="bottom", fontsize=11, color=KIRMIZI)
# gün ekseni
ax.annotate("", xy=(9.6, 0.55), xytext=(0, 0.55), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.2))
for t in (0, 4, 9):
    ax.plot([t, t], [0.47, 0.63], color=SOLUK, lw=1.2)
    ax.text(t, 0.35, str(t), ha="center", va="top", fontsize=12, color=YAZI)
ax.text(9.7, 0.55, "gün", va="center", fontsize=11, color=SOLUK)
ax.text(2, -0.25, "4 · (3 + 2)\n= 20 birim", ha="center", va="top", fontsize=11, color=YAZI)
ax.text(6.5, -0.25, "kalan 30 − 20 = 10 birim\n10 ÷ 2 = 5 gün", ha="center", va="top", fontsize=11, color=YAZI)
ax.set_xlim(-0.8, 10.3); ax.set_ylim(-1.3, 3.5)
kaydet(fig, __file__)
