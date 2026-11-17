import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 10. f: [−3, 4] -> R, köşeler (−3, 0), (−1, 3), (2, 0), (4, 2).
# (f∘f)(x) = 0  =>  f(x) ∈ {−3, 2}  =>  f(x) = 2  =>  x = −5/3, 0, 4  (3 çözüm).
fig, ax = sekil(5.6, 3.8)
eksenler(ax, x=(-3.8, 4.8), y=(-1.2, 3.8))
ax.set_aspect("equal")
ax.set_xticks(range(-3, 5)); ax.set_xticklabels(["−3", "", "−1", "", "", "2", "", "4"])
ax.set_yticks(range(-1, 4)); ax.set_yticklabels(["", "", "", "2", "3"])
xs, ys = [-3, -1, 2, 4], [0, 3, 0, 2]
ax.plot(xs, ys, color=MAVI)
for p in zip(xs, ys): nokta(ax, *p, renk=MAVI)
ax.plot([-1, -1], [0, 3], color=SOLUK, lw=1, ls="--")
ax.plot([4, 4], [0, 2], color=SOLUK, lw=1, ls="--")
for t in ax.get_yticklabels(): t.set_bbox(dict(facecolor="white", edgecolor="none", pad=0.5))
ax.text(-2.75, 1.9, "f", color=MAVI, fontsize=15, fontweight="bold")
kaydet(fig, __file__)
