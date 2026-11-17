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

# Ders, bölüm 1: m(A) = 90°, |AB| = 5, |AC| = 12, |BC| = 13, α = m(C).
A, B, C = P(0, 0), P(0, 5), P(12, 0); G = (A + B + C) / 3
print("AB", uz(A, B), "AC", uz(A, C), "BC", uz(B, C), "A", olc(A, B, C))
fig, ax = sekil(6, 3.2); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B), color=KIRMIZI, lw=3); ax.plot(*zip(A, C), color=YESIL, lw=3); ax.plot(*zip(B, C), color=MAVI, lw=3)
dik(ax, A, B, C, s=0.55)
aci(ax, C, A, B, r=2.2, ad="α", renk=YAZI)
ad(ax, A, "A", G, d=0.7); ad(ax, B, "B", G, d=0.7); ad(ax, C, "C", G, d=0.7)
ax.text(-0.5, 2.5, "karşı\ndik kenar\n5", ha="right", va="center", color=KIRMIZI, fontsize=13)
ax.text(6, -0.6, "komşu dik kenar: 12", ha="center", va="top", color=YESIL, fontsize=13)
kenar(ax, B, C, "hipotenüs: 13", G, d=0.75, renk=MAVI)
ax.set_xlim(-3.3, 13.2); ax.set_ylim(-1.8, 6.2)
kaydet(fig, __file__)
