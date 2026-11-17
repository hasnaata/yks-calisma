import sys; sys.path.insert(0, "tools")
from cizim import *

# a/3 = b/5 = c/7 = k: a 3 kutu, b 5 kutu, c 7 kutu; toplam 15 kutu = 45, bir kutu = 3.
SATIRLAR = [("a", 3, MAVI, MAVI_ACIK), ("b", 5, YESIL, YESIL_ACIK), ("c", 7, SARI, SARI_ACIK)]
fig, ax = sekil(6, 3.4)
ax.axis("off"); ax.set_aspect("equal")
for i, (ad, n, renk, acik) in enumerate(SATIRLAR):
    y = -i * 1.25
    ax.text(-0.45, y + 0.5, ad, ha="center", va="center", fontsize=17, color=renk, fontweight="bold")
    for j in range(n):
        ax.add_patch(patches.Rectangle((j, y), 0.92, 0.92, facecolor=acik, edgecolor=renk, lw=1.6))
        ax.text(j + 0.46, y + 0.46, "3", ha="center", va="center", fontsize=13, color=renk)
    ax.text(n + 0.25, y + 0.46, f"= {3 * n}", ha="left", va="center", fontsize=15, color=YAZI)
ax.text(-0.75, -3.35, "15 kutu = 45   →   1 kutu = k = 3", ha="left", va="center", fontsize=14, color=YAZI)
ax.set_xlim(-0.9, 9.6); ax.set_ylim(-3.8, 1.1)
kaydet(fig, __file__)
