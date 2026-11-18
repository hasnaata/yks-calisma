# Alıştırma 10 (köprü): |EK| = |LF| = 5, |KL| = 7 → |DC| = 10, |AB| = 24.
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

AB, DC, DX, H, BOY = 24, 10, 7, 6.5, 2.5
ET = {"AB": "?", "EK": "5", "KL": "7", "LF": "5"}; EK = []

# Köşegenler orta tabanı K ve L'de keser: K ∈ [AC], L ∈ [BD].
A, B, C, D = P(0, 0), P(AB, 0), P(DX + DC, H), P(DX, H)
E, F = (A + D) / 2, (B + C) / 2
K = kesis(A, C - A, E, F - E); L = kesis(B, D - B, E, F - E)
print("AB", uz(A, B), "DC", uz(D, C), "EF", uz(E, F), "EK", uz(E, K), "KL", uz(K, L), "LF", uz(L, F))

fig, ax = sekil(6, BOY)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(A, C), color=SOLUK, lw=1.4, ls="--"); ax.plot(*zip(B, D), color=SOLUK, lw=1.4, ls="--")
ax.plot(*zip(E, K), color=MAVI, lw=2.4); ax.plot(*zip(L, F), color=MAVI, lw=2.4); ax.plot(*zip(K, L), color=KIRMIZI, lw=2.4)
paralel_isareti(A, B, f=0.22); paralel_isareti(D, C, f=0.8)
s = AB / 14
cetik(A, E, L=0.16 * s); cetik(E, D, L=0.16 * s); cetik(B, F, 2, L=0.16 * s); cetik(F, C, 2, L=0.16 * s)
for Q in (A, B, C, D): nokta(ax, *Q, "")
for Q, r in ((E, MAVI), (F, MAVI), (K, KIRMIZI), (L, KIRMIZI)): nokta(ax, *Q, "", renk=r)
s = AB / 14
ax.text(A[0] - 0.25 * s, -0.15 * s, "A", ha="right", va="top")
ax.text(B[0] + 0.25 * s, -0.15 * s, "B", ha="left", va="top")
ax.text(C[0] + 0.2 * s, C[1] + 0.1 * s, "C", ha="left", va="bottom")
ax.text(D[0] - 0.2 * s, D[1] + 0.1 * s, "D", ha="right", va="bottom")
ax.text(E[0] - 0.3 * s, E[1], "E", ha="right", va="center", color=MAVI)
ax.text(F[0] + 0.3 * s, F[1], "F", ha="left", va="center", color=MAVI)
ax.text(K[0], K[1] - 0.4 * s, "K", ha="center", va="top", color=KIRMIZI)
ax.text(L[0], L[1] - 0.4 * s, "L", ha="center", va="top", color=KIRMIZI)
if ET.get("AB"): olcu(A, B, ET["AB"], d=-0.45 * s)
if ET.get("DC"): olcu(D, C, ET["DC"], d=0.4 * s)
for (U, V, k, r) in ((E, K, "EK", MAVI), (L, F, "LF", MAVI)):
    if ET.get(k): ax.text((U[0] + V[0]) / 2, U[1] + 0.3 * s, ET[k], ha="center", va="bottom", color=r, fontsize=13)
if ET.get("KL"): ax.text((K[0] + L[0]) / 2, K[1] - 0.35 * s, ET["KL"], ha="center", va="top", color=KIRMIZI, fontsize=13)
for (fx, fy, metin, renk) in EK:
    ax.text(fx, fy, metin, ha="center", va="center", color=renk, fontsize=13)
ax.set_xlim(-0.9 * s, B[0] + 0.9 * s); ax.set_ylim(-1.0 * s, C[1] + 0.9 * s)
kaydet(fig, __file__)
