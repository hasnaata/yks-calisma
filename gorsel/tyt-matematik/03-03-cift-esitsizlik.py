import sys; sys.path.insert(0, "tools")
from cizim import *

# −3 < 2x + 1 ≤ 9  ⇒  −2 < x ≤ 4. Aralıktaki tam sayılar −1, 0, 1, 2, 3, 4 (6 tane).
LO, HI = -4, 6
fig, ax = sekil(6, 1.6)
sayi_dogrusu(ax, LO, HI)
ax.hlines(0, -2, 4, color=MAVI, lw=5, zorder=3)
ax.plot(-2, 0, "o", color=MAVI, markerfacecolor="white", markersize=11, mew=2.2, zorder=5)
ax.plot(4, 0, "o", color=MAVI, markerfacecolor=MAVI, markersize=11, mew=2.2, zorder=5)
for k in range(-1, 4):
    ax.plot(k, 0, "o", color=YESIL, markersize=7, zorder=6)
ax.plot(4, 0, "o", color=YESIL, markersize=7, zorder=6)
ax.text(1, 0.45, "6 tam sayı", ha="center", color=YESIL, fontsize=13, fontweight="bold")
kaydet(fig, __file__)
