import sys; sys.path.insert(0, "tools")
from cizim import *

# A = {1, 2, 4}, B = {1, 3}: A×B grafiği, 3 · 2 = 6 nokta.
fig, ax = sekil(5, 3.8)
eksenler(ax, x=(-0.3, 5.3), y=(-0.3, 3.9), izgara=False)
ax.set_xticks([1, 2, 3, 4]); ax.set_yticks([1, 2, 3])
A, B = [1, 2, 4], [1, 3]
for a in A: ax.plot([a, a], [0, 3.6], ls="--", color=MAVI, lw=1.2)
for b in B: ax.plot([0, 4.6], [b, b], ls="--", color=YESIL, lw=1.2)
for a in A:
    for b in B:
        nokta(ax, a, b, f"({a}, {b})", dx=0.08, dy=0.18, renk=KIRMIZI)
for a in A: ax.plot(a, 0, "s", color=MAVI, markersize=7, clip_on=False, zorder=6)
for b in B: ax.plot(0, b, "s", color=YESIL, markersize=7, clip_on=False, zorder=6)
kaydet(fig, __file__)
