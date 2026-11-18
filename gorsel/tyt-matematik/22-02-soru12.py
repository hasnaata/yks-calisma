# Alıştırma 12: D ∈ [BC], |DC| = 2|BD|; E ∈ [AD], |AE| = 3|ED|; A(ABC) = 1200 m².
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
def alan(X, Y, Z):
    """XYZ üçgeninin alanı (kontrol için)."""
    u, v = Y - X, Z - X
    return abs(u[0] * v[1] - u[1] * v[0]) / 2
B, D, C, A = P(0, 0), P(3, 0), P(9, 0), P(2, 8); E = A + (D - A) * 3 / 4
print("oran A(EDC)/A(ABC)", round(alan(E, D, C) / alan(A, B, C), 4), "·1200 =", round(1200 * alan(E, D, C) / alan(A, B, C), 4))
G = (A + B + C) / 3
fig, ax = sekil(4.8, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([E, D, C], closed=True, facecolor=YESIL_ACIK, edgecolor="none"))
ax.plot(*zip(B, C, A, B), color=YAZI); ax.plot(*zip(A, D), color=YAZI)
ax.plot(*zip(B, E, C), color=SOLUK, lw=1.6)
harf(A, "A", 0, 0.5); harf(B, "B", -0.45, -0.1); harf(C, "C", 0.45, -0.1); harf(D, "D", 0.05, -0.5); harf(E, "E", 0.5, 0.2)
kenar(A, E, "3y", P(9, 0), 0.6); kenar(E, D, "y", P(-5, 0), 0.4)
olcu(B, D, "x", (0, -1.2)); olcu(D, C, "2x", (0, -1.2))
ax.set_xlim(-0.9, 9.9); ax.set_ylim(-2.6, 8.9)
kaydet(fig, __file__)
