# Alıştırma 5: [AB] ∥ [DC], [BE] ve [CE] sırasıyla B ve C açılarının açıortayları, m(ABC) = 64° → m(ECD) = 58°.
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

H = 4.5
A = P(0, 0); B = P(10, 0)
D = P(H / np.tan(np.radians(72)), H); C = P(B[0] - H / np.tan(np.radians(64)), H)
yon = lambda d: P(np.cos(np.radians(d)), np.sin(np.radians(d)))
E = kesis(B, yon(180 - 32), C, yon(180 + 58))
print("B", acisi(B, A, C), "ABE", acisi(B, A, E), "EBC", acisi(B, E, C), "BCD", acisi(C, B, D),
      "BCE", acisi(C, B, E), "ECD", acisi(C, E, D), "BEC", acisi(E, B, C), "E", E)

fig, ax = sekil(6, 3.1)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(B, E, C), color=MAVI, lw=1.8)
paralel_isareti(A, B, f=0.3); paralel_isareti(D, C, f=0.3)
for Q in (A, B, C, D): nokta(ax, *Q, "")
nokta(ax, *E, "", renk=MAVI)
ax.text(A[0] - 0.2, -0.15, "A", ha="right", va="top")
ax.text(B[0] + 0.2, -0.15, "B", ha="left", va="top")
ax.text(C[0] + 0.2, C[1] + 0.1, "C", ha="left", va="bottom")
ax.text(D[0] - 0.2, D[1] + 0.1, "D", ha="right", va="bottom")
ax.text(E[0] - 0.3, E[1], "E", ha="right", va="center", color=MAVI)
aci(ax, B, A, E, r=0.9, renk=YESIL); aci(ax, B, E, C, r=0.9, renk=YESIL)
aci(ax, B, A, E, r=1.0, renk=YESIL); aci(ax, B, E, C, r=1.0, renk=YESIL)
ax.text(B[0] - 1.9, 0.45, "64°", ha="center", va="center", color=YESIL, fontsize=13)
aci(ax, C, B, E, r=0.5, renk=SOLUK); aci(ax, C, E, D, r=0.75, renk=KIRMIZI)
ax.text(C[0] - 1.25, C[1] - 0.35, "?", ha="center", va="center", color=KIRMIZI, fontsize=14)
ax.set_xlim(-0.8, B[0] + 0.8); ax.set_ylim(-0.7, H + 0.7)
kaydet(fig, __file__)
