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

# Alıştırma soru 6: m(B) = 45°, |AB| = 6√2, |BC| = 14. (Dikme ayağı H: |BH| = |AH| = 6, |HC| = 8, |AC| = 10.)
B, C, A = P(0, 0), P(14, 0), P(6, 6); G = (A + B + C) / 3
print("AB", uz(A, B), 6 * np.sqrt(2), "B", olc(B, A, C), "AC", uz(A, C))
fig, ax = sekil(5.4, 3.2); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
aci(ax, B, C, A, r=1.5, ad="45°", renk=MAVI)
ad(ax, A, "A", G, d=0.7); ad(ax, B, "B", G, d=0.7); ad(ax, C, "C", G, d=0.7)
kenar(ax, A, B, "6√2", G, d=0.8)
ax.annotate("", xy=(14, -1.2), xytext=(0, -1.2), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.1))
ax.text(7, -1.8, "14", ha="center", va="center", fontsize=13)
ax.set_xlim(-1.5, 15.5); ax.set_ylim(-2.4, 7.2)
kaydet(fig, __file__)
