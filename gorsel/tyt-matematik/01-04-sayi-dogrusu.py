import sys; sys.path.insert(0, "tools")
from cizim import *

# Sayı doğrusunda negatifler solda, pozitifler sağda; sıfır ikisi de değil. Sağdaki sayı her zaman büyüktür.
fig, ax = sekil(6, 2.3)
sayi_dogrusu(ax, -5, 5)
ax.set_ylim(-1.0, 1.45)
ax.hlines(0, -5.45, -0.12, color=KIRMIZI, lw=5, zorder=3)
ax.hlines(0, 0.12, 5.45, color=YESIL, lw=5, zorder=3)
ax.plot(0, 0, "o", color=YAZI, markerfacecolor="white", markersize=10, mew=2, zorder=5)
ax.text(-2.75, 0.42, "Negatif sayılar", ha="center", color=KIRMIZI, fontsize=14)
ax.text(2.75, 0.42, "Pozitif sayılar", ha="center", color=YESIL, fontsize=14)
ax.text(0, 1.05, "0: ne pozitif\nne negatif", ha="center", va="center", color=YAZI, fontsize=11)
ax.annotate("", xy=(4.6, -0.82), xytext=(1.4, -0.82), arrowprops=dict(arrowstyle="-|>", color=MAVI, lw=1.8))
ax.text(1.2, -0.82, "sağa gittikçe büyür", ha="right", va="center", color=MAVI, fontsize=12)
kaydet(fig, __file__)
