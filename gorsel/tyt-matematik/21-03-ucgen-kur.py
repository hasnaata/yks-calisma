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

# Ders, bölüm 2: tan α = 3/4. Dik kenarlar 3k ve 4k, hipotenüs 5k (burada k = 1 birim çizildi).
B, C, A = P(0, 0), P(4, 0), P(0, 3); G = (A + B + C) / 3
print("AB", uz(A, B), "BC", uz(B, C), "AC", uz(A, C), "B", olc(B, A, C))
fig, ax = sekil(4.6, 3.4); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B), color=KIRMIZI, lw=2.6); ax.plot(*zip(B, C), color=YESIL, lw=2.6); ax.plot(*zip(A, C), color=MAVI, lw=2.6)
dik(ax, B, A, C, s=0.25)
aci(ax, C, B, A, r=0.75, ad="α", renk=YAZI)
ad(ax, A, "A", G, d=0.3); ad(ax, B, "B", G, d=0.3); ad(ax, C, "C", G, d=0.3)
kenar(ax, A, B, "3k", G, d=0.35, renk=KIRMIZI); kenar(ax, B, C, "4k", G, d=0.3, renk=YESIL)
kenar(ax, A, C, "5k", G, d=0.35, renk=MAVI)
ax.set_xlim(-0.8, 4.6); ax.set_ylim(-0.7, 3.5)
kaydet(fig, __file__)
