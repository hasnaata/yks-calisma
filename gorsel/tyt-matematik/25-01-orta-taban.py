# Örnek 3: [AB] ∥ [DC], |AB| = 14, |DC| = 6; E ve F yan kenarların orta noktaları → |EF| = 10.
# Neden: [BD] köşegeni [EF]'yi L'de keser; |EL| = 14/2 = 7 (ABD üçgeni), |LF| = 6/2 = 3 (BCD üçgeni).
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

A, B, C, D = P(0, 0), P(14, 0), P(9, 5), P(3, 5)
E, F = (A + D) / 2, (B + C) / 2
L = kesis(B, D - B, E, F - E)
print("EF", uz(E, F), "EL", uz(E, L), "LF", uz(L, F), "L orta mı", uz(B, L), uz(L, D))

fig, ax = sekil(6, 2.9)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(B, D), color=SOLUK, lw=1.4, ls="--")
ax.plot(*zip(E, F), color=MAVI, lw=2.4)
paralel_isareti(A, B, f=0.3); paralel_isareti(D, C, f=0.75)
cetik(A, E); cetik(E, D); cetik(B, F, 2); cetik(F, C, 2)
for Q in (A, B, C, D): nokta(ax, *Q, "")
nokta(ax, *E, "", renk=MAVI); nokta(ax, *F, "", renk=MAVI); nokta(ax, *L, "", renk=SOLUK)
ax.text(A[0] - 0.25, -0.15, "A", ha="right", va="top")
ax.text(B[0] + 0.25, -0.15, "B", ha="left", va="top")
ax.text(C[0] + 0.2, C[1] + 0.1, "C", ha="left", va="bottom")
ax.text(D[0] - 0.2, D[1] + 0.1, "D", ha="right", va="bottom")
ax.text(E[0] - 0.3, E[1], "E", ha="right", va="center", color=MAVI)
ax.text(F[0] + 0.3, F[1], "F", ha="left", va="center", color=MAVI)
ax.text(L[0] + 0.1, L[1] - 0.35, "L", ha="left", va="top", color=SOLUK)
olcu(A, B, "14", d=-0.45); olcu(D, C, "6", d=0.4)
ax.text((E[0] + L[0]) / 2, E[1] + 0.35, "7", ha="center", va="bottom", color=SOLUK, fontsize=12)
ax.text((L[0] + F[0]) / 2, E[1] + 0.35, "3", ha="center", va="bottom", color=SOLUK, fontsize=12)
ax.text((E[0] + F[0]) / 2 - 1.2, E[1] - 0.35, "|EF| = 10", ha="center", va="top", color=MAVI, fontsize=13)
ax.set_xlim(-0.9, B[0] + 0.9); ax.set_ylim(-1.0, C[1] + 0.9)
kaydet(fig, __file__)
