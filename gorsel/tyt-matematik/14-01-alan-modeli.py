import sys; sys.path.insert(0, "tools")
from cizim import *

# Ortak çarpan alan modeliyle: 4x² + 6x = 2x · (2x + 3). Ölçek x = 3 için doğru: yükseklik 6, genişlikler 6 ve 3.
x = 3
fig, ax = sekil(5.5, 4)
ax.axis("off"); ax.set_aspect("equal")
h = 2 * x
for x0, gen, dolgu, kenar, alan in ((0, 2 * x, MAVI_ACIK, MAVI, "$4x^2$"), (2 * x, 3, YESIL_ACIK, YESIL, "$6x$")):
    ax.add_patch(patches.Rectangle((x0, 0), gen, h, facecolor=dolgu, edgecolor=kenar, lw=2.2))
    ax.text(x0 + gen / 2, h / 2, alan, ha="center", va="center", fontsize=22, color=kenar)
ax.text(x, -0.4, "$2x$", ha="center", va="top", fontsize=15, color=MAVI)
ax.text(2 * x + 1.5, -0.4, "$3$", ha="center", va="top", fontsize=15, color=YESIL)
ax.text(-0.4, h / 2, "$2x$", ha="right", va="center", fontsize=15, color=YAZI)
ax.annotate("", xy=(2 * x + 3, h + 0.8), xytext=(0, h + 0.8), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.3))
ax.text((2 * x + 3) / 2, h + 1.1, "$2x + 3$", ha="center", va="bottom", fontsize=15, color=YAZI)
ax.set_xlim(-2, 2 * x + 3.5); ax.set_ylim(-1.8, h + 2.3)
kaydet(fig, __file__)
