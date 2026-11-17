import sys; sys.path.insert(0, "tools")
from cizim import *

# 1 + 3 + 5 + 7 = 16 = 4·4: her tek sayı karenin köşesine bir L ekler.
fig, ax = sekil(6, 3.4)
ax.axis("off"); ax.set_aspect("equal")
renkler = [(MAVI_ACIK, MAVI), (YESIL_ACIK, YESIL), (SARI_ACIK, SARI), (KIRMIZI_ACIK, KIRMIZI)]
n = 4
for i in range(n):
    for j in range(n):
        k = max(i, j)
        dolgu, kenar = renkler[k]
        ax.add_patch(patches.Rectangle((i, n - 1 - j), 1, 1, facecolor=dolgu, edgecolor=kenar, lw=1.3))
etiketler = ["1", "+ 3", "+ 5", "+ 7"]
for k, et in enumerate(etiketler):
    ax.text([5.0, 5.6, 6.8, 8.0][k], 2.6, et, ha="left", va="center", fontsize=17, color=renkler[k][1], fontweight="bold")
ax.text(5.0, 1.2, "= 16 = 4 · 4", ha="left", va="center", fontsize=16, color=YAZI)
ax.text(2, -0.35, "4 tek sayı, 4 × 4 kare", ha="center", va="top", fontsize=13, color=SOLUK)
ax.set_xlim(-0.2, 9.4); ax.set_ylim(-1.0, 4.2)
kaydet(fig, __file__)
