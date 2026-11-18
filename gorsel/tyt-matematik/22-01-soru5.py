import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 5: |AB| = |AC| = 10, |BC| = 12; [BH] ⊥ [AC], H, AC üzerinde; |BH| = 9,6.
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

B, C, A = P(0, 0), P(12, 0), P(6, 8)
u = (C - A) / uz(A, C); H = A + np.dot(B - A, u) * u
print("AB", uz(A, B), "BH", round(uz(B, H), 4), "H", H)
G = (A + B + C) / 3
fig, ax = sekil(6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(B, H), color=KIRMIZI, lw=1.9)
dik(H, B, C, 0.45)
harf(A, "A", 0, 0.5); harf(B, "B", -0.5, -0.05); harf(C, "C", 0.5, -0.05); harf(H, "H", 0.45, 0.3, KIRMIZI)
kenar(A, B, "10", G, 0.55)
ax.text(10.0, 3.9, "10", ha="center", va="center", fontsize=13)
olcu(B, C, "12", (0, -1.0))
M = (B + H) / 2
ax.text(M[0] + 0.1, M[1] - 0.6, "?", ha="center", va="center", color=KIRMIZI, fontsize=14)
ax.set_xlim(-1.0, 13.0); ax.set_ylim(-2.5, 8.9)
kaydet(fig, __file__)
