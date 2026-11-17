import sys; sys.path.insert(0, "tools")
from cizim import *

# Aynı f. f⁻¹(x) < 0 ⇔ x = f(t), t ∈ [−3, 0) ⇔ x ∈ [−2, 1).
# x ekseninde [−3, 0) yeşil (f⁻¹'in değerleri), y ekseninde [−2, 1) sarı (aranan x'ler).
fig, ax = sekil(5.4, 5.2)
eksenler(ax, x=(-4.2, 5.2), y=(-3.2, 5.8))
ax.set_aspect("equal")
ax.set_xticks([-3, -2, -1, 1, 2, 3, 4]); ax.set_xticklabels([])
ax.set_yticks([-2, -1, 1, 2, 3, 4, 5]); ax.set_yticklabels([])
X = [-3, 0, 1, 4]; Y = [-2, 1, 3, 5]
ax.plot(X, Y, color=SOLUK, lw=1.6)
ax.plot([-3, 0], [-2, 1], color=KIRMIZI, lw=3)
nokta(ax, -3, -2, renk=KIRMIZI); nokta(ax, 0, 1, renk=KIRMIZI, dolu=False); nokta(ax, 4, 5, renk=SOLUK)
ax.plot([-3, 0], [0, 0], color=YESIL, lw=7, alpha=0.55, solid_capstyle="butt")
ax.plot([0, 0], [-2, 1], color=SARI, lw=7, alpha=0.55, solid_capstyle="butt")
ax.plot([-3, -3], [-2, 0], color=SOLUK, ls=":", lw=1.2)
ax.plot([-3, 0], [-2, -2], color=SOLUK, ls=":", lw=1.2)
ax.text(-3, 0.25, "−3", color=YESIL, ha="center", va="bottom", fontsize=13, fontweight="bold")
ax.text(0.2, -2, "−2", color=SARI, ha="left", va="center", fontsize=13, fontweight="bold")
ax.text(0.2, 1, "1", color=SARI, ha="left", va="center", fontsize=13, fontweight="bold")
ax.text(-1.5, 0.55, "f⁻¹(x) < 0", color=YESIL, ha="center", fontsize=12)
ax.text(0.45, -1.1, "x ∈ [−2, 1)", color=SARI, ha="left", fontsize=12,
        bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.9))
ax.text(2.6, 4.5, "f", color=SOLUK, fontsize=15, fontweight="bold")
kaydet(fig, __file__)
