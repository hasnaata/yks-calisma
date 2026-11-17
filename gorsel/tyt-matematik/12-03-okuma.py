import sys; sys.path.insert(0, "tools")
from cizim import *

# f: [−3, 4] → [−2, 5], köşeler (−3, −2), (0, 1), (1, 3), (4, 5). Artan, bire bir ve örten.
# f(1) = 3 (mavi: x ekseninden başla), f⁻¹(−2) = −3 (kırmızı: y ekseninden başla).
fig, ax = sekil(5.4, 5.2)
eksenler(ax, x=(-4.2, 5.2), y=(-3.2, 5.8))
ax.set_aspect("equal")
ax.set_xticks([-3, -2, -1, 1, 2, 3, 4]); ax.set_xticklabels([])
ax.set_yticks([-2, -1, 1, 2, 3, 4, 5]); ax.set_yticklabels([])
X = [-3, 0, 1, 4]; Y = [-2, 1, 3, 5]
ax.plot(X, Y, color=MAVI)
nokta(ax, -3, -2, renk=MAVI); nokta(ax, 4, 5, renk=MAVI)
kutu = dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.9)
# f(1) = 3: x = 1'den yukarı, sonra sola
ax.annotate("", xy=(1, 2.9), xytext=(1, 0), arrowprops=dict(arrowstyle="->", color=MAVI, lw=1.6, ls="--"))
ax.annotate("", xy=(0.1, 3), xytext=(1, 3), arrowprops=dict(arrowstyle="->", color=MAVI, lw=1.6, ls="--"))
nokta(ax, 1, 3, renk=MAVI)
ax.text(1, -0.25, "1", color=MAVI, ha="center", va="top", fontsize=13, fontweight="bold")
ax.text(-0.15, 3, "3", color=MAVI, ha="right", va="center", fontsize=13, fontweight="bold")
ax.text(1.35, 2.45, "f(1) = 3", color=MAVI, fontsize=12, bbox=kutu)
# f⁻¹(−2) = −3: y = −2'den sola, sonra yukarı x eksenine
ax.annotate("", xy=(-2.9, -2), xytext=(0, -2), arrowprops=dict(arrowstyle="->", color=KIRMIZI, lw=1.6, ls="--"))
ax.annotate("", xy=(-3, -0.1), xytext=(-3, -2), arrowprops=dict(arrowstyle="->", color=KIRMIZI, lw=1.6, ls="--"))
ax.text(0.15, -2, "−2", color=KIRMIZI, ha="left", va="center", fontsize=13, fontweight="bold")
ax.text(-3, 0.2, "−3", color=KIRMIZI, ha="center", va="bottom", fontsize=13, fontweight="bold")
ax.text(-2.2, -2.75, "f⁻¹(−2) = −3", color=KIRMIZI, fontsize=12, bbox=kutu)
# diğer işaretler
ax.text(4, -0.25, "4", color=SOLUK, ha="center", va="top", fontsize=12)
ax.text(-0.15, 5, "5", color=SOLUK, ha="right", va="center", fontsize=12)
ax.text(-0.15, 1, "1", color=SOLUK, ha="right", va="center", fontsize=12)
ax.text(-1, 0.2, "−1", color=SOLUK, ha="center", va="bottom", fontsize=12)
ax.text(2.6, 4.5, "f", color=MAVI, fontsize=15, fontweight="bold")
kaydet(fig, __file__)
