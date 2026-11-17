import sys; sys.path.insert(0, "tools")
from cizim import *

# Ali işi 6 günde, Bora 12 günde bitirir. İş = EKOK(6, 12) = 12 birim.
# Ali günde 12/6 = 2 birim, Bora günde 12/12 = 1 birim; birlikte günde 3 birim -> 12/3 = 4 gün.
fig, ax = sekil(6.2, 2.8)
ax.axis("off"); ax.set_aspect("equal")
x = 0
for gun in range(4):
    for i, (renk, acik) in enumerate([(MAVI, MAVI_ACIK), (MAVI, MAVI_ACIK), (SARI, SARI_ACIK)]):
        ax.add_patch(patches.Rectangle((x + i, 0), 1, 0.9, facecolor=acik, edgecolor=renk, lw=1.4))
    ax.annotate("", xy=(x + 0.05, -0.25), xytext=(x + 2.95, -0.25), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
    ax.text(x + 1.5, -0.45, f"{gun + 1}. gün", ha="center", va="top", fontsize=12, color=YAZI)
    x += 3
# açıklama
ax.add_patch(patches.Rectangle((0, 1.35), 0.6, 0.5, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))
ax.text(0.8, 1.6, "Ali: günde 2 birim", va="center", fontsize=11, color=MAVI)
ax.add_patch(patches.Rectangle((6.4, 1.35), 0.6, 0.5, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.4))
ax.text(7.2, 1.6, "Bora: günde 1 birim", va="center", fontsize=11, color=SARI)
ax.text(6, -1.2, "İş = 12 birim, günde 3 birim  →  12 ÷ 3 = 4 gün", ha="center", va="top", fontsize=11, color=YAZI)
ax.set_xlim(-0.1, 12.1); ax.set_ylim(-1.7, 2.1)
kaydet(fig, __file__)
