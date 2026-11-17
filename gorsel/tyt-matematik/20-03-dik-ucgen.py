import sys; sys.path.insert(0, "tools")
from cizim import *

# m(B) = 90°, |AB| = 6, |BC| = 8, |AC| = 10; E, [AC]'nin orta noktası: |BE| = |AE| = |EC| = 5.
B = np.array([0.0, 0.0]); A = np.array([0.0, 6.0]); C = np.array([8.0, 0.0]); E = (A + C) / 2
L = lambda X, Y: np.linalg.norm(X - Y)
print("BE", L(B, E), "AE", L(A, E), "EC", L(E, C))

def centik(P1, Q1, renk):
    M = (P1 + Q1) / 2; u = (Q1 - P1) / L(P1, Q1); v = np.array([-u[1], u[0]])
    ax.plot(*zip(M - 0.2 * v, M + 0.2 * v), color=renk, lw=1.6)

fig, ax = sekil(6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, E), color=YESIL)
k = 0.45
ax.plot([k, k, 0], [0, k, k], color=YAZI, lw=1.3)
for X, Y in ((A, E), (E, C), (B, E)):
    centik(X, Y, YESIL)
nokta(ax, *A, "A", dx=-0.3, dy=0.3); nokta(ax, *B, "B", dx=-0.6, dy=-0.5); nokta(ax, *C, "C", dx=0.2, dy=-0.5)
nokta(ax, *E, "E", dx=0.2, dy=0.25, renk=YESIL)
ax.text(-0.6, 3.0, "6", fontsize=15, ha="center", va="center")
ax.text(4.0, -0.55, "8", fontsize=15, ha="center", va="center")
ax.text(2.2, 5.0, "5", color=YESIL, fontsize=15, ha="center", va="center")
ax.text(6.4, 1.9, "5", color=YESIL, fontsize=15, ha="center", va="center")
ax.text(2.4, 1.05, "5", color=YESIL, fontsize=15, ha="center", va="center")
ax.set_xlim(-1.1, 8.7); ax.set_ylim(-1.0, 6.7)
kaydet(fig, __file__)
