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

# Alıştırma soru 10: kareli kâğıt, birim kare kenarı 1. A(0,0), B(6,0), C(2,3).
A, B, C = P(0, 0), P(6, 0), P(2, 3); G = (A + B + C) / 3
print("tanA", 3 / 2, "tanB", 3 / 4, "B açısı", olc(B, A, C), np.degrees(np.arctan(0.75)))
fig, ax = sekil(5, 3); ax.set_aspect("equal"); ax.axis("off")
for x in range(0, 7): ax.plot([x, x], [-0.0, 4], color=CIZGI, lw=0.8)
for y in range(0, 5): ax.plot([0, 6], [y, y], color=CIZGI, lw=0.8)
ax.plot(*zip(A, B, C, A), color=MAVI, lw=2.4)
ad(ax, A, "A", G, d=0.45, renk=MAVI); ad(ax, B, "B", G, d=0.45, renk=MAVI); ad(ax, C, "C", G, d=0.45, renk=MAVI)
ax.set_xlim(-0.6, 6.6); ax.set_ylim(-0.6, 4.2)
kaydet(fig, __file__)
