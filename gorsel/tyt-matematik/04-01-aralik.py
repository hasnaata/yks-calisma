import sys; sys.path.insert(0, "tools")
from cizim import *

# 2^x = 50, 3^y = 50, 7^z = 50: her bilinmeyen iki ardışık tam sayı arasında.
fig, ax = sekil(6, 2.8)
sayi_dogrusu(ax, 0, 7)
ax.set_ylim(-1, 1.6)
for (a, b), ad, renk, y in (((2, 3), "z", SARI, 0.45), ((3, 4), "y", YESIL, 1.05), ((5, 6), "x", MAVI, 0.45)):
    for t in (a, b):
        ax.plot([t, t], [0, y], color=renk, lw=1, ls=":", zorder=2)
    ax.hlines(y, a, b, color=renk, lw=6, zorder=3)
    for t in (a, b):
        ax.plot(t, y, "o", color=renk, markerfacecolor="white", markersize=10, mew=2, zorder=5)
    ax.text((a + b) / 2, y + 0.3, ad, ha="center", va="center", fontsize=17, color=renk, fontweight="bold")
kaydet(fig, __file__)
