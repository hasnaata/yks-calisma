import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 10: B(0, 0), C(6, 0); d: y = 4, d ∥ BC. A(2, 4) ve A'(9, 4) iki konum.
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

B, C, A, A2 = P(0, 0), P(6, 0), P(2, 4), P(9, 4)
fig, ax = sekil(6, 3.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-1.2, 11], [4, 4], color=SOLUK, lw=1.4, ls="--")
ax.text(11.2, 4, "d", ha="left", va="center", color=SOLUK, fontsize=13)
ax.plot([-1.2, 11], [0, 0], color=CIZGI, lw=1.0)
ax.plot(*zip(B, A2, C), color=YESIL, lw=2.0, ls=(0, (5, 3)))
ax.plot(*zip(B, C, A, B), color=MAVI)
ax.plot(*zip(B, C), color=YAZI, lw=2.4)
ax.annotate("", xy=(7.6, 4.45), xytext=(3.4, 4.45), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.3))
harf(A, "A", -0.1, 0.45, MAVI); harf(A2, "A'", 0.1, 0.45, YESIL); harf(B, "B", -0.4, -0.35); harf(C, "C", 0.2, -0.42)
ax.set_xlim(-1.5, 11.8); ax.set_ylim(-1.0, 5.2)
kaydet(fig, __file__)
