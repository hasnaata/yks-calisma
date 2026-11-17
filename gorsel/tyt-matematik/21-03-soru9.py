import sys; sys.path.insert(0, "tools")
from cizim import *

def P(x, y): return np.array([x, y], float)
def uz(A, B): return float(np.linalg.norm(A - B))
def olc(K, A, B):
    u, v = A - K, B - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)
def kenar(ax, A, B, metin, G, d=0.4, renk=YAZI, fs=13):
    """[AB] kenarının ortasına, G noktasından uzak tarafa etiket."""
    M = (A + B) / 2; t = (B - A) / uz(A, B); n = np.array([-t[1], t[0]])
    if np.dot(n, M - G) < 0: n = -n
    ax.text(*(M + d * n), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik(ax, K, A, B, s=0.3):
    """K köşesinde dik açı işareti."""
    u = (A - K) / uz(A, K) * s; v = (B - K) / uz(B, K) * s
    ax.plot(*zip(K + u, K + u + v, K + v), color=SOLUK, lw=1.3)
def ad(ax, K, metin, G, d=0.4, renk=YAZI):
    """Köşe adını G'den uzak tarafa yazar."""
    n = (K - G) / uz(K, G); ax.plot(*K, "o", color=renk, markersize=5, zorder=5)
    ax.text(*(K + d * n), metin, ha="center", va="center", color=renk, fontsize=13)

# Alıştırma soru 9: el yüksekliği 1,5 m, ip 50 m, tan α = 3/4 (yatay 40 m, düşey 30 m), uçurtma yerden 31,5 m yukarıda.
E, U = P(0, 1.5), P(40, 31.5); Y = P(40, 1.5)
print("ip", uz(E, U), "tan", (U[1] - E[1]) / (U[0] - E[0]), "yükseklik", U[1])
fig, ax = sekil(5.6, 4.4); ax.set_aspect("equal"); ax.axis("off")
ax.plot([-4, 46], [0, 0], color=SOLUK, lw=1.4)
ax.plot([0, 0], [0, 1.5], color=YAZI, lw=4)
ax.plot(*zip(E, U), color=MAVI, lw=1.6)
ax.plot(*zip(E, Y), color=SOLUK, lw=1.2, ls="--")
k = 1.6; ax.add_patch(patches.Polygon([U + [0, k * 1.5], U + [k, 0], U + [0, -k * 1.5], U + [-k, 0]], closed=True, facecolor=KIRMIZI_ACIK, edgecolor=KIRMIZI, lw=1.6))
aci(ax, E, Y, U, r=7, ad="α", renk=KIRMIZI)
M = (E + U) / 2 + 3.2 * P(-0.6, 0.8); ax.text(*M, "50 m", ha="center", va="center", color=MAVI, fontsize=13)
ax.text(-1.2, 1.0, "1,5 m", ha="right", va="center", fontsize=12)
ax.text(42.5, U[1], "uçurtma", ha="left", va="center", fontsize=12, color=KIRMIZI)
ax.set_xlim(-8, 52); ax.set_ylim(-4, 35)
kaydet(fig, __file__)
