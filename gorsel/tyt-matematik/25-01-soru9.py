# Alıştırma 9: park. [AB] ∥ [DC], |AD| = 7, |BC| = 5, |DC| = 15; A ve B açılarının açıortayları [DC]'yi E ve F'de keser.
# |DE| = |AD| = 7, |FC| = |BC| = 5 → |EF| = 3.
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
D, C = P(0, H), P(15, H)
A = P(-np.sqrt(7**2 - H**2), 0); B = P(15 + np.sqrt(5**2 - H**2), 0)
yon = lambda d: P(np.cos(np.radians(d)), np.sin(np.radians(d)))
aA, aB = acisi(A, B, D), acisi(B, A, C)
E = kesis(A, yon(aA / 2), D, P(1, 0)); F = kesis(B, yon(180 - aB / 2), D, P(1, 0))
print("AD", uz(A, D), "BC", uz(B, C), "A", aA, "B", aB, "DE", uz(D, E), "EF", uz(E, F), "FC", uz(F, C))

fig, ax = sekil(6, 2.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=YESIL_ACIK, edgecolor="none"))
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(A, E), color=MAVI, lw=1.8); ax.plot(*zip(B, F), color=MAVI, lw=1.8)
paralel_isareti(A, B, f=0.5); paralel_isareti(D, C, f=0.2)
for Q in (A, B, C, D): nokta(ax, *Q, "")
nokta(ax, *E, "", renk=MAVI); nokta(ax, *F, "", renk=MAVI)
ax.text(A[0] - 0.2, -0.15, "A", ha="right", va="top")
ax.text(B[0] + 0.2, -0.15, "B", ha="left", va="top")
ax.text(C[0] + 0.2, C[1] + 0.1, "C", ha="left", va="bottom")
ax.text(D[0] - 0.2, D[1] + 0.1, "D", ha="right", va="bottom")
ax.text(E[0], E[1] + 0.25, "E", ha="center", va="bottom", color=MAVI)
ax.text(F[0], F[1] + 0.25, "F", ha="center", va="bottom", color=MAVI)
aci(ax, A, B, E, r=2.2, renk=MAVI); aci(ax, A, E, D, r=2.2, renk=MAVI)
aci(ax, B, F, A, r=1.3, renk=MAVI); aci(ax, B, C, F, r=1.3, renk=MAVI)
aci(ax, B, F, A, r=1.45, renk=MAVI); aci(ax, B, C, F, r=1.45, renk=MAVI)
olcu(A, D, "7", d=0.45); olcu(B, C, "5", d=-0.4)
ax.text((E[0] + F[0]) / 2, H - 0.35, "?", ha="center", va="top", color=KIRMIZI, fontsize=14)
# |DC| = 15 ölçü oku
yy = H + 1.6
ax.annotate("", xy=(C[0], yy), xytext=(D[0], yy), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(7.5 - 3.2, yy + 0.12, "15", ha="center", va="bottom", fontsize=13)
ax.set_xlim(A[0] - 0.8, B[0] + 0.8); ax.set_ylim(-0.8, H + 2.4)
kaydet(fig, __file__)
