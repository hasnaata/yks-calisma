import sys; sys.path.insert(0, "tools")
from cizim import *

# Dağılma özelliği alan modeliyle: 7 · (10 + 3) = 7 · 10 + 7 · 3. Birim kareler gerçek ölçekte.
fig, ax = sekil(6, 3.4)
ax.axis("off"); ax.set_aspect("equal")
for x0, gen, dolgu, kenar in ((0, 10, MAVI_ACIK, MAVI), (10, 3, YESIL_ACIK, YESIL)):
    ax.add_patch(patches.Rectangle((x0, 0), gen, 7, facecolor=dolgu, edgecolor=kenar, lw=2.2))
    for i in range(1, gen): ax.plot([x0 + i, x0 + i], [0, 7], color=kenar, lw=0.4, alpha=0.35)
    for j in range(1, 7): ax.plot([x0, x0 + gen], [j, j], color=kenar, lw=0.4, alpha=0.35)
    ax.text(x0 + gen / 2, -0.7, str(gen), ha="center", va="top", fontsize=14, color=kenar)
ax.text(5, 3.5, "70", ha="center", va="center", fontsize=20, color=MAVI, fontweight="bold")
ax.text(11.5, 3.5, "21", ha="center", va="center", fontsize=20, color=YESIL, fontweight="bold")
ax.text(-0.6, 3.5, "7", ha="right", va="center", fontsize=14, color=YAZI)
ax.annotate("", xy=(13, 8.0), xytext=(0, 8.0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.3))
ax.text(6.5, 8.35, "10 + 3 = 13", ha="center", va="bottom", fontsize=13, color=YAZI)
ax.set_xlim(-1.5, 13.5); ax.set_ylim(-2, 9.3)
kaydet(fig, __file__)
