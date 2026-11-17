import sys; sys.path.insert(0, "tools")
from cizim import *

# Kendini dene Soru 3: üstte y = x + 1 (kesikli), altta y = x − 2 (düz); aradaki şerit boyalı.
X, Y = (-4, 5), (-4.5, 5)
fig, ax = sekil(4.8, 4.8)
eksenler(ax, x=X, y=Y)
ax.set_xticks(range(-3, 5)); ax.set_yticks(range(-4, 5))
ax.set_xticklabels([]); ax.set_yticklabels([])
ax.tick_params(length=0)
# Yalnızca eksenleri kestikleri noktalar yazılır.
for x, y, t in [(-1, 0, "−1"), (2, 0, "2"), (0, 1, "1"), (0, -2, "−2")]:
    nokta(ax, x, y, "", renk=MAVI, dolu=(t in ("2", "−2")))
ax.text(-1.15, 0.3, "−1", ha="right", fontsize=13)
ax.text(2.2, -0.55, "2", fontsize=13)
ax.text(-0.25, 1.15, "1", ha="right", fontsize=13)
ax.text(-0.25, -2.0, "−2", ha="right", va="center", fontsize=13)
xs = np.linspace(X[0], X[1], 200)
ust, alt = xs + 1, xs - 2
ax.fill_between(xs, np.clip(alt, Y[0], Y[1]), np.clip(ust, Y[0], Y[1]), color=MAVI_ACIK, zorder=0.2)
ax.plot(xs, ust, color=MAVI, ls=(0, (6, 4)), zorder=3)
ax.plot(xs, alt, color=MAVI, zorder=3)
ax.set_ylim(*Y)
kaydet(fig, __file__)
