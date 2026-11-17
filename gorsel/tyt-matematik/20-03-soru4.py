import sys; sys.path.insert(0, "tools")
from cizim import *

# D, E orta noktalar; [AF] kenarortay, |AF| = 18; P = DE ∩ AF; G ağırlık merkezi; |PG| = 3.
B = np.array([0.0, 0.0]); C = np.array([14.0, 0.0]); F = (B + C) / 2
A = np.array([9.0, np.sqrt(18**2 - 4)])
D, E = (A + B) / 2, (A + C) / 2
G = (A + B + C) / 3; P = (A + F) / 2
L = lambda X, Y: np.linalg.norm(X - Y)
print("AF", L(A, F), "AP", L(A, P), "PG", L(P, G), "GF", L(G, F), "P.y-D.y", P[1] - D[1])

def centik(P1, Q1, n, renk=SOLUK):
    M = (P1 + Q1) / 2; u = (Q1 - P1) / L(P1, Q1); v = np.array([-u[1], u[0]])
    for i in range(n):
        c = M + (i - (n - 1) / 2) * 0.3 * u
        ax.plot(*zip(c - 0.35 * v, c + 0.35 * v), color=renk, lw=1.4)

fig, ax = sekil(5, 5.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(D, E), color=YAZI, lw=1.8)
ax.plot(*zip(A, F), color=MAVI)
for X, Y, n in ((A, D, 1), (D, B, 1), (A, E, 2), (E, C, 2), (B, F, 3), (F, C, 3)):
    centik(X, Y, n)
nokta(ax, *A, "A", dx=-0.3, dy=0.5); nokta(ax, *B, "B", dx=-1.1, dy=-0.7); nokta(ax, *C, "C", dx=0.35, dy=-0.7)
nokta(ax, *D, "D", dx=-1.1, dy=0.0); nokta(ax, *E, "E", dx=0.45, dy=0.0)
nokta(ax, *F, "F", dx=-0.35, dy=-1.5)
nokta(ax, *P, "P", dx=-1.1, dy=0.3); nokta(ax, *G, "G", dx=-1.2, dy=-0.5)
M = (P + G) / 2; ax.text(M[0] + 0.55, M[1], "3", color=MAVI, fontsize=15, va="center")
ax.set_xlim(-1.6, 15.0); ax.set_ylim(-1.9, A[1] + 1.4)
kaydet(fig, __file__)
