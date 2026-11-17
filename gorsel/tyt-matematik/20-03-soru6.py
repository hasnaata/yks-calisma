import sys; sys.path.insert(0, "tools")
from cizim import *

# G ağırlık merkezi; [AD] ⊥ [BE]; |GD| = 3, |GE| = 4 → |AG| = 6, |BG| = 8, |AB| = 10.
G = np.array([0.0, 0.0]); A = np.array([-6.0, 0.0]); D = np.array([3.0, 0.0])
B = np.array([0.0, -8.0]); E = np.array([0.0, 4.0]); C = 2 * D - B
print("C", C, "E=(A+C)/2", (A + C) / 2, "G=(A+B+C)/3", (A + B + C) / 3, "AB", np.linalg.norm(A - B))

fig, ax = sekil(5, 5.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, D), color=MAVI); ax.plot(*zip(B, E), color=YESIL)
k = 0.5
ax.plot([k, k, 0], [0, k, k], color=YAZI, lw=1.3)
def centik(P1, Q1, n):
    M = (P1 + Q1) / 2; d = (Q1 - P1) / np.linalg.norm(Q1 - P1); m = np.array([-d[1], d[0]])
    for i in range(n):
        c = M + (i - (n - 1) / 2) * 0.3 * d
        ax.plot(*zip(c - 0.32 * m, c + 0.32 * m), color=SOLUK, lw=1.4)
for X, Y, n in ((B, D, 1), (D, C, 1), (A, E, 2), (E, C, 2)):
    centik(X, Y, n)
nokta(ax, *A, "A", dx=-0.9, dy=-0.2); nokta(ax, *B, "B", dx=-0.4, dy=-1.0); nokta(ax, *C, "C", dx=0.3, dy=0.2)
nokta(ax, *D, "D", dx=0.4, dy=-0.4, renk=MAVI); nokta(ax, *E, "E", dx=-0.8, dy=0.25, renk=YESIL)
nokta(ax, *G, "G", dx=-0.8, dy=-0.85)
ax.text(1.5, -0.45, "3", color=MAVI, fontsize=15, ha="center", va="top")
ax.text(0.45, 2.0, "4", color=YESIL, fontsize=15, va="center")
ax.set_xlim(-7.4, 7.2); ax.set_ylim(-9.4, 8.9)
kaydet(fig, __file__)
