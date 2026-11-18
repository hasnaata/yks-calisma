import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 9: ABCD dikdörtgen, |AB| = 12, |BC| = 8; E, [DC] üzerinde, |DE| = 3. ADE ve BCE boyalı.
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

A, B, C, D, E = P(0, 0), P(12, 0), P(12, 8), P(0, 8), P(3, 8)
fig, ax = sekil(6, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, D, E], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.add_patch(patches.Polygon([B, C, E], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(A, E, B), color=YAZI)
harf(A, "A", -0.45, -0.35); harf(B, "B", 0.45, -0.35); harf(C, "C", 0.45, 0.35); harf(D, "D", -0.45, 0.35); harf(E, "E", 0, 0.5)
olcu(A, B, "12", (0, -0.95)); olcu(B, C, "8", (0.95, 0)); olcu(D, E, "3", (0, 1.25))
ax.set_xlim(-1.0, 14.3); ax.set_ylim(-2.4, 10.6)
kaydet(fig, __file__)
