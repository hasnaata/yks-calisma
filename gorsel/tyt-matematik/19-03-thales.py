import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P) - np.asarray(Q))), 3)
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kenar(ax, P, Q, metin, G, d=0.45, renk=YAZI, fs=13):
    """[PQ] kenarının ortasına, G noktasından uzak tarafa etiket."""
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def centik(ax, P, Q, n=1, renk=SOLUK, L=0.18, ara=0.12):
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]]); M = (P + Q) / 2
    for k in range(n):
        c = M + (k - (n - 1) / 2) * ara * u
        ax.plot(*zip(c - L * v, c + L * v), color=renk, lw=1.6)

# Thales: d1 ∥ d2 ∥ d3. |AB|=4, |BC|=6, |DE|=5, |EF|=x (7,5).
a1 = 75; C = np.array([0.0, 0.0]); B = C + 6 * yon(a1); A = C + 10 * yon(a1)
a2 = np.degrees(np.arcsin(B[1] / 7.5)); F = np.array([4.0, 0.0]); E = F + 7.5 * yon(a2); D = F + 12.5 * yon(a2)
print("AB", uz(A, B), "BC", uz(B, C), "DE", uz(D, E), "EF", uz(E, F), "yB", B[1], "yE", E[1], "yA", A[1], "yD", D[1])
fig, ax = sekil(5.5, 4.4)
ax.set_aspect("equal"); ax.axis("off")
x0, x1 = -1.5, 14.5
for y, ad in ((A[1], "d₁"), (B[1], "d₂"), (0, "d₃")):
    ax.annotate("", xy=(x1, y), xytext=(x0, y), arrowprops=dict(arrowstyle="<->", color=MAVI, lw=1.8))
    ax.text(x1 + 0.3, y, ad, color=MAVI, va="center", fontsize=13)
ax.plot(*zip(C - 0.8 * yon(a1), A + 0.8 * yon(a1)), color=YAZI)
ax.plot(*zip(F - 0.8 * yon(a2), D + 0.8 * yon(a2)), color=YAZI)
nokta(ax, *A, "A", dx=-0.9, dy=0.3); nokta(ax, *B, "B", dx=-0.9, dy=0.3); nokta(ax, *C, "C", dx=-0.9, dy=0.3)
nokta(ax, *D, "D", dx=0.45, dy=-0.85); nokta(ax, *E, "E", dx=0.45, dy=-0.85); nokta(ax, *F, "F", dx=0.45, dy=-0.85)
kenar(ax, A, B, "4", (5, 5), d=0.6); kenar(ax, B, C, "6", (5, 5), d=0.6)
kenar(ax, D, E, "5", (5, 5), d=0.6); kenar(ax, E, F, "x", (5, 5), d=0.6)
ax.set_xlim(x0 - 0.3, x1 + 1.3); ax.set_ylim(-1.0, A[1] + 1.2)
kaydet(fig, __file__)
