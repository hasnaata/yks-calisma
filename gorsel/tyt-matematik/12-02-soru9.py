import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 9. f: [−2, 3] -> [−3, 5], köşe noktaları (−2, −3), (0, 2), (2, 3), (3, 5); doğru parçaları.
# f⁻¹(3) = 2, f⁻¹(2) = 0, sonuç 0.
fig, ax = sekil(5.0, 5.0)
eksenler(ax, x=(-3.2, 4.2), y=(-3.8, 5.8))
ax.set_aspect("equal")
ax.set_xticks(range(-3, 5)); ax.set_xticklabels(["", "", "", "", "", "2", "3", ""])
ax.set_yticks(range(-3, 6)); ax.set_yticklabels(["", "", "", "", "", "2", "3", "", "5"])
P = [(-2, -3), (0, 2), (2, 3), (3, 5)]
ax.plot([p[0] for p in P], [p[1] for p in P], color=MAVI)
for px, py in P:
    nokta(ax, px, py, renk=MAVI)
    if px != 0:
        ax.plot([px, px], [0, py], color=SOLUK, lw=1.1, ls="--")
        ax.plot([0, px], [py, py], color=SOLUK, lw=1.1, ls="--")
ax.text(-2, 0.15, "−2", color=SOLUK, fontsize=13, ha="center", va="bottom")
ax.text(0.15, -3, "−3", color=SOLUK, fontsize=13, ha="left", va="center")
ax.text(3.2, 4.8, "f", color=MAVI, fontsize=16, fontweight="bold")
kaydet(fig, __file__)
