import sys; sys.path.insert(0, "tools")
from cizim import *

# f: [−3, 5] → R. (−3, 2) dolu → (−1, −2) → (2, 4) boş; x = 2'de (2, 1) dolu, (2, 1) → (5, 1) sabit.
# Görüntü kümesi [−2, 4): tam sayılar −2, −1, 0, 1, 2, 3 (6 tane).
fig, ax = sekil(5.6, 4.6)
eksenler(ax, x=(-4.4, 6.4), y=(-3.2, 5.2))
ax.set_aspect("equal")
ax.set_xticks([-3, -2, -1, 1, 2, 3, 4, 5]); ax.set_xticklabels(["−3", "", "−1", "", "2", "", "", "5"])
ax.set_yticks([-2, -1, 1, 2, 3, 4]); ax.set_yticklabels(["", "", "1", "2", "", "4"])
ax.text(0.2, -2.15, "−2", color=SOLUK, fontsize=13, va="top")
ax.plot([-3, -1, 2], [2, -2, 4], color=MAVI)
ax.plot([2, 5], [1, 1], color=MAVI)
nokta(ax, -3, 2, renk=MAVI)
nokta(ax, 2, 4, renk=MAVI, dolu=False)
nokta(ax, 2, 1, renk=MAVI)
nokta(ax, 5, 1, renk=MAVI)
ax.plot([0, -1], [-2, -2], color=SOLUK, ls="--", lw=1)
ax.plot([0, 2], [4, 4], color=SOLUK, ls="--", lw=1)
ax.plot([2, 2], [0, 4], color=SOLUK, ls=":", lw=1)
ax.text(3.2, 1.35, "y = f(x)", color=MAVI, fontsize=13)
kaydet(fig, __file__)
