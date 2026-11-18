import sys; sys.path.insert(0, "tools")
from cizim import *

# Örnek 5: solda |AB| = |AC| = 5, |BC| = 8 ikizkenar (h = 3); sağda kenarı 6 olan eşkenar DEF (h = 3√3).
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

B, C, A = P(0, 0), P(8, 0), P(4, 3); H = P(4, 0)
E, F, D = P(10, 0), P(16, 0), P(13, 3 * np.sqrt(3)); K_ = P(13, 0)
print("AB", uz(A, B), "DE", round(uz(D, E), 4), "DF", round(uz(D, F), 4), "h", round(uz(D, K_), 4))
G1, G2 = (A + B + C) / 3, (D + E + F) / 3
fig, ax = sekil(6.4, 3.2)
ax.set_aspect("equal"); ax.axis("off")
for X, Y, Z in ((A, B, C), (D, E, F)):
    ax.add_patch(patches.Polygon([X, Y, Z], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
    ax.plot(*zip(Y, Z, X, Y), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.8); ax.plot(*zip(D, K_), color=KIRMIZI, lw=1.8)
dik(H, A, C, 0.35); dik(K_, D, F, 0.35)
harf(A, "A", 0, 0.45); harf(B, "B", -0.45, -0.1); harf(C, "C", 0.45, -0.1); harf(H, "H", 0, -0.45, KIRMIZI)
harf(D, "D", 0, 0.45); harf(E, "E", -0.45, -0.1); harf(F, "F", 0.45, -0.1); harf(K_, "K", 0, -0.45, KIRMIZI)
kenar(A, B, "5", G1, 0.45); kenar(A, C, "5", G1, 0.45)
ax.text(2, -0.42, "4", ha="center", va="center", fontsize=13); ax.text(6, -0.42, "4", ha="center", va="center", fontsize=13)
ax.text(4.15, 1.45, "3", ha="left", va="center", color=KIRMIZI, fontsize=13)
kenar(D, E, "6", G2, 0.45); kenar(D, F, "6", G2, 0.45)
ax.text(11.5, -0.42, "3", ha="center", va="center", fontsize=13); ax.text(14.5, -0.42, "3", ha="center", va="center", fontsize=13)
ax.text(12.85, 1.5, "$3\\sqrt{3}$", ha="right", va="center", color=KIRMIZI, fontsize=13)
ax.set_xlim(-0.9, 16.9); ax.set_ylim(-1.0, 6.0)
kaydet(fig, __file__)
