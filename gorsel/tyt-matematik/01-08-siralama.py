import sys; sys.path.insert(0, "tools")
from cizim import *

# 0,30 ile 0,35 arası büyütülmüş sayı doğrusu: 0,3 < 0,33 < 0,3(3) < 0,(34) < 0,3(4).
fig, ax = sekil(6.2, 2.6)
a, b = 0.30, 0.35
ax.set_xlim(a - 0.003, b + 0.003); ax.set_ylim(-1.1, 1.6); ax.axis("off")
ax.annotate("", xy=(b + 0.0028, 0), xytext=(a - 0.0028, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
for t in [0.30, 0.31, 0.32, 0.33, 0.34, 0.35]:
    ax.plot([t, t], [-0.08, 0.08], color=SOLUK, lw=1.2)
    ax.text(t, -0.3, f"{t:.2f}".replace(".", ","), ha="center", va="top", color=SOLUK, fontsize=11)
# (değer, etiket, yükseklik, renk); devreden kısım etiket içinde mathtext ile üstü çizgili
N = [(0.30, r"$0{,}3$", 0.5, YAZI), (0.33, r"$0{,}33$", 0.5, YAZI), (1 / 3, r"$0{,}\overline{3}$", 1.15, MAVI),
     (34 / 99, r"$0{,}\overline{34}$", 0.5, MAVI), (0.3 + 4 / 90, r"$0{,}3\overline{4}$", 1.15, KIRMIZI)]
for x, ad, y, r in N:
    ax.plot(x, 0, "o", color=r, markersize=8, zorder=5)
    ax.plot([x, x], [0.1, y - 0.05], color=r, lw=1, zorder=4)
    ax.text(x, y, ad, ha="center", va="bottom", color=r, fontsize=15)
kaydet(fig, __file__)
