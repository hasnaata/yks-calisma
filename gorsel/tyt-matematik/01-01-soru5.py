import sys; sys.path.insert(0, "tools")
from cizim import *

# Soru 5: K, L, M, N, P noktaları. √11 ≈ 3,32 → N; P = 3,8 (3,5'in sağında).
fig, ax = sekil(6.2, 1.7)
sayi_dogrusu(ax, -4, 4)
for x, ad in ((-np.sqrt(11), "K"), (1.7, "L"), (2.75, "M"), (np.sqrt(11), "N"), (3.8, "P")):
    ax.plot(x, 0, "o", color=MAVI, markersize=8, zorder=5)
    ax.text(x, 0.22, ad, ha="center", va="bottom", color=MAVI, fontsize=14, fontweight="bold")
ax.set_ylim(-0.75, 0.75)
kaydet(fig, __file__)
