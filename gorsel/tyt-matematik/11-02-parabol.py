import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = x², tanım kümesi [−2, 3]. f(−2) = 4, f(0) = 0, f(3) = 9. Görüntü kümesi [0, 9], [4, 9] değil.
fig, ax = sekil(5, 5)
eksenler(ax, x=(-3.2, 4.4), y=(-1.2, 10.6), izgara=False)
ax.set_xticks([-2, -1, 1, 2, 3]); ax.set_xticklabels(["−2", "−1", "1", "2", "3"])
ax.set_yticks([4, 9]); ax.set_yticklabels(["4", "9"])
xs = np.linspace(-3.0, 3.2, 100); ax.plot(xs, xs**2, color=CIZGI, lw=1.6)
xs = np.linspace(-2, 3, 100); ax.plot(xs, xs**2, color=MAVI, lw=2.6)
ax.plot([0.14, 0.14], [0, 9], color=YESIL, lw=6, solid_capstyle="butt", alpha=0.7)
nokta(ax, -2, 4, "f(−2) = 4", dx=-1.1, dy=0.55, renk=SARI)
nokta(ax, 3, 9, "f(3) = 9", dx=-1.95, dy=0.2, renk=SARI)
nokta(ax, 0, 0, renk=KIRMIZI)
ax.annotate("f(0) = 0", xy=(0.1, 0.1), xytext=(1.5, 0.7), color=KIRMIZI, fontsize=13,
            arrowprops=dict(arrowstyle="->", color=KIRMIZI, lw=1.2))
ax.plot([-2, 0], [4, 4], "--", color=SOLUK, lw=1); ax.plot([0, 3], [9, 9], "--", color=SOLUK, lw=1)
ax.text(1.0, 5.6, "görüntü\nkümesi\n[0, 9]", color=YESIL, fontsize=12, ha="left")
kaydet(fig, __file__)
