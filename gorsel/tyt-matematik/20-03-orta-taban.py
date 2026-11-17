import sys; sys.path.insert(0, "tools")
from cizim import *

# D, E: [AB] ve [AC]'nin orta noktaları; [AF] kenarortay, |AF| = 12; P = DE ∩ AF; G ağırlık merkezi.
# Beklenen: |AP| = 6, |PG| = 2, |GF| = 4 (3k, k, 2k; k = 2).
B = np.array([0.0, 0.0]); C = np.array([12.0, 0.0]); F = (B + C) / 2
A = np.array([5.0, np.sqrt(144 - 1)])
D, E = (A + B) / 2, (A + C) / 2
G = (A + B + C) / 3; P = (A + F) / 2
L = lambda X, Y: np.linalg.norm(X - Y)
print("AF", L(A, F), "AP", L(A, P), "PG", L(P, G), "GF", L(G, F))

def centik(P1, Q1, n, renk=SOLUK):
    M = (P1 + Q1) / 2; u = (Q1 - P1) / L(P1, Q1); v = np.array([-u[1], u[0]])
    for i in range(n):
        c = M + (i - (n - 1) / 2) * 0.22 * u
        ax.plot(*zip(c - 0.25 * v, c + 0.25 * v), color=renk, lw=1.4)

fig, ax = sekil(5.2, 5.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, E), color=CIZGI, lw=1.6, ls="--")
ax.plot(*zip(D, E), color=SARI, lw=2)
ax.plot(*zip(A, F), color=MAVI)
for X, Y, n in ((A, D, 1), (D, B, 1), (A, E, 2), (E, C, 2), (B, F, 3), (F, C, 3)):
    centik(X, Y, n)
nokta(ax, *A, "A", dx=-0.3, dy=0.4); nokta(ax, *B, "B", dx=-0.9, dy=-0.5); nokta(ax, *C, "C", dx=0.3, dy=-0.5)
nokta(ax, *D, "D", dx=-0.9, dy=0.0, renk=SARI); nokta(ax, *E, "E", dx=0.35, dy=0.0, renk=SARI)
nokta(ax, *F, "F", dx=-0.25, dy=-1.1, renk=MAVI)
nokta(ax, *P, "P", dx=-0.85, dy=0.15); nokta(ax, *G, "G", dx=-0.95, dy=-0.4)
for X, Y, t in ((A, P, "6"), (P, G, "2"), (G, F, "4")):
    M = (X + Y) / 2; ax.text(M[0] + 0.45, M[1], t, color=MAVI, fontsize=15, va="center")
ax.set_xlim(-1.2, 12.8); ax.set_ylim(-1.4, A[1] + 1.0)
kaydet(fig, __file__)
