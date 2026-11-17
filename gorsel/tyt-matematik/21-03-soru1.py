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

# Alıştırma soru 1: m(B) = 90°, |AB| = 8, |BC| = 15 (|AC| = 17), α = m(ACB).
B, C, A = P(0, 0), P(15, 0), P(0, 8); G = (A + B + C) / 3
print("AC", uz(A, C), "B", olc(B, A, C))
fig, ax = sekil(5.6, 3.4); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI); dik(ax, B, A, C, s=0.7)
aci(ax, C, B, A, r=2.6, ad="α", renk=MAVI)
ad(ax, A, "A", G, d=0.9); ad(ax, B, "B", G, d=0.9); ad(ax, C, "C", G, d=0.9)
kenar(ax, A, B, "8", G, d=0.8); kenar(ax, B, C, "15", G, d=0.8)
ax.set_xlim(-2, 16.5); ax.set_ylim(-2, 9.2)
kaydet(fig, __file__)
