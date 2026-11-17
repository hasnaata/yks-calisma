import sys; sys.path.insert(0, "tools")
from cizim import *

# f: [−4, 5] → R, f(x) = (x + 3)(x − 1)(x − 4)/10. Kökler −3, 1, 4. f(−4) = −4, f(5) = 3,2.
fig, ax = sekil(5.8, 4.2)
eksenler(ax, x=(-5.0, 6.2), y=(-4.8, 4.4))
ax.set_aspect(0.8)
ax.set_xticks([]); ax.set_yticks([])
xs = np.linspace(-4, 5, 400); ax.plot(xs, (xs + 3) * (xs - 1) * (xs - 4) / 10, color=MAVI)
nokta(ax, -4, -4, renk=MAVI); nokta(ax, 5, 3.2, renk=MAVI)
for r in (-3, 1, 4): nokta(ax, r, 0, renk=YAZI)
ax.text(-2.85, -0.3, "−3", ha="left", va="top", fontsize=13)
ax.text(0.85, -0.3, "1", ha="right", va="top", fontsize=13)
ax.text(4.15, -0.3, "4", ha="left", va="top", fontsize=13)
ax.plot([-4, -4], [0, -4], color=SOLUK, ls="--", lw=1); ax.text(-4, 0.3, "−4", ha="center", fontsize=13)
ax.plot([5, 5], [0, 3.2], color=SOLUK, ls="--", lw=1); ax.text(5, -0.3, "5", ha="center", va="top", fontsize=13)
ax.text(-2.4, 2.6, "y = f(x)", color=MAVI, fontsize=13)
kaydet(fig, __file__)
