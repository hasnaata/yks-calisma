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

# Alıştırma soru 7: m(BAC) = 90°, [AH] ⊥ [BC], |BH| = 4, |HC| = 9 (|AH| = 6).
B, H, C, A = P(0, 0), P(4, 0), P(13, 0), P(4, 6); G = (A + B + C) / 3
print("A", olc(A, B, C), "AH", uz(A, H))
fig, ax = sekil(5.4, 3.2); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI); ax.plot(*zip(A, H), color=KIRMIZI, lw=1.8)
dik(ax, A, B, C, s=0.6); dik(ax, H, A, C, s=0.5)
ad(ax, A, "A", G, d=0.7); ad(ax, B, "B", G, d=0.7); ad(ax, C, "C", G, d=0.7)
ax.plot(*H, "o", color=KIRMIZI, markersize=5); ax.text(H[0], -0.6, "H", ha="center", va="center", color=KIRMIZI)
for x0, x1, m in ((0, 4, "4"), (4, 13, "9")):
    ax.annotate("", xy=(x1, -1.4), xytext=(x0, -1.4), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.1))
    ax.text((x0 + x1) / 2, -2.0, m, ha="center", va="center", fontsize=13)
ax.set_xlim(-1.3, 14.3); ax.set_ylim(-2.5, 7.2)
kaydet(fig, __file__)
