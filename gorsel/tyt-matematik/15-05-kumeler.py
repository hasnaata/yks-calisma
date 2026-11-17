import sys; sys.path.insert(0, "tools")
from cizim import *

fig, ax = sekil(6.0, 3.6)
ax.axis("off"); ax.set_aspect("equal")
ax.set_xlim(0, 10); ax.set_ylim(0, 6)
ax.add_patch(patches.FancyBboxPatch((0.2, 0.2), 9.6, 5.6, boxstyle="round,pad=0,rounding_size=0.5",
                                    facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.add_patch(patches.FancyBboxPatch((0.7, 0.7), 4.6, 4.0, boxstyle="round,pad=0,rounding_size=0.4",
                                    facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2))
ax.text(0.6, 5.2, "ℂ  karmaşık sayılar", color=MAVI, fontsize=14, fontweight="bold", va="center")
ax.text(1.1, 4.2, "ℝ  gerçek sayılar", color=YESIL, fontsize=13, fontweight="bold", va="center")
for x, y, t in [(1.6, 3.2, "−5"), (3.4, 3.2, "3/4"), (1.8, 1.7, "√2"), (3.6, 1.7, "π")]:
    ax.text(x, y, t, fontsize=15, ha="center", va="center")
for x, y, t in [(6.6, 4.0, "i"), (8.5, 4.0, "3i"), (6.9, 2.4, "2 − 3i"), (8.3, 1.2, "√−9")]:
    ax.text(x, y, t, fontsize=15, ha="center", va="center", color=MAVI)
ax.text(5.0, -0.25, "Her gerçek sayı b = 0 olan karmaşık sayıdır: 5 = 5 + 0i", ha="center", va="top",
        color=SOLUK, fontsize=11.5)
kaydet(fig, __file__)
