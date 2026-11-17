import sys; sys.path.insert(0, "tools")
from cizim import *

# |x − 3| < 5 (merkeze yakınlar, içerisi) ve |x − 3| > 5 (uzaklar, dışarısı).
fig, eks = plt.subplots(2, 1, figsize=(6, 3.4))
for ax, baslik, renk, ic in ((eks[0], "|x − 3| < 5", YESIL, True), (eks[1], "|x − 3| > 5", KIRMIZI, False)):
    sayi_dogrusu(ax, -4, 10, isaretler=[-2, 0, 3, 8])
    ax.set_ylim(-1, 1.1)
    if ic:
        ax.hlines(0, -2, 8, color=renk, lw=5, zorder=3)
    else:
        ax.annotate("", xy=(-4.5, 0), xytext=(-2, 0), arrowprops=dict(arrowstyle="-|>", color=renk, lw=5, mutation_scale=18), zorder=3)
        ax.annotate("", xy=(10.5, 0), xytext=(8, 0), arrowprops=dict(arrowstyle="-|>", color=renk, lw=5, mutation_scale=18), zorder=3)
    for x in (-2, 8):
        ax.plot(x, 0, "o", color=renk, markerfacecolor="white", markersize=11, mew=2.2, zorder=5)
    ax.plot(3, 0, "o", color=SARI, markersize=7, zorder=6)
    ax.text(-4.5, 0.7, baslik, va="center", fontsize=15, color=renk, fontweight="bold")
    ax.text(10.5, 0.7, "−2 < x < 8" if ic else "x < −2 veya x > 8", va="center", ha="right", fontsize=13, color=YAZI)
kaydet(fig, __file__)
