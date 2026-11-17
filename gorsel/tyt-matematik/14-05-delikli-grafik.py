import sys; sys.path.insert(0, "tools")
from cizim import *

# y = (x² − 4)/(x − 2) grafiği: y = x + 2 doğrusu, ama x = 2'de boşluk (4 değeri alınmaz).
fig, ax = sekil(5.2, 4.6)
eksenler(ax, x=(-4.5, 4.5), y=(-2.5, 7.5))
ax.set_xticks([-4, -2, 2, 4]); ax.set_yticks([4, 6])
ax.set_xticklabels(["−4", "−2", "2", "4"]); ax.set_yticklabels(["4", "6"])
xs = np.linspace(-4.4, 4.4, 400)
ax.plot(xs, xs + 2, color=MAVI)
nokta(ax, 2, 4, dolu=False, renk=MAVI)
ax.plot([2, 2], [0, 3.8], color=SOLUK, lw=1, ls="--")
ax.plot([0, 1.85], [4, 4], color=SOLUK, lw=1, ls="--")
ax.text(2.35, 3.3, "x = 2 için\ntanımsız", fontsize=12, color=KIRMIZI, va="top")
ax.text(-4.3, 6.6, r"$y = \dfrac{x^2 - 4}{x - 2}$", fontsize=15, color=MAVI)
kaydet(fig, __file__)
