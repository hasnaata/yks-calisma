# Örnek 3: G ağırlık merkezi; üç kenarortay üçgeni 6 eşit alana böler.
import sys; sys.path.insert(0, "tools")
from cizim import *

P = lambda x, y: np.array([float(x), float(y)])
uz = lambda X, Y: float(np.linalg.norm(X - Y))
def dik(K, X, Y, r):
    """K köşesinde KX ile KY arasındaki dik açı işareti (r: kenar boyu)."""
    a_ = (X - K) / uz(X, K) * r; b_ = (Y - K) / uz(Y, K) * r
    ax.plot(*zip(K + a_, K + a_ + b_, K + b_), color=SOLUK, lw=1.3)
def kenalan(X, Y, metin, G, d, renk=YAZI, fs=13):
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
B, C, A = P(0, 0), P(10, 0), P(3.5, 8)
D, E, F = (A + B) / 2, (A + C) / 2, (B + C) / 2; G = (A + B + C) / 3
parcalar = [(A, D, G), (D, B, G), (B, F, G), (F, C, G), (C, E, G), (E, A, G)]
print("alanlar", [round(alan(X, Y, Z), 4) for X, Y, Z in parcalar])
fig, ax = sekil(5.4, 4.8)
ax.set_aspect("equal"); ax.axis("off")
renkler = [SARI_ACIK, MAVI_ACIK] * 3
for (X, Y, Z), r in zip(parcalar, renkler):
    ax.add_patch(patches.Polygon([X, Y, Z], closed=True, facecolor=r, edgecolor="none"))
    ax.text(*((X + Y + Z) / 3), "S", ha="center", va="center", color=YAZI, fontsize=13, fontweight="bold")
ax.plot(*zip(B, C, A, B), color=YAZI)
for X, Y in ((A, F), (B, E), (C, D)): ax.plot(*zip(X, Y), color=MAVI, lw=1.6)
tik(A, D, 1); tik(D, B, 1); tik(B, F, 2); tik(F, C, 2); tik(C, E, 3); tik(E, A, 3)
harf(A, "A", 0, 0.5); harf(B, "B", -0.45, -0.1); harf(C, "C", 0.45, -0.1)
harf(D, "D", -0.5, 0.15); harf(E, "E", 0.5, 0.15); harf(F, "F", 0, -0.5); harf(G, "G", 0.15, 0.55, MAVI)
ax.set_xlim(-1, 11); ax.set_ylim(-1, 8.8)
kaydet(fig, __file__)
