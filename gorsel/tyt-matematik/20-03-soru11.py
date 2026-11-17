import sys; sys.path.insert(0, "tools")
from cizim import *

# m(B) = 90°, |AC| = 24 (kenarlar 14,4 - 19,2 - 24). E: [AC] orta, D: [BC] orta; AD ∩ BE = G.
B = np.array([0.0, 0.0]); A = np.array([0.0, 14.4]); C = np.array([19.2, 0.0])
E, D = (A + C) / 2, (B + C) / 2; G = (A + B + C) / 3
L = lambda X, Y: np.linalg.norm(X - Y)
print("AC", L(A, C), "BE", L(B, E), "BG", L(B, G), "GE", L(G, E))

def centik(P1, Q1, n):
    M = (P1 + Q1) / 2; d = (Q1 - P1) / L(P1, Q1); m = np.array([-d[1], d[0]])
    for i in range(n):
        c = M + (i - (n - 1) / 2) * 0.35 * d
        ax.plot(*zip(c - 0.4 * m, c + 0.4 * m), color=SOLUK, lw=1.4)

fig, ax = sekil(6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, D), color=MAVI); ax.plot(*zip(B, E), color=YESIL)
k = 0.9
ax.plot([k, k, 0], [0, k, k], color=YAZI, lw=1.3)
for X, Y, n in ((A, E, 2), (E, C, 2), (B, D, 1), (D, C, 1)):
    centik(X, Y, n)
nokta(ax, *A, "A", dx=-0.6, dy=0.5); nokta(ax, *B, "B", dx=-1.3, dy=-1.0); nokta(ax, *C, "C", dx=0.4, dy=-1.0)
nokta(ax, *E, "E", dx=0.1, dy=-1.7, renk=YESIL); nokta(ax, *D, "D", dx=-0.4, dy=-1.6, renk=MAVI)
nokta(ax, *G, "G", dx=-0.3, dy=0.7)
n = np.array([0.6, 0.8]) * 1.3  # [AC]'ye dik, dışa doğru: |AC| ölçü çizgisi
ax.annotate("", xy=C + n, xytext=A + n, arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
M = (A + C) / 2 + n * 1.75
ax.text(*M, "24", fontsize=15, ha="center", va="center")
ax.set_xlim(-1.8, 21.6); ax.set_ylim(-2.0, 16.6)
kaydet(fig, __file__)
