import sys; sys.path.insert(0, "tools")
from cizim import *

# Soru 8: ortak kenarı olan iki dikdörtgen. x = 3 alınarak orantılı çizildi:
# I: (x + 5) x (x + 4) = 8 x 7, II: (x + 2) x (x + 4) = 5 x 7.
X = 3.0
g1, g2, h = X + 5, X + 2, X + 4
fig, ax = sekil(6, 3.6)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Rectangle((0, 0), g1, h, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.add_patch(patches.Rectangle((g1, 0), g2, h, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2))
ax.text(g1 / 2, h / 2 + 0.7, "I", ha="center", va="center", fontsize=18, color=MAVI)
ax.text(g1 / 2, h / 2 - 0.7, r"Alan: $x^2 + 9x + 20$", ha="center", va="center", fontsize=13, color=MAVI)
ax.text(g1 + g2 / 2, h / 2 + 0.7, "II", ha="center", va="center", fontsize=18, color=YESIL)
ax.text(g1 + g2 / 2, h / 2 - 0.7, r"Alan:", ha="center", va="center", fontsize=13, color=YESIL)
ax.text(g1 + g2 / 2, h / 2 - 1.6, r"$x^2 + 6x + 8$", ha="center", va="center", fontsize=13, color=YESIL)
ax.set_xlim(-0.3, g1 + g2 + 0.3); ax.set_ylim(-0.3, h + 0.3)
kaydet(fig, __file__)
