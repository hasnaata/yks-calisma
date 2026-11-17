import sys; sys.path.insert(0, "tools")
from cizim import *

# f: [−3, 4] → R; x + 3 (−3 ≤ x < 1), 2 − x (1 ≤ x ≤ 4).
# Sol parça (−3, 0) dolu → (1, 4) boş. Sağ parça (1, 1) dolu → (4, −2) dolu. Görüntü [−2, 4).
fig, ax = sekil(5.6, 4.6)
eksenler(ax, x=(-4.4, 5.6), y=(-3.4, 5.4))
ax.set_aspect("equal")
ax.set_xticks([-3, -2, -1, 1, 2, 3, 4]); ax.set_xticklabels(["−3", "−2", "−1", "1", "2", "3", "4"])
ax.set_yticks([-2, -1, 1, 2, 3, 4]); ax.set_yticklabels(["−2", "−1", "1", "2", "3", "4"])
ax.axvline(1, color=SOLUK, ls=":", lw=1.2)
ax.plot([-3, 1], [0, 4], color=MAVI)
ax.plot([1, 4], [1, -2], color=YESIL)
nokta(ax, -3, 0, renk=MAVI)
nokta(ax, 1, 4, renk=MAVI, dolu=False)
nokta(ax, 1, 1, renk=YESIL)
nokta(ax, 4, -2, renk=YESIL)
ax.text(-3.6, 2.3, "y = x + 3", color=MAVI, fontsize=12)
ax.text(2.5, 0.2, "y = 2 − x", color=YESIL, fontsize=12)
ax.text(1.3, 4.25, "(1, 4) dahil değil", color=MAVI, fontsize=11)
ax.text(1.3, 1.25, "f(1) = 1", color=YESIL, fontsize=11)
kaydet(fig, __file__)
