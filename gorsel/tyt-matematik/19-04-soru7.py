import sys; sys.path.insert(0, "tools")
from cizim import *

# A biçimli merdiven: |TA| = |TB| = 3 m, |AB| = 1,8 m. |TD| = |TE| = 1 m, [DE] // [AB], |DE| = 0,6 m.
A = np.array([-0.9, 0.0]); B = np.array([0.9, 0.0]); T = np.array([0.0, np.sqrt(9 - 0.81)])
D = T + (A - T) / 3; E = T + (B - T) / 3
print("TA", np.linalg.norm(T - A), "DE", np.linalg.norm(E - D))
fig, ax = sekil(3.6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-1.6, 1.6], [0, 0], color=SOLUK, lw=1.2)
ax.plot(*zip(A, T, B), color=YAZI, lw=3.5)
ax.plot(*zip(D, E), color=MAVI, lw=3)
nokta(ax, *T, "T", dx=-0.08, dy=0.12); nokta(ax, *A, "A", dx=-0.25, dy=-0.25); nokta(ax, *B, "B", dx=0.1, dy=-0.25)
nokta(ax, *D, "D", dx=-0.3, dy=-0.05); nokta(ax, *E, "E", dx=0.12, dy=-0.05)
def kenar(P, Q, t, yon):
    M = (P + Q) / 2; ax.text(M[0] + yon, M[1], t, ha="right" if yon < 0 else "left", va="center", fontsize=12)
kenar(T, D, "1 m", -0.12); kenar(D, A, "2 m", -0.12); kenar(T, E, "1 m", 0.12); kenar(E, B, "2 m", 0.12)
ax.text(0, D[1] + 0.12, "?", ha="center", va="bottom", color=MAVI, fontsize=14)
ax.text(0, -0.25, "1,8 m", ha="center", va="center", fontsize=12)
ax.set_xlim(-1.7, 1.7); ax.set_ylim(-0.45, 3.2)
kaydet(fig, __file__)
