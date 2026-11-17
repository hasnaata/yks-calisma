import sys; sys.path.insert(0, "tools")
from cizim import *

# Üç kenarortay G'de kesişir. Çentikler: BD=DC (1), CE=EA (2), AF=FB (3).
A = np.array([2.0, 5.2]); B = np.array([0.0, 0.0]); C = np.array([7.0, 0.0])
D, E, F = (B + C) / 2, (A + C) / 2, (A + B) / 2
G = (A + B + C) / 3

def centik(ax, P, Q, n, renk=SOLUK):
    M = (P + Q) / 2; u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    for i in range(n):
        c = M + (i - (n - 1) / 2) * 0.13 * u
        ax.plot(*zip(c - 0.14 * v, c + 0.14 * v), color=renk, lw=1.4)

fig, ax = sekil(6, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, D), color=MAVI); ax.plot(*zip(B, E), color=YESIL); ax.plot(*zip(C, F), color=KIRMIZI)
for P, Q, n in ((B, D, 1), (D, C, 1), (C, E, 2), (E, A, 2), (A, F, 3), (F, B, 3)):
    centik(ax, P, Q, n)
nokta(ax, *A, "A", dx=-0.1, dy=0.2); nokta(ax, *B, "B", dx=-0.45, dy=-0.3); nokta(ax, *C, "C", dx=0.15, dy=-0.3)
nokta(ax, *D, "D", dx=-0.12, dy=-0.5); nokta(ax, *E, "E", dx=0.15, dy=0.1); nokta(ax, *F, "F", dx=-0.5, dy=0.05)
nokta(ax, *G, "G", dx=0.12, dy=0.15, renk=YAZI)
ax.text(2.55, 3.55, r"$V_a$", color=MAVI, fontsize=14)
ax.text(2.0, 1.15, r"$V_b$", color=YESIL, fontsize=14)
ax.text(4.6, 0.95, r"$V_c$", color=KIRMIZI, fontsize=14)
ax.set_xlim(-0.7, 7.6); ax.set_ylim(-0.8, 5.7)
kaydet(fig, __file__)
