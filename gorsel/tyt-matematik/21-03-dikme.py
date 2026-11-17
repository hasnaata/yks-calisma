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

# Ders, bölüm 5: |AB| = |AC| = 10, |BC| = 12, |BD| = 2, α = m(ADC). H, BC'nin orta noktası; |AH| = 8, |DH| = 4.
B, C, A, D, H = P(0, 0), P(12, 0), P(6, 8), P(2, 0), P(6, 0); G = (A + B + C) / 3
print("AB", uz(A, B), "AC", uz(A, C), "AH", uz(A, H), "DH", uz(D, H), "H", olc(H, A, C), "tan", uz(A, H) / uz(D, H))
fig, ax = sekil(5.4, 4.2); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, D, H], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.plot(*zip(A, B, C, A), color=YAZI); ax.plot(*zip(A, D), color=MAVI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.8, ls="--"); dik(ax, H, A, C, s=0.55)
aci(ax, D, C, A, r=0.9, ad="α", renk=MAVI)
ad(ax, A, "A", G, d=0.6); ad(ax, B, "B", G, d=0.6); ad(ax, C, "C", G, d=0.6)
ax.plot(*D, "o", color=MAVI, markersize=5); ax.text(D[0], -0.7, "D", ha="center", va="center", color=MAVI)
ax.plot(*H, "o", color=KIRMIZI, markersize=5); ax.text(H[0], -0.7, "H", ha="center", va="center", color=KIRMIZI)
kenar(ax, A, B, "10", G, d=0.55); kenar(ax, A, C, "10", G, d=0.55)
for x0, x1, m in ((0, 2, "2"), (2, 6, "4"), (6, 12, "6")):
    ax.annotate("", xy=(x1, -1.6), xytext=(x0, -1.6), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.1))
    ax.text((x0 + x1) / 2, -2.15, m, ha="center", va="center", fontsize=13)
ax.text(6.3, 4.6, "8", ha="left", va="center", color=KIRMIZI, fontsize=13)
ax.set_xlim(-1.0, 13.0); ax.set_ylim(-2.6, 9.0)
kaydet(fig, __file__)
