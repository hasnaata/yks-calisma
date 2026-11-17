import sys; sys.path.insert(0, "tools")
from cizim import *

# Kenarortaylar |AD| = 12, |BE| = 9 (üçüncüsü 10) olacak biçimde gerçek ölçülü üçgen.
ma, mb, mc = 12, 9, 10
a = 2 / 3 * np.sqrt(2 * mb**2 + 2 * mc**2 - ma**2)
b = 2 / 3 * np.sqrt(2 * ma**2 + 2 * mc**2 - mb**2)
c = 2 / 3 * np.sqrt(2 * ma**2 + 2 * mb**2 - mc**2)
B = np.array([0.0, 0.0]); C = np.array([a, 0.0])
x = (c**2 - b**2 + a**2) / (2 * a); A = np.array([x, np.sqrt(c**2 - x**2)])
D, E, F = (B + C) / 2, (A + C) / 2, (A + B) / 2
G = (A + B + C) / 3
L = lambda P, Q: np.linalg.norm(P - Q)
print("AD", L(A, D), "AG", L(A, G), "GD", L(G, D), "BE", L(B, E), "BG", L(B, G), "GE", L(G, E))

def etiket(P, Q, t, renk, d=0.45, yan=1):
    M = (P + Q) / 2; u = (Q - P) / L(P, Q); v = yan * np.array([-u[1], u[0]])
    ax.text(*(M + d * v), t, color=renk, fontsize=14, ha="center", va="center")

fig, ax = sekil(6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(C, F), color=CIZGI, lw=1.6, ls="--")
ax.plot(*zip(A, D), color=MAVI); ax.plot(*zip(B, E), color=YESIL)
nokta(ax, *A, "A", dx=-0.2, dy=0.3); nokta(ax, *B, "B", dx=-0.7, dy=-0.4); nokta(ax, *C, "C", dx=0.2, dy=-0.4)
nokta(ax, *D, "D", dx=-0.2, dy=-0.8, renk=MAVI); nokta(ax, *E, "E", dx=0.25, dy=0.05, renk=YESIL)
nokta(ax, *G, "G", dx=0.3, dy=-0.55)
etiket(A, G, "8", MAVI, yan=1); etiket(G, D, "4", MAVI, yan=1)
etiket(B, G, "6", YESIL, yan=1); etiket(G, E, "3", YESIL, yan=1)
ax.set_xlim(-1.0, a + 0.8); ax.set_ylim(-1.2, A[1] + 0.9)
kaydet(fig, __file__)
