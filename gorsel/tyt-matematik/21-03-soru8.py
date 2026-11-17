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

# Alıştırma soru 8: rampa uzunluğu 3,7 m, yükseklik 1,2 m (yatay 3,5 m), α rampanın yerle açısı.
O, Y, T = P(0, 0), P(3.5, 0), P(3.5, 1.2); G = (O + Y + T) / 3
print("rampa", uz(O, T), "Y", olc(Y, O, T))
fig, ax = sekil(5.6, 2.6); ax.set_aspect("equal"); ax.axis("off")
ax.plot([-0.4, 4.4], [0, 0], color=SOLUK, lw=1.4)
ax.add_patch(patches.Polygon([O, Y, T], closed=True, facecolor=SARI_ACIK, edgecolor=SARI, lw=2))
ax.add_patch(patches.Rectangle((3.5, 0), 0.9, 1.2, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))
ax.text(3.95, 0.6, "kapı\ngirişi", ha="center", va="center", color=MAVI, fontsize=10)
dik(ax, Y, O, T, s=0.12)
aci(ax, O, Y, T, r=0.75, ad="α", renk=KIRMIZI)
kenar(ax, O, T, "3,7 m", G, d=0.22, renk=SARI)
ax.text(3.38, 0.6, "1,2 m", ha="right", va="center", fontsize=12)
ax.set_xlim(-0.5, 4.5); ax.set_ylim(-0.25, 1.75)
kaydet(fig, __file__)
