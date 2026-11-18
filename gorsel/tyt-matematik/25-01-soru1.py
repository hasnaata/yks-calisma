# Alıştırma 1: [AB] ∥ [DC], m(A) = 68°, m(B) = 74° → m(C) = 106°.
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

AB, H, aA, aB, BOY = 8.5, 3.4, 68, 74, 3.0
UZAK = {}

A = P(0, 0); B = P(AB, 0)
D = P(H / np.tan(np.radians(aA)), H); C = P(AB - H / np.tan(np.radians(aB)), H)
ACILAR = [(A, B, D, 0.55, "68°", MAVI), (B, C, A, 0.55, "74°", YESIL), (C, D, B, 0.45, "?", YESIL)]
print("A", acisi(A, B, D), "B", acisi(B, A, C), "C", acisi(C, B, D), "D", acisi(D, A, C), "DC", uz(D, C))

fig, ax = sekil(6, BOY)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
paralel_isareti(A, B, f=0.5); paralel_isareti(D, C, f=0.5)
for Q in (A, B, C, D): nokta(ax, *Q, "")
ax.text(A[0] - 0.2, A[1] - 0.15, "A", ha="right", va="top")
ax.text(B[0] + 0.2, B[1] - 0.15, "B", ha="left", va="top")
ax.text(C[0] + 0.2, C[1] + 0.1, "C", ha="left", va="bottom")
ax.text(D[0] - 0.2, D[1] + 0.1, "D", ha="right", va="bottom")
for (K, U, V, r, metin, renk) in ACILAR:
    aci(ax, K, U, V, r=r, ad="", renk=renk)
    a1 = np.arctan2(*(U - K)[::-1]); a2 = np.arctan2(*(V - K)[::-1])
    u = (U - K) / np.linalg.norm(U - K) + (V - K) / np.linalg.norm(V - K); u = u / np.linalg.norm(u)
    ax.text(*(K + UZAK.get(metin, 1.9) * r * u), metin, ha="center", va="center", color=renk, fontsize=13)
x0 = min(A[0], D[0]); x1 = max(B[0], C[0])
ax.set_xlim(x0 - 0.8, x1 + 0.8); ax.set_ylim(-0.7, H + 0.7)
kaydet(fig, __file__)
