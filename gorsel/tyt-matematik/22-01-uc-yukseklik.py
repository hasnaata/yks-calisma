import sys; sys.path.insert(0, "tools")
from cizim import *

# Örnek 2: |AB| = 13, |BC| = 14, |CA| = 15; A(5, 12). h_a = 12, h_b = 11,2 (F, AC üzerinde).
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

B, C, A = P(0, 0), P(14, 0), P(5, 12)
H = P(5, 0)
u = (C - A) / uz(A, C); F = A + np.dot(B - A, u) * u
print("h_a", uz(A, H), "h_b", round(uz(B, F), 4), "F", F)
G = (A + B + C) / 3
fig, ax = sekil(6, 5.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.9)
ax.plot(*zip(B, F), color=YESIL, lw=1.9)
dik(H, A, C, 0.55); dik(F, B, C, 0.55)
harf(A, "A", 0, 0.65); harf(B, "B", -0.6, -0.1); harf(C, "C", 0.6, -0.1)
harf(H, "H", 0, -0.65, KIRMIZI); harf(F, "F", 0.55, 0.3, YESIL)
kenar(A, B, "13", G, 0.6); ax.text(12.3, 3.6, "15", ha="left", va="center", fontsize=13)
olcu(B, C, "14", (0, -1.3))
ax.text(5.25, 8.6, "12", ha="left", va="center", color=KIRMIZI, fontsize=13)
M = (B + F) / 2
ax.text(M[0] + 0.1, M[1] - 0.75, "$h_b$", ha="center", va="center", color=YESIL, fontsize=14)
ax.set_xlim(-1.2, 15.2); ax.set_ylim(-3.2, 13.3)
kaydet(fig, __file__)
