# Örnek 2: ortak taban [BC] = 9; |AE| = 8, |DF| = 6; F, BC doğrusunun C'den ötesinde.
import sys; sys.path.insert(0, "tools")
from cizim import *

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
def tik(X, Y, n=1, r=0.22, renk=SOLUK):
    """[XY] parçasının ortasına n adet eşitlik çentiği."""
    M = (X + Y) / 2; t = (Y - X) / uz(X, Y); nn = np.array([-t[1], t[0]])
    for i in range(n):
        Q = M + (i - (n - 1) / 2) * 0.16 * t
        ax.plot(*zip(Q - r * nn, Q + r * nn), color=renk, lw=1.3)
B, C, A, D = P(0, 0), P(9, 0), P(3, 8), P(11, 6); E, F = P(3, 0), P(11, 0)
print("A(ABC)", 9 * 8 / 2, "A(DBC)", 9 * 6 / 2)
fig, ax = sekil(6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=YESIL_ACIK, edgecolor="none", alpha=0.9))
ax.add_patch(patches.Polygon([D, B, C], closed=True, facecolor=MAVI_ACIK, edgecolor="none", alpha=0.75))
ax.plot(*zip(C, F), color=SOLUK, lw=1.5, ls="--")
ax.plot(*zip(B, C, A, B), color=YESIL)
ax.plot(*zip(B, D, C), color=MAVI)
ax.plot(*zip(B, C), color=YAZI, lw=2.6)
ax.plot(*zip(A, E), color=YESIL, lw=1.7, ls="--"); ax.plot(*zip(D, F), color=MAVI, lw=1.7, ls="--")
dik(E, A, C, 0.4); dik(F, D, B, 0.4)
harf(A, "A", 0, 0.5); harf(B, "B", -0.45, -0.1); harf(C, "C", 0, -0.5); harf(D, "D", 0.4, 0.3)
harf(E, "E", 0, -0.5); harf(F, "F", 0.4, -0.4)
ax.text(2.7, 4.6, "8", ha="right", va="center", color=YESIL, fontsize=14)
ax.text(11.3, 3, "6", ha="left", va="center", color=MAVI, fontsize=14)
olcu(B, C, "9", (0, -1.3))
ax.set_xlim(-1, 12.6); ax.set_ylim(-2.8, 8.9)
kaydet(fig, __file__)
