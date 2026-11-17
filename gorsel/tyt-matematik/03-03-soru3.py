import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 3: 2 dahil, sola doğru sonsuza giden küme (x ≤ 2).
LO, HI = -3, 5
fig, ax = sekil(6, 1.3)
sayi_dogrusu(ax, LO, HI)
ax.hlines(0, LO - 0.2, 2, color=MAVI, lw=5, zorder=3)
ax.annotate("", xy=(LO - 0.6, 0), xytext=(LO - 0.1, 0), arrowprops=dict(arrowstyle="-|>,head_width=0.35,head_length=0.6", color=MAVI, lw=3), zorder=4)
ax.plot(2, 0, "o", color=MAVI, markerfacecolor=MAVI, markersize=11, mew=2.2, zorder=5)
kaydet(fig, __file__)
