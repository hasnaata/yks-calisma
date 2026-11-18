import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 8: tarla ABC; B ve C yol üzerinde, |BC| = 30 m, |HB| = 10 m, |AH| = 24 m (|AB| = 26 m).
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

H, B, C, A = P(-10, 0), P(0, 0), P(30, 0), P(-10, 24)
print("AB", uz(A, B))
fig, ax = sekil(6, 4.0)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Rectangle((-16, -2.2), 52, 2.2, facecolor="#e6e3dc", edgecolor="none", zorder=0))
ax.plot([-16, 36], [0, 0], color=SOLUK, lw=1.4)
ax.text(33, -1.1, "yol", ha="center", va="center", color=SOLUK, fontsize=12)
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2.2))
ax.text(9, 7, "tarla", ha="center", va="center", color=YESIL, fontsize=13)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.9)
dik(H, A, B, 1.3)
harf(A, "A", 0, 1.6); harf(B, "B", 0.5, 1.4); harf(C, "C", 0.4, 1.4); harf(H, "H", -1.6, 1.0, KIRMIZI)
ax.text(-11.2, 12, "24", ha="right", va="center", color=KIRMIZI, fontsize=13)
olcu(H, B, "10", (0, -3.6)); olcu(B, C, "30", (0, -3.6))
ax.set_xlim(-16.5, 36.5); ax.set_ylim(-7.8, 27.5)
kaydet(fig, __file__)
