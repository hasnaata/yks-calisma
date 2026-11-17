import sys; sys.path.insert(0, "tools")
from cizim import *

# (x² − 9)/(x² + x − 6): pay ve payda çarpan kutularına ayrılır, ortak kutu sadeleşir.
fig, ax = sekil(6, 3.4)
ax.axis("off")
ax.set_xlim(0, 10); ax.set_ylim(0, 5.4)

def kutu(x, y, yazi, renk, zemin):
    ax.add_patch(patches.FancyBboxPatch((x - 0.95, y - 0.42), 1.9, 0.84, boxstyle="round,pad=0.05",
                                        facecolor=zemin, edgecolor=renk, lw=1.8))
    ax.text(x, y, yazi, ha="center", va="center", fontsize=16, color=YAZI)

# kesir: pay üstte, payda altta
kutu(1.3, 3.6, "x − 3", MAVI, MAVI_ACIK)
kutu(3.5, 3.6, "x + 3", KIRMIZI, KIRMIZI_ACIK)
kutu(1.3, 1.6, "x − 2", MAVI, MAVI_ACIK)
kutu(3.5, 1.6, "x + 3", KIRMIZI, KIRMIZI_ACIK)
ax.plot([0.2, 4.6], [2.6, 2.6], color=YAZI, lw=2)
# ortak çarpanların üstü çizilir
for y in (3.6, 1.6):
    ax.plot([2.6, 4.4], [y - 0.45, y + 0.45], color=KIRMIZI, lw=2.4)
ax.annotate("", xy=(6.4, 2.6), xytext=(5.0, 2.6), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=2))
kutu(7.6, 3.6, "x − 3", MAVI, MAVI_ACIK)
kutu(7.6, 1.6, "x − 2", MAVI, MAVI_ACIK)
ax.plot([6.5, 8.7], [2.6, 2.6], color=YAZI, lw=2)
ax.text(2.4, 4.9, "x² − 9", ha="center", fontsize=13, color=SOLUK)
ax.text(2.4, 0.35, "x² + x − 6", ha="center", fontsize=13, color=SOLUK)
ax.text(7.6, 0.35, "x ≠ −3,  x ≠ 2", ha="center", fontsize=13, color=KIRMIZI)
kaydet(fig, __file__)
