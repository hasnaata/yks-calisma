import sys; sys.path.insert(0, "tools")
from cizim import *

# ABC ~ DEF, k = 3/2. ABC: |BC|=8, A'dan yükseklik 3, çevre 18 (|AB|=|AC|=5).
# DEF: |EF|=12, yükseklik 4,5, çevre 27.
def ucgen(B, k):
    return B + k * np.array([4.0, 3.0]), B, B + np.array([8.0 * k, 0.0])
A, B, C = ucgen(np.array([0.0, 0.0]), 1); D, E, F = ucgen(np.array([11.0, 0.0]), 1.5)
for P, Q, R in ((A, B, C), (D, E, F)):
    print("çevre", np.linalg.norm(P - Q) + np.linalg.norm(Q - R) + np.linalg.norm(P - R), "yükseklik", P[1])
fig, ax = sekil(6, 3.2)
ax.set_aspect("equal"); ax.axis("off")
for (P, Q, R), h, taban in (((A, B, C), "3", "8"), ((D, E, F), "?", "12")):
    ax.plot(*zip(P, Q, R, P), color=YAZI)
    H = np.array([P[0], 0.0])
    ax.plot(*zip(P, H), color=MAVI, lw=1.8, ls="--")
    s = 0.4; ax.plot([H[0], H[0] + s, H[0] + s], [s, s, 0], color=MAVI, lw=1.2)
    ax.text(P[0] - 0.25, P[1] / 2, h, color=MAVI, ha="right", va="center", fontsize=13)
    ax.text((Q[0] + R[0]) / 2 + 0.9, -0.6, taban, ha="center", va="center", fontsize=13)
nokta(ax, *A, "A", dx=-0.65, dy=0.2); nokta(ax, *B, "B", dx=-0.85, dy=-0.25); nokta(ax, *C, "C", dx=0.3, dy=-0.25)
nokta(ax, *D, "D", dx=-0.65, dy=0.2); nokta(ax, *E, "E", dx=-0.85, dy=-0.25); nokta(ax, *F, "F", dx=0.3, dy=-0.25)
ax.text(A[0] - 0.45, 0.4, "H", color=MAVI, ha="center", va="center", fontsize=12)
ax.text(D[0] - 0.45, 0.4, "K", color=MAVI, ha="center", va="center", fontsize=12)
ax.set_xlim(-1.1, 24.0); ax.set_ylim(-1.1, D[1] + 0.9)
kaydet(fig, __file__)
