import sys; sys.path.insert(0, "tools")
from cizim import *

# 6 kişiden geziye gidecek 2 kişiyi seçmek = kalacak 4 kişiyi seçmek. C(6, 2) = C(6, 4) = 15.
fig, ax = sekil(6, 3.0)
ax.axis("off"); ax.set_aspect("equal")
for i in range(6):
    x = i * 1.0
    git = i < 2
    ax.add_patch(patches.Circle((x, 0), 0.32, facecolor=YESIL_ACIK if git else MAVI_ACIK,
                                edgecolor=YESIL if git else MAVI, lw=1.8))
    ax.text(x, 0, str(i + 1), ha="center", va="center", fontsize=14, color=YESIL if git else MAVI, fontweight="bold")
ax.add_patch(patches.FancyBboxPatch((-0.5, -0.5), 1.92, 1.0, boxstyle="round,pad=0.02,rounding_size=0.15",
                                    facecolor="none", edgecolor=YESIL, lw=2, linestyle="--"))
ax.add_patch(patches.FancyBboxPatch((1.58, -0.5), 3.92, 1.0, boxstyle="round,pad=0.02,rounding_size=0.15",
                                    facecolor="none", edgecolor=MAVI, lw=2, linestyle="--"))
ax.text(0.5, 0.75, "gidenler: 2", ha="center", fontsize=13, color=YESIL, fontweight="bold")
ax.text(3.5, 0.75, "kalanlar: 4", ha="center", fontsize=13, color=MAVI, fontweight="bold")
ax.text(2.5, -0.85, "C(6, 2) = C(6, 4) = 15", ha="center", va="top", fontsize=16, color=YAZI, fontweight="bold")
ax.set_xlim(-0.7, 5.7); ax.set_ylim(-1.6, 1.3)
kaydet(fig, __file__)
