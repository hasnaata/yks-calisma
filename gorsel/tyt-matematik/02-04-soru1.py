import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 1: K = 252 sayısının bölme merdiveni; K, L, M, N harflerle gizli.
fig, ax = sekil(3.4, 3.2)
ax.axis("off")
satirlar = [("K", "2"), ("L", "2"), ("63", "3"), ("21", "M"), ("7", "N"), ("1", None)]
for i, (n, p) in enumerate(satirlar):
    y = -i
    harf = n.isalpha()
    ax.text(1.6, y, n, ha="right", va="center", fontsize=15, color=MAVI if harf else YAZI,
            fontweight="bold" if harf else "normal")
    if p:
        ax.text(2.0, y, p, ha="left", va="center", fontsize=15, color=MAVI if p.isalpha() else YAZI,
                fontweight="bold" if p.isalpha() else "normal")
        ax.plot([1.8, 2.6], [y - 0.5, y - 0.5], color=CIZGI, lw=1)
ax.plot([1.8, 1.8], [0.5, -4.5], color=SOLUK, lw=1.6)
ax.set_xlim(0.9, 2.9); ax.set_ylim(-5.5, 0.6)
kaydet(fig, __file__)
