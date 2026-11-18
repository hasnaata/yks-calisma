# Alıştırma 12: ABCD yamuğu [EF] orta tabanı boyunca kesilir. ABFE'nin orta tabanı 22, EFCD'ninki 14 → |EF| = 18, |AB| = 26, |DC| = 10.
import sys; sys.path.insert(0, "tools")
from cizim import *

P = lambda x, y: np.array([float(x), float(y)])
uz = lambda U, V: round(float(np.linalg.norm(U - V)), 4)
def acisi(K, U, V):
    u, v = U - K, V - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)
def kesis(p, u, q, v):
    t = np.linalg.solve(np.array([u, -v]).T, q - p); return p + t[0] * u
def paralel_isareti(U, V, renk=SOLUK, k=0.18, f=0.5):
    M = U + f * (V - U); t = (V - U) / np.linalg.norm(V - U)
    ax.annotate("", xy=M + k * t, xytext=M - k * t, arrowprops=dict(arrowstyle="-|>", color=renk, lw=1.4, mutation_scale=14))
def cetik(U, V, n=1, renk=SOLUK, L=0.16):
    M = (U + V) / 2; t = (V - U) / np.linalg.norm(V - U); m = np.array([-t[1], t[0]])
    for i in range(n):
        c = M + (i - (n - 1) / 2) * 0.13 * t
        ax.plot(*zip(c - L * m, c + L * m), color=renk, lw=1.5)
def olcu(U, V, metin, d=0.3, renk=YAZI, fs=13):
    """[UV] parçasının ortasına, U→V yönünün soluna d kadar uzağa yazı (d < 0: sağına)."""
    M = (U + V) / 2; t = (V - U) / np.linalg.norm(V - U); m = np.array([-t[1], t[0]])
    ax.text(*(M + d * m), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik_isareti(K, U, V, r=0.28):
    a_ = (U - K) / np.linalg.norm(U - K) * r; b_ = (V - K) / np.linalg.norm(V - K) * r
    ax.plot(*zip(K + a_, K + a_ + b_, K + b_), color=SOLUK, lw=1.3)

A, B, C, D = P(0, 0), P(26, 0), P(16, 8), P(6, 8)
E, F = (A + D) / 2, (B + C) / 2
M1, N1 = (A + E) / 2, (B + F) / 2      # alt parçanın orta tabanı
M2, N2 = (E + D) / 2, (F + C) / 2      # üst parçanın orta tabanı
print("AB", uz(A, B), "DC", uz(D, C), "EF", uz(E, F), "alt orta", uz(M1, N1), "üst orta", uz(M2, N2))

fig, ax = sekil(6, 2.8)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, F, E], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
ax.add_patch(patches.Polygon([E, F, C, D], closed=True, facecolor=YESIL_ACIK, edgecolor="none"))
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(E, F), color=KIRMIZI, lw=2.2)
ax.plot(*zip(M1, N1), color=MAVI, lw=1.6, ls="--"); ax.plot(*zip(M2, N2), color=YESIL, lw=1.6, ls="--")
paralel_isareti(A, B, f=0.2); paralel_isareti(D, C, f=0.75)
for Q in (A, B, C, D): nokta(ax, *Q, "")
nokta(ax, *E, "", renk=KIRMIZI); nokta(ax, *F, "", renk=KIRMIZI)
ax.text(A[0] - 0.4, -0.3, "A", ha="right", va="top")
ax.text(B[0] + 0.4, -0.3, "B", ha="left", va="top")
ax.text(C[0] + 0.4, C[1] + 0.2, "C", ha="left", va="bottom")
ax.text(D[0] - 0.4, D[1] + 0.2, "D", ha="right", va="bottom")
ax.text(E[0] - 0.6, E[1], "E", ha="right", va="center", color=KIRMIZI)
ax.text(F[0] + 0.6, F[1], "F", ha="left", va="center", color=KIRMIZI)
ax.text(13, M1[1] + 0.3, "22", ha="center", va="bottom", color=MAVI, fontsize=13)
ax.text(11, M2[1] + 0.3, "14", ha="center", va="bottom", color=YESIL, fontsize=13)
ax.text(13, -0.6, "?", ha="center", va="top", color=YAZI, fontsize=14)
ax.text(5.5, E[1] - 0.3, "kesim", ha="center", va="top", color=KIRMIZI, fontsize=11)
ax.set_xlim(-1.6, 27.6); ax.set_ylim(-2.0, 9.6)
kaydet(fig, __file__)
