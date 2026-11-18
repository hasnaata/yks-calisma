import sys; sys.path.insert(0, "tools")
from cizim import *

# Örnek 1: |BC| = 10, |AH| = 6, H, BC üzerinde (|BH| = 3). Üçgen 10 x 6 dikdörtgenin yarısı.
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

B, C, A, H = P(0, 0), P(10, 0), P(3, 6), P(3, 0)
D1, D2 = P(0, 6), P(10, 6)
fig, ax = sekil(6, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([B, H, A], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
ax.add_patch(patches.Polygon([H, C, A], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
ax.add_patch(patches.Polygon([B, A, D1], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.add_patch(patches.Polygon([A, C, D2], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.plot(*zip(B, D1, D2, C), color=SARI, lw=1.4, ls="--")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.9)
dik(H, A, C, 0.4)
harf(A, "A", 0, 0.42); harf(B, "B", -0.4, -0.05); harf(C, "C", 0.4, -0.05); harf(H, "H", 0, -0.42, KIRMIZI)
ax.text(3.2, 2.6, "6", ha="left", va="center", color=KIRMIZI, fontsize=13)
olcu(B, C, "10", (0, -0.9))
ax.set_xlim(-0.8, 10.8); ax.set_ylim(-2.3, 6.8)
kaydet(fig, __file__)
