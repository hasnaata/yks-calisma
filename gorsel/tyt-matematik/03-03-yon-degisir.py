import sys; sys.path.insert(0, "tools")
from cizim import *

# 2 < 5 iken iki taraf −1 ile çarpılınca −2 > −5 olur: sayılar 0'a göre aynalanır, sıra tersine döner.
LO, HI = -6, 6
fig, ax = sekil(6, 2.6)
sayi_dogrusu(ax, LO, HI)
ax.set_ylim(-1, 1.6)
for v, renk in ((2, MAVI), (5, MAVI), (-2, KIRMIZI), (-5, KIRMIZI)):
    ax.plot(v, 0, "o", color=renk, markersize=10, zorder=5)
for v in (2, 5):
    ax.annotate("", xy=(-v, 0.12), xytext=(v, 0.12),
                arrowprops=dict(arrowstyle="-|>", color=SOLUK, lw=1.4, connectionstyle="arc3,rad=0.45" if v == 2 else "arc3,rad=0.32"))
ax.text(3.5, -0.75, "2 < 5", ha="center", color=MAVI, fontsize=14, fontweight="bold")
ax.text(-3.5, -0.75, "−2 > −5", ha="center", color=KIRMIZI, fontsize=14, fontweight="bold")
ax.text(0, 1.38, "· (−1)", ha="center", color=YAZI, fontsize=14)
kaydet(fig, __file__)
