import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = x + 1, g(x) = 2 − x/2, (f + g)(x) = x/2 + 3.
# x = 2'de: f(2) = 3, g(2) = 1, (f + g)(2) = 4.
fig, ax = sekil(5.6, 4.2)
eksenler(ax, x=(-3.6, 5.6), y=(-1.6, 5.6))
ax.set_aspect("equal")
ax.set_xticks([-3, -2, -1, 1, 2, 3, 4, 5]); ax.set_xticklabels(["", "−2", "", "", "2", "", "4", ""])
ax.set_yticks([-1, 1, 2, 3, 4, 5]); ax.set_yticklabels(["", "1", "", "3", "4", ""])
xs = np.linspace(-2.6, 4.6, 20)
ax.plot(xs, xs + 1, color=MAVI)
ax.plot(xs, 2 - xs / 2, color=YESIL)
ax.plot(xs, xs / 2 + 3, color=KIRMIZI)
# x = 2'de yükseklikleri üst üste koy
ax.plot([2, 2], [0, 3], color=MAVI, lw=5, alpha=0.45, solid_capstyle="butt")
ax.plot([2.0, 2.0], [3, 4], color=YESIL, lw=5, alpha=0.7, solid_capstyle="butt")
nokta(ax, 2, 3, renk=MAVI); nokta(ax, 2, 1, renk=YESIL); nokta(ax, 2, 4, renk=KIRMIZI)
ax.text(2.25, 1.45, "f(2) = 3", color=MAVI, fontsize=12)
ax.text(2.55, 3.3, "+ g(2) = 1", color=YESIL, fontsize=12)
ax.text(-3.4, 4.95, "f + g", color=KIRMIZI, fontsize=13)
ax.text(-1.3, -1.35, "f", color=MAVI, fontsize=13)
ax.text(4.3, 0.15, "g", color=YESIL, fontsize=13)
ax.text(0.15, 4.45, "(f + g)(2) = 4", color=KIRMIZI, fontsize=12)
kaydet(fig, __file__)
