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

# Alıştırma soru 12: direk |AH| = 12, |AB| = 15 (|BH| = 9), tan(ACH) = 3/4 (|HC| = 16, |AC| = 20), |BC| = 25.
B, H, C, A = P(-9, 0), P(0, 0), P(16, 0), P(0, 12); G = (A + B + C) / 3
print("AB", uz(A, B), "AC", uz(A, C), "tanC", uz(A, H) / uz(H, C), "BC", uz(B, C))
fig, ax = sekil(6, 3.4); ax.set_aspect("equal"); ax.axis("off")
ax.plot([-10.5, 17.5], [0, 0], color=SOLUK, lw=1.4)
ax.plot(*zip(H, A), color=YAZI, lw=4)
ax.plot(*zip(A, B), color=MAVI, lw=1.8); ax.plot(*zip(A, C), color=MAVI, lw=1.8)
dik(ax, H, A, C, s=1.0)
aci(ax, C, H, A, r=3.0, ad="", renk=KIRMIZI)
ax.text(C[0] - 4.6, 0.9, "θ", color=KIRMIZI, fontsize=13, ha="center", va="center")
ad(ax, A, "A", G, d=1.2)
for K, m in ((B, "B"), (C, "C")):
    ax.plot(*K, "o", color=YAZI, markersize=5, zorder=5); ax.text(K[0], -1.3, m, ha="center", va="center")
ax.text(H[0], -1.3, "H", ha="center", va="center")
kenar(ax, A, B, "15", G, d=1.2)
ax.text(0.6, 6, "12", ha="left", va="center", fontsize=13)
ax.set_xlim(-11, 18); ax.set_ylim(-2.2, 13.5)
kaydet(fig, __file__)
