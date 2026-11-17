import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 11: x ≤ −3 veya x ≥ 5 (|x − 1| ≥ 4 çözüm kümesi).
fig, ax = sekil(6, 1.3)
sayi_dogrusu(ax, -6, 8, isaretler=[-3, 0, 5])
ax.set_ylim(-0.9, 0.6)
ax.annotate("", xy=(-6.5, 0), xytext=(-3, 0), arrowprops=dict(arrowstyle="-|>", color=MAVI, lw=5, mutation_scale=18), zorder=3)
ax.annotate("", xy=(8.5, 0), xytext=(5, 0), arrowprops=dict(arrowstyle="-|>", color=MAVI, lw=5, mutation_scale=18), zorder=3)
for x in (-3, 5):
    ax.plot(x, 0, "o", color=MAVI, markersize=11, zorder=5)
kaydet(fig, __file__)
