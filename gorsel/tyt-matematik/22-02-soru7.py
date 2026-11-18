# Alıştırma 7: G ağırlık merkezi; D, [BC]'nin, E, [AC]'nin orta noktası; A(ABC) = 54.
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
B, C, A = P(0, 0), P(12, 0), P(3, 9)
D, E = (B + C) / 2, (A + C) / 2; G = (A + B + C) / 3
print("A(ABC)", alan(A, B, C), "A(GDCE)", alan(G, D, C) + alan(G, C, E))
fig, ax = sekil(5.6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([G, D, C, E], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.plot(*zip(B, C, A, B), color=YAZI); ax.plot(*zip(A, D), color=MAVI, lw=1.7); ax.plot(*zip(B, E), color=MAVI, lw=1.7)
tik(B, D, 1); tik(D, C, 1); tik(A, E, 2); tik(E, C, 2)
harf(A, "A", 0, 0.55); harf(B, "B", -0.5, -0.1); harf(C, "C", 0.5, -0.1); harf(D, "D", 0, -0.55); harf(E, "E", 0.5, 0.25)
harf(G, "G", -0.6, 0.3, MAVI)
ax.set_xlim(-1.0, 13.0); ax.set_ylim(-1.0, 9.9)
kaydet(fig, __file__)
