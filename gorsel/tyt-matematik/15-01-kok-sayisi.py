import sys; sys.path.insert(0, "tools")
from cizim import *

fig, eks = plt.subplots(1, 3, figsize=(6.4, 2.9))
veriler = [("x² − 4 = 0", lambda x: x**2 - 4, [-2, 2], "Ç = {−2, 2}"),
           ("x² = 0", lambda x: x**2, [0], "Ç = {0}"),
           ("x² + 1 = 0", lambda x: x**2 + 1, [], "Ç = ∅")]
for ax, (baslik, f, kokler, cozum) in zip(eks, veriler):
    ax.axis("off"); ax.set_xlim(-3.2, 3.2); ax.set_ylim(-5.5, 7.5)
    ax.annotate("", xy=(3.1, 0), xytext=(-3.1, 0), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.2))
    xs = np.linspace(-2.9, 2.9, 200)
    ys = f(xs); ys = np.where(ys > 6.3, np.nan, ys)
    ax.plot(xs, ys, color=MAVI)
    for k in kokler: nokta(ax, k, 0, renk=KIRMIZI)
    ax.text(0, 7.4, baslik, ha="center", va="top", fontsize=12)
    ax.text(0, -5.4, cozum, ha="center", va="bottom", fontsize=12, color=KIRMIZI)
plt.subplots_adjust(wspace=0.15)
kaydet(fig, __file__)
