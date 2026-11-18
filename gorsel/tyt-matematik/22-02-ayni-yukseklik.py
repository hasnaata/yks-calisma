# Örnek 1: D, [BC] üzerinde; |BD| = 6, |DC| = 4, A(ABC) = 40, yükseklik 8.
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
B, D, C, A = P(0, 0), P(6, 0), P(10, 0), P(2.5, 8); H = P(2.5, 0)
print("A(ABC)", 10 * 8 / 2, "A(ABD)", 6 * 8 / 2, "A(ADC)", 4 * 8 / 2)
fig, ax = sekil(5.4, 5)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, D], closed=True, facecolor=YESIL_ACIK, edgecolor="none"))
ax.add_patch(patches.Polygon([A, D, C], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(A, D), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.7, ls="--")
dik(H, A, C, 0.4)
harf(A, "A", 0, 0.5); harf(B, "B", -0.45, -0.1); harf(C, "C", 0.45, -0.1); harf(D, "D", 0.05, -0.5); harf(H, "H", -0.05, -0.5, KIRMIZI)
ax.text(2.2, 3.2, "h", ha="right", va="center", color=KIRMIZI, fontsize=14)
ax.text(*((A + B + D) / 3 + P(0.55, -0.4)), "24", ha="center", va="center", color=YESIL, fontsize=14, fontweight="bold")
ax.text(*((A + D + C) / 3 + P(0.3, -0.3)), "16", ha="center", va="center", color=MAVI, fontsize=14, fontweight="bold")
olcu(B, D, "6", (0, -1.2)); olcu(D, C, "4", (0, -1.2))
ax.set_xlim(-1, 11); ax.set_ylim(-2.6, 8.9)
kaydet(fig, __file__)
