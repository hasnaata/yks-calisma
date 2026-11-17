import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = x + 2 (x < 1), 5 − x (x ≥ 1). x = 1'de: sol parça (1, 3) boş, sağ parça (1, 4) dolu.
# y = 3 doğrusu grafiği yalnızca x = 2'de keser; (1, 3) boş nokta sayılmaz.
fig, ax = sekil(5.6, 4.4)
eksenler(ax, x=(-3.6, 6.4), y=(-1.6, 5.6))
ax.set_aspect("equal")
ax.set_xticks([-3, -2, -1, 1, 2, 3, 4, 5, 6]); ax.set_xticklabels(["−3", "−2", "−1", "1", "2", "3", "4", "5", "6"])
ax.set_yticks([-1, 1, 2, 3, 4, 5]); ax.set_yticklabels(["−1", "1", "2", "3", "4", "5"])
ax.axhline(3, color=SARI, ls="--", lw=1.4)
ax.text(6.3, 3.15, "y = 3", color=SARI, ha="right", va="bottom", fontsize=12)
xs = np.linspace(-3.5, 1, 20); ax.plot(xs, xs + 2, color=MAVI)
xs = np.linspace(1, 6.3, 20); ax.plot(xs, 5 - xs, color=YESIL)
nokta(ax, 1, 3, renk=MAVI, dolu=False)
nokta(ax, 1, 4, renk=YESIL)
nokta(ax, 2, 3, renk=KIRMIZI)
ax.text(-3.5, 1.5, "y = x + 2", color=MAVI, fontsize=12)
ax.text(2.4, 4.3, "y = 5 − x", color=YESIL, fontsize=12)
ax.text(0.85, 4.15, "f(1) = 4", color=YESIL, fontsize=12, ha="right")
ax.text(1.9, 2.8, "x = 2", color=KIRMIZI, fontsize=12, va="top", ha="right")
kaydet(fig, __file__)
