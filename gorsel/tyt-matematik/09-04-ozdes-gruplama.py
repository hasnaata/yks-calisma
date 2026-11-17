import sys; sys.path.insert(0, "tools")
from cizim import *

# ADA: iki A'yı ayırt edersek 3! = 6 diziliş; A'lar özdeş olunca her ikili tek dizilişe iner.
fig, ax = sekil(6, 3.9)
ax.axis("off"); ax.set_aspect("equal")
gruplar = [("A$_1$ D A$_2$", "A$_2$ D A$_1$", "A D A"),
           ("A$_1$ A$_2$ D", "A$_2$ A$_1$ D", "A A D"),
           ("D A$_1$ A$_2$", "D A$_2$ A$_1$", "D A A")]
for i, (s1, s2, son) in enumerate(gruplar):
    y = -i * 1.25
    ax.add_patch(patches.FancyBboxPatch((0, y - 0.45), 4.4, 0.9, boxstyle="round,pad=0,rounding_size=0.12",
                                        facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))
    ax.text(1.1, y, s1, ha="center", va="center", fontsize=15, color=MAVI)
    ax.text(3.3, y, s2, ha="center", va="center", fontsize=15, color=MAVI)
    ax.annotate("", xy=(5.6, y), xytext=(4.6, y), arrowprops=dict(arrowstyle="-|>", color=SOLUK, lw=1.6))
    ax.add_patch(patches.FancyBboxPatch((5.8, y - 0.45), 1.9, 0.9, boxstyle="round,pad=0,rounding_size=0.12",
                                        facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.4))
    ax.text(6.75, y, son, ha="center", va="center", fontsize=15, color=YESIL, fontweight="bold")
ax.text(2.2, 0.85, "A'lar ayrı: 3! = 6", ha="center", va="bottom", fontsize=13, color=MAVI)
ax.text(6.75, 0.85, "A'lar özdeş: 3", ha="center", va="bottom", fontsize=13, color=YESIL)
ax.text(3.85, -3.4, "Her diziliş 2! = 2 kez sayılmış:  6 : 2 = 3", ha="center", va="center", fontsize=13, color=YAZI)
ax.set_xlim(-0.1, 7.8); ax.set_ylim(-3.75, 1.45)
kaydet(fig, __file__)
