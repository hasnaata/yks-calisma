import sys; sys.path.insert(0, "tools")
from cizim import *

# Çift fonksiyon: f(x) = x² − 3. f(−2) = f(2) = 1; grafik y eksenine göre simetrik.
fig, ax = sekil(5, 3.8)
eksenler(ax, (-3.6, 3.6), (-3.6, 4.6))
ax.set_xticks([-2, 2]); ax.set_xticklabels(["−2", "2"])
ax.set_yticks([1]); ax.set_yticklabels([""])
x = np.linspace(-2.75, 2.75, 200)
ax.plot(x, x**2 - 3, color=MAVI)
ax.plot([-2, 2], [1, 1], "--", color=YESIL, lw=1.5)
ax.plot([0, 0], [-3.6, 4.6], color=YESIL, lw=2.6, alpha=0.35)
nokta(ax, -2, 1, "(−2, 1)", dx=-1.5, dy=0.3, renk=MAVI)
nokta(ax, 2, 1, "(2, 1)", dx=0.2, dy=0.3, renk=MAVI)
ax.text(1.75, 3.6, "y = x² − 3", color=MAVI, fontsize=12, ha="right")
ax.text(0.2, -3.3, "ayna: y ekseni", color=YESIL, fontsize=11)
kaydet(fig, __file__)
