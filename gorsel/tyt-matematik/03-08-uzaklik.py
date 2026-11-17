import sys; sys.path.insert(0, "tools")
from cizim import *

# |x − 3| = 5: 3'e uzaklığı 5 olan iki nokta (−2 ve 8).
fig, ax = sekil(6, 1.9)
sayi_dogrusu(ax, -4, 10, isaretler=[-2, 0, 3, 8])
ax.set_ylim(-0.9, 1.25)
ax.plot(3, 0, "o", color=SARI, markersize=9, zorder=5)
for x in (-2, 8):
    ax.plot(x, 0, "o", color=MAVI, markersize=11, zorder=5)
for a, b in ((3, -2), (3, 8)):
    ax.annotate("", xy=(b, 0.42), xytext=(a, 0.42), arrowprops=dict(arrowstyle="->", color=MAVI, lw=1.8))
    ax.text((a + b) / 2, 0.62, "5 birim", ha="center", va="bottom", color=MAVI, fontsize=13)
ax.text(3, -0.75, "merkez", ha="center", va="top", color=SARI, fontsize=11)
kaydet(fig, __file__)
