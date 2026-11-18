import sys; sys.path.insert(0, "tools")
from cizim import *

# Örnek 4: B'de geniş açı. |BC| = 6, A'dan BC doğrusuna dikme H, B'nin dışında; |HB| = 4, |AH| = 8.
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

H, B, C, A = P(-4, 0), P(0, 0), P(6, 0), P(-4, 8)
print("AB", round(uz(A, B), 4), "B açısı", round(float(np.degrees(np.arccos(np.dot(A - B, C - B) / uz(A, B) / uz(C, B)))), 2))
fig, ax = sekil(6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, H, B], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
ax.plot(*zip(H, B), color=SOLUK, lw=1.6, ls="--")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.9)
dik(H, A, B, 0.45)
harf(A, "A", 0, 0.5); harf(B, "B", 0.25, -0.5); harf(C, "C", 0.5, -0.1); harf(H, "H", -0.5, -0.1, KIRMIZI)
ax.text(-4.35, 4, "8", ha="right", va="center", color=KIRMIZI, fontsize=13)
olcu(H, B, "4", (0, -1.0)); olcu(B, C, "6", (0, -1.0))
ax.set_xlim(-5.5, 7.2); ax.set_ylim(-2.4, 8.9)
kaydet(fig, __file__)
