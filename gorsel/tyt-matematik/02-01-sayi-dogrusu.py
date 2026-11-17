import sys; sys.path.insert(0, "tools")
from cizim import *

# 47'ye 0'dan 6'şar adımla gidilir: 7 tam adım 42'ye varır, kalan 5 birim bir adıma yetmez.
fig, ax = sekil(6.2, 2.4)
ax.axis("off")
ax.annotate("", xy=(50, 0), xytext=(-1.5, 0), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.4))
for t in range(0, 43, 6):
    ax.plot([t, t], [-0.25, 0.25], color=SOLUK, lw=1.2)
    ax.text(t, -0.6, str(t), ha="center", va="top", fontsize=12, color=YAZI)
for i in range(7):
    a = i * 6
    ax.add_patch(patches.Arc((a + 3, 0.15), 6, 3.2, theta1=0, theta2=180, color=MAVI, lw=1.8))
    ax.text(a + 3, 1.95, str(i + 1), ha="center", va="bottom", fontsize=12, color=MAVI)
ax.plot([42, 47], [0, 0], color=KIRMIZI, lw=5, solid_capstyle="butt")
ax.plot([47, 47], [-0.3, 0.3], color=KIRMIZI, lw=2)
ax.text(47, -0.6, "47", ha="center", va="top", fontsize=12, color=KIRMIZI, fontweight="bold")
ax.text(44.5, 0.55, "5", ha="center", va="bottom", fontsize=13, color=KIRMIZI, fontweight="bold")
ax.text(21, 3.0, "7 adım × 6 = 42", ha="center", va="bottom", fontsize=13, color=MAVI)
ax.text(46, 2.0, "kalan", ha="center", va="bottom", fontsize=13, color=KIRMIZI)
ax.set_xlim(-2, 51); ax.set_ylim(-1.6, 3.9)
kaydet(fig, __file__)
