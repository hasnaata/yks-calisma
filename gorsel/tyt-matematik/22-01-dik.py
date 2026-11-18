import sys; sys.path.insert(0, "tools")
from cizim import *

# Örnek 3: A'da dik; |AB| = 12, |AC| = 16, |BC| = 20; hipotenüse ait yükseklik 9,6.
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

A, B, C = P(0, 0), P(0, 12), P(16, 0)
u = (C - B) / uz(B, C); H = B + np.dot(A - B, u) * u
print("BC", uz(B, C), "AH", round(uz(A, H), 4))
G = (A + B + C) / 3
fig, ax = sekil(6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
ax.plot(*zip(A, B), color=MAVI, lw=2.6); ax.plot(*zip(A, C), color=MAVI, lw=2.6)
ax.plot(*zip(B, C), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.6, ls="--")
dik(A, B, C, 0.8); dik(H, A, C, 0.6)
harf(A, "A", -0.6, -0.6); harf(B, "B", -0.7, 0.2); harf(C, "C", 0.7, -0.2); harf(H, "H", 0.55, 0.6, KIRMIZI)
ax.text(-0.5, 6, "12", ha="right", va="center", color=MAVI, fontsize=13)
ax.text(8, -0.7, "16", ha="center", va="top", color=MAVI, fontsize=13)
kenar(B, C, "20", G, 0.8)
M = (A + H) / 2
ax.text(M[0] + 0.35, M[1] - 0.55, "9,6", ha="left", va="center", color=KIRMIZI, fontsize=13)
ax.set_xlim(-2.2, 17.5); ax.set_ylim(-2.0, 13.2)
kaydet(fig, __file__)
