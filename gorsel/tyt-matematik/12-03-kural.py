import sys; sys.path.insert(0, "tools")
from cizim import *

# Doğru A(−2, 1) ve B(1, 7) noktalarından geçer: m = 6/3 = 2, n = 5, f(x) = 2x + 5.
fig, ax = sekil(5.0, 5.4)
eksenler(ax, x=(-3.6, 2.6), y=(-1.2, 8.6))
ax.set_aspect("equal")
ax.set_xticks([-3, -2, -1, 1, 2]); ax.set_xticklabels(["", "−2", "", "1", ""])
ax.set_yticks(range(1, 9)); ax.set_yticklabels(["", "", "", "", "", "", "7", ""])
xs = np.array([-3.1, 1.75]); ax.plot(xs, 2 * xs + 5, color=MAVI)
nokta(ax, -2, 1, renk=MAVI); nokta(ax, 1, 7, renk=MAVI); nokta(ax, 0, 5, renk=YESIL)
kutu = dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.9)
ax.text(-2.15, 1.45, "A(−2, 1)", color=MAVI, fontsize=12, ha="right", bbox=kutu)
ax.text(0.75, 7.55, "B(1, 7)", color=MAVI, fontsize=12, ha="right", bbox=kutu)
ax.text(-0.2, 5.25, "n = 5", color=YESIL, fontsize=12, ha="right", bbox=kutu)
# eğim üçgeni
ax.plot([-2, 1], [1, 1], color=SARI, lw=1.6, ls="--")
ax.plot([1, 1], [1, 7], color=SARI, lw=1.6, ls="--")
ax.text(-0.5, 0.35, "Δx = 3", color=SARI, fontsize=12, ha="center", bbox=kutu)
ax.text(1.15, 3.6, "Δy = 6", color=SARI, fontsize=12, ha="left", bbox=kutu)
kaydet(fig, __file__)
