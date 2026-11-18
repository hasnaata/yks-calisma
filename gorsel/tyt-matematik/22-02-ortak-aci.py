# Örnek 6: |AD| = 3, |DB| = 1, |AE| = 2, |EC| = 4; A açısı ortak (55°, sorunun cevabı açıya bağlı değil).
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
a = np.radians(55)
A0, B0, C0 = P(0, 0), 4 * P(1, 0), 6 * P(np.cos(a), np.sin(a))
t = np.arctan2(*(C0 - B0)[::-1]); R = np.array([[np.cos(-t), -np.sin(-t)], [np.sin(-t), np.cos(-t)]])
A, B, C = [R @ (X - B0) for X in (A0, B0, C0)]
if A[1] < 0: A, B, C = [P(X[0], -X[1]) for X in (A, B, C)]
D, E = A + (B - A) * 3 / 4, A + (C - A) * 2 / 6
print("AB", round(uz(A, B), 4), "AC", round(uz(A, C), 4), "AD", round(uz(A, D), 4), "AE", round(uz(A, E), 4),
      "oran", round(alan(A, D, E) / alan(A, B, C), 4))
G = (A + B + C) / 3
fig, ax = sekil(5.6, 3.8)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, D, E], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
ax.add_patch(patches.Polygon([D, B, C, E], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(D, E), color=MAVI, lw=2)
aci(ax, A, B, C, r=0.45)
harf(A, "A", 0, 0.4); harf(B, "B", -0.4, -0.1); harf(C, "C", 0.4, -0.1)
nD = D - G; harf(D, "D", -0.42, 0.05); harf(E, "E", 0.4, 0.15)
kenar(A, D, "3", G, 0.35); kenar(D, B, "1", G, 0.35); kenar(A, E, "2", G, 0.35); kenar(E, C, "4", G, 0.35)
xs = [X[0] for X in (A, B, C)]; ys = [X[1] for X in (A, B, C)]
ax.set_xlim(min(xs) - 0.9, max(xs) + 0.9); ax.set_ylim(min(ys) - 0.5, max(ys) + 0.7)
kaydet(fig, __file__)
