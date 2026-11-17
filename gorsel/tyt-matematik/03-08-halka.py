import sys; sys.path.insert(0, "tools")
from cizim import *

# 2 ≤ |x − 1| < 5: merkezden (1) uzaklığı 2 ile 5 arası; iki ayrı parça.
fig, ax = sekil(6, 1.9)
sayi_dogrusu(ax, -5, 7, isaretler=[-4, -1, 1, 3, 6])
ax.set_ylim(-0.9, 1.2)
for a, ad_, b, bd in ((-4, False, -1, True), (3, True, 6, False)):
    ax.hlines(0, a, b, color=MAVI, lw=5, zorder=3)
    for x, dolu in ((a, ad_), (b, bd)):
        ax.plot(x, 0, "o", color=MAVI, markerfacecolor=MAVI if dolu else "white", markersize=11, mew=2.2, zorder=5)
ax.plot(1, 0, "o", color=SARI, markersize=8, zorder=5)
ax.text(1, 0.55, "merkez", ha="center", color=SARI, fontsize=12)
ax.text(-2.5, 0.55, "sol parça", ha="center", color=MAVI, fontsize=12)
ax.text(4.5, 0.55, "sağ parça", ha="center", color=MAVI, fontsize=12)
kaydet(fig, __file__)
