import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 11: çivi tahtası; A(1, 1), B(5, 1), C(2, 4); K(3, 6), L(0, 5), M(6, 5), N(7, 4), P(8, 7).
P = lambda x, y: np.array([float(x), float(y)])
uz = lambda X, Y: float(np.linalg.norm(X - Y))
def dik(K, X, Y, r):
    """K köşesinde KX ile KY arasındaki dik açı işareti (r: kenar boyu)."""
    a_ = (X - K) / uz(X, K) * r; b_ = (Y - K) / uz(Y, K) * r
    ax.plot(*zip(K + a_, K + a_ + b_, K + b_), color=SOLUK, lw=1.3)
def kenar(X, Y, metin, G, d, renk=YAZI, fs=13):
    """[XY] kenarının ortasına, G'den uzak yana d kadar açıkta etiket."""
    M = (X + Y) / 2; t = (Y - X) / uz(X, Y); n = np.array([-t[1], t[0]])
    if np.dot(n, M - G) < 0: n = -n
    ax.text(*(M + d * n), metin, ha="center", va="center", color=renk, fontsize=fs)
def olcu(X, Y, metin, kay, renk=SOLUK, fs=13):
    """X ile Y arasında, kay vektörü kadar kaydırılmış oklu ölçü çizgisi; yazı çizginin dışında."""
    kay = np.array(kay, dtype=float); X2, Y2 = X + kay, Y + kay
    ax.annotate("", xy=Y2, xytext=X2, arrowprops=dict(arrowstyle="<->", color=renk, lw=1.2, shrinkA=0, shrinkB=0))
    for Z in (X, Y): ax.plot(*zip(Z + kay * 0.6, Z + kay * 1.4), color=renk, lw=1)
    M = (X2 + Y2) / 2 + 0.75 * kay
    ax.text(*M, metin, ha="center", va="center", color=YAZI, fontsize=fs)
def harf(X, ad, dx, dy, renk=YAZI):
    nokta(ax, *X, "", renk=renk)
    ax.text(X[0] + dx, X[1] + dy, ad, ha="center", va="center", color=renk, fontsize=13)

A, B, C = P(1, 1), P(5, 1), P(2, 4)
adaylar = {"K": P(3, 6), "L": P(0, 5), "M": P(6, 5), "N": P(7, 4), "P": P(8, 7)}
for ad, X in adaylar.items(): print(ad, "alan", abs((B - A)[0] * (X - A)[1] - (B - A)[1] * (X - A)[0]) / 2)
fig, ax = sekil(6, 5.4)
ax.set_aspect("equal"); ax.axis("off")
for x in range(0, 9):
    for y in range(0, 8): ax.plot(x, y, "o", color=CIZGI, markersize=5, zorder=1)
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2.2, zorder=2))
harf(A, "A", -0.35, -0.35); harf(B, "B", 0.35, -0.35); harf(C, "C", -0.35, 0.3)
for ad, X in adaylar.items():
    ax.plot(*X, "o", color=KIRMIZI, markersize=8, zorder=4)
    ax.text(X[0] + 0.33, X[1] + 0.3, ad, ha="center", va="center", color=KIRMIZI, fontsize=13)
ax.set_xlim(-0.6, 8.7); ax.set_ylim(-0.7, 7.7)
kaydet(fig, __file__)
