import sys; sys.path.insert(0, "tools")
from cizim import *

# Kendini dene 1: C'de geniş açı. |BC| = 5, |CH| = 3, |AH| = 4, |AC| = 5; H, BC doğrusu üzerinde C'nin ötesinde.
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

B, C, H, A = P(0, 0), P(5, 0), P(8, 0), P(8, 4)
print("AC", uz(A, C))
G = (A + B + C) / 3
fig, ax = sekil(6, 3.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(C, H), color=SOLUK, lw=1.6, ls="--")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.9)
dik(H, A, C, 0.3)
harf(A, "A", 0, 0.42); harf(B, "B", -0.42, -0.05); harf(C, "C", -0.1, -0.45); harf(H, "H", 0.42, -0.05, KIRMIZI)
ax.text(8.28, 2, "4", ha="left", va="center", color=KIRMIZI, fontsize=13)
kenar(A, C, "5", G, 0.4)
olcu(B, C, "5", (0, -0.8)); olcu(C, H, "3", (0, -0.8))
ax.set_xlim(-0.8, 9.0); ax.set_ylim(-1.8, 4.7)
kaydet(fig, __file__)
