# Örnek 5: |AB| = 8, |AC| = 6; üstte m(A) = 30°, altta m(A) = 150°. İkisinde de C'nin AB doğrusuna uzaklığı 3.
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
fig, ax = sekil(6, 5.6)
ax.set_aspect("equal"); ax.axis("off")
for oy, aci_ in ((5.6, 30), (0, 150)):
    o = P(0, oy)
    A, B = o + P(0, 0), o + P(8, 0)
    C = A + 6 * P(np.cos(np.radians(aci_)), np.sin(np.radians(aci_))); H = P(C[0], oy)
    print(aci_, "C", C.round(4), "yükseklik", round(C[1] - oy, 4), "alan", round(alan(A, B, C), 4))
    ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
    if aci_ > 90: ax.plot(*zip(A, H), color=SOLUK, lw=1.5, ls="--")
    ax.plot(*zip(A, B, C, A), color=YAZI)
    ax.plot(*zip(C, H), color=KIRMIZI, lw=1.7, ls="--")
    dik(H, C, B, 0.3)
    if aci_ < 90:
        aci(ax, A, B, C, r=0.9); ax.text(2.35, oy + 0.33, "30°", ha="center", va="center", color=MAVI, fontsize=12)
    else:
        aci(ax, A, B, C, r=0.5, ad="150°")
    harf(A, "A", -0.1 if aci_ < 90 else 0.15, -0.45); harf(B, "B", 0.42, -0.05); harf(C, "C", 0, 0.42)
    harf(H, "H", 0, -0.45, KIRMIZI)
    ax.text(C[0] + (0.25 if aci_ < 90 else -0.25), oy + 1.5, "3", ha="left" if aci_ < 90 else "right", va="center", color=KIRMIZI, fontsize=13)
    G = (A + B + C) / 3
    kenar(A, C, "6", G, 0.4)
    ax.text(5.6 if aci_ > 90 else 3.0, oy - 0.45, "8", ha="center", va="center", color=YAZI, fontsize=13)
ax.set_xlim(-6.3, 9.0); ax.set_ylim(-0.9, 9.2)
kaydet(fig, __file__)
