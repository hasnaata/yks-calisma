import sys; sys.path.insert(0, "tools")
from cizim import *

fig, eks = plt.subplots(1, 3, figsize=(6.4, 3.3))
veriler = [("x² − 2x − 3", -3, [-1, 3], "Δ = 16 > 0", "Ç = {−1, 3}", YESIL),
           ("x² − 2x + 1", 1, [1], "Δ = 0", "Ç = {1}", SARI),
           ("x² − 2x + 5", 5, [], "Δ = −16 < 0", "Ç = ∅", KIRMIZI)]
for ax, (baslik, c, kokler, delta, cozum, renk) in zip(eks, veriler):
    ax.axis("off"); ax.set_xlim(-2.2, 4.2); ax.set_ylim(-7.5, 10.5)
    ax.annotate("", xy=(4.1, 0), xytext=(-2.1, 0), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.2))
    xs = np.linspace(-1.9, 3.9, 200)
    ys = xs**2 - 2*xs + c; ys = np.where(ys > 8.2, np.nan, ys)
    ax.plot(xs, ys, color=MAVI)
    for k in kokler: nokta(ax, k, 0, renk=renk)
    ax.text(1, 10.4, baslik, ha="center", va="top", fontsize=12)
    ax.text(1, -5.0, delta, ha="center", va="center", fontsize=12, color=renk)
    ax.text(1, -7.3, cozum, ha="center", va="center", fontsize=12, color=renk)
plt.subplots_adjust(wspace=0.12)
kaydet(fig, __file__)
