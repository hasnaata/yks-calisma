import sys; sys.path.insert(0, "tools")
from cizim import *

# Dışbükey ABCDEF altıgeni. A'dan çıkan 3 köşegen (n − 3) mavi, kalan 6 köşegen gri kesikli: toplam 9 = 6·3/2.
P = {"A": (0.0, 3.2), "B": (-2.6, 2.0), "C": (-2.9, -0.6), "D": (-0.8, -2.3), "E": (2.4, -1.6), "F": (2.8, 1.3)}
ad = list(P); V = np.array([P[k] for k in ad])
# dışbükeylik denetimi
for i in range(6):
    a, b, c = V[i], V[(i + 1) % 6], V[(i + 2) % 6]
    d1, d2 = b - a, c - b; assert d1[0] * d2[1] - d1[1] * d2[0] > 0
fig, ax = sekil(5, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon(V, closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.4, alpha=1))
for i in range(6):
    for j in range(i + 2, 6):
        if i == 0 and j == 5: continue
        if i == 0:
            ax.plot(*zip(V[i], V[j]), color=MAVI, lw=2.6, zorder=3)
        else:
            ax.plot(*zip(V[i], V[j]), color=SOLUK, lw=1.3, ls="--", zorder=2)
O = V.mean(axis=0)
for k, v in zip(ad, V):
    u = (v - O) / np.linalg.norm(v - O)
    nokta(ax, *v, "", renk=YAZI)
    ax.text(*(v + 0.42 * u), k, ha="center", va="center", fontsize=14)
ax.set_xlim(-3.6, 3.6); ax.set_ylim(-2.9, 3.8)
kaydet(fig, __file__)
