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

# Ders, bölüm 3: m(A) = 90°, α = m(B), β = m(C), α + β = 90°.
A, B, C = P(0, 0), P(5, 0), P(0, 3); G = (A + B + C) / 3
print("A", olc(A, B, C), "B+C", olc(B, A, C) + olc(C, A, B))
fig, ax = sekil(5, 3.3); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
dik(ax, A, B, C, s=0.28)
aci(ax, B, A, C, r=0.9, ad="α", renk=MAVI); aci(ax, C, A, B, r=0.55, ad="β", renk=KIRMIZI)
ad(ax, A, "A", G, d=0.35); ad(ax, B, "B", G, d=0.35); ad(ax, C, "C", G, d=0.35)
kenar(ax, A, B, "c", G, d=0.3); kenar(ax, A, C, "b", G, d=0.3); kenar(ax, B, C, "a", G, d=0.35)
ax.set_xlim(-0.8, 5.8); ax.set_ylim(-0.7, 3.6)
kaydet(fig, __file__)
