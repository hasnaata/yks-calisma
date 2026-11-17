import sys; sys.path.insert(0, "tools")
from cizim import *

# Aynı g: köşeler (−3, 2), (−1, −2), (2, 4), (5, 1). Kökler −2 ve 0.
# g > 0: [−3, −2) ∪ (0, 5]; g < 0: (−2, 0).
fig, ax = sekil(5.8, 4.4)
eksenler(ax, x=(-4.6, 6.4), y=(-3.4, 5.4))
ax.set_aspect("equal")
ax.set_xticks([-3, -2, -1, 1, 2, 3, 4, 5]); ax.set_xticklabels(["−3", "", "−1", "", "", "", "", "5"])
ax.set_yticks([-2, -1, 1, 2, 3, 4]); ax.set_yticklabels(["", "", "", "2", "", "4"])
xs = np.linspace(-3, 5, 801); ys = np.interp(xs, [-3, -1, 2, 5], [2, -2, 4, 1])
ax.fill_between(xs, ys, 0, where=ys >= 0, color=MAVI_ACIK, zorder=1)
ax.fill_between(xs, ys, 0, where=ys <= 0, color=KIRMIZI_ACIK, zorder=1)
ax.plot(xs, np.where(ys >= 0, ys, np.nan), color=MAVI, zorder=4)
ax.plot(xs, np.where(ys <= 0, ys, np.nan), color=KIRMIZI, zorder=4)
nokta(ax, -3, 2, renk=MAVI); nokta(ax, 5, 1, renk=MAVI)
nokta(ax, -2, 0, renk=YAZI); nokta(ax, 0, 0, renk=YAZI)
ax.text(-1.85, 0.2, "−2", ha="left", va="bottom", fontsize=12)
ax.text(0.25, 0.3, "0", fontsize=12)
ax.text(2.0, 0.55, "g(x) > 0", color=MAVI, fontsize=13, fontweight="bold")
ax.text(-1, -2.9, "g(x) < 0", color=KIRMIZI, fontsize=13, fontweight="bold", ha="center")
kaydet(fig, __file__)
