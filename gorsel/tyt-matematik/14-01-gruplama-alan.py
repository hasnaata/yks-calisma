import sys; sys.path.insert(0, "tools")
from cizim import *

# Gruplandırma alan modeliyle: xy + 2x + 3y + 6 = (x + 3)(y + 2). Ölçek x = 5, y = 4 için doğru.
x, y = 5, 4
fig, ax = sekil(5.5, 4.4)
ax.axis("off"); ax.set_aspect("equal")
hucreler = [  # (sol, alt, genişlik, yükseklik, dolgu, kenar, alan)
    (0, 2, x, y, MAVI_ACIK, MAVI, "$xy$"), (0, 0, x, 2, MAVI_ACIK, MAVI, "$2x$"),
    (x, 2, 3, y, YESIL_ACIK, YESIL, "$3y$"), (x, 0, 3, 2, YESIL_ACIK, YESIL, "$6$"),
]
for x0, y0, g, h, dolgu, kenar, alan in hucreler:
    ax.add_patch(patches.Rectangle((x0, y0), g, h, facecolor=dolgu, edgecolor=kenar, lw=2.2))
    ax.text(x0 + g / 2, y0 + h / 2, alan, ha="center", va="center", fontsize=19, color=kenar)
ax.text(x / 2, y + 2.4, "$x$", ha="center", va="bottom", fontsize=15, color=MAVI)
ax.text(x + 1.5, y + 2.4, "$3$", ha="center", va="bottom", fontsize=15, color=YESIL)
ax.text(-0.35, 2 + y / 2, "$y$", ha="right", va="center", fontsize=15, color=YAZI)
ax.text(-0.35, 1, "$2$", ha="right", va="center", fontsize=15, color=YAZI)
ax.text(x / 2, -0.4, "$x(y+2)$", ha="center", va="top", fontsize=14, color=MAVI)
ax.text(x + 1.5, -0.4, "$3(y+2)$", ha="center", va="top", fontsize=14, color=YESIL)
ax.set_xlim(-1.5, x + 3.6); ax.set_ylim(-1.9, y + 3.6)
kaydet(fig, __file__)
