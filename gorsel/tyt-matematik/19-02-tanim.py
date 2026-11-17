import sys; sys.path.insert(0, "tools")
from cizim import *

# ABC ~ DEF, k = 3/2. ABC: |AB|=4, |BC|=6, |AC|=5. DEF her kenarı 1,5 katı: 6, 9, 7,5.
def ucgen(B, a, b, c, k=1.0):
    """B köşesi, |BC|=a, |AC|=b, |AB|=c, k katına büyütülmüş."""
    a, b, c = a * k, b * k, c * k
    x = (c**2 - b**2 + a**2) / (2 * a); y = np.sqrt(c**2 - x**2)
    return B + np.array([x, y]), B, B + np.array([a, 0.0])
def kenar(ax, P, Q, metin, G, d=0.45, renk=YAZI):
    M = (P + Q) / 2; n = M - G; n = n / np.linalg.norm(n)
    ax.text(*(M + d * n), metin, ha="center", va="center", color=renk, fontsize=13)

A, B, C = ucgen(np.array([0.0, 0.0]), 6, 5, 4)
D, E, F = ucgen(np.array([8.0, 0.0]), 6, 5, 4, 1.5)
print(np.linalg.norm(D - E), np.linalg.norm(E - F), np.linalg.norm(D - F))
fig, ax = sekil(6, 2.8)
ax.set_aspect("equal"); ax.axis("off")
for P, Q, R in ((A, B, C), (D, E, F)):
    ax.plot(*zip(P, Q, R, P), color=YAZI)
for (P, Q, R), (r1, r2) in (((A, B, C), (0.55, 0.6)), ((D, E, F), (0.75, 0.85))):
    aci(ax, P, Q, R, r=r1, renk=MAVI); aci(ax, Q, R, P, r=r2, renk=KIRMIZI); aci(ax, R, P, Q, r=r2, renk=YESIL)
G1 = (A + B + C) / 3; G2 = (D + E + F) / 3
nokta(ax, *A, "A", dx=-0.15, dy=0.25); nokta(ax, *B, "B", dx=-0.75, dy=-0.25); nokta(ax, *C, "C", dx=0.25, dy=-0.25)
nokta(ax, *D, "D", dx=-0.15, dy=0.25); nokta(ax, *E, "E", dx=-0.75, dy=-0.25); nokta(ax, *F, "F", dx=0.25, dy=-0.25)
kenar(ax, A, B, "4", G1); kenar(ax, B, C, "6", G1); kenar(ax, A, C, "5", G1)
kenar(ax, D, E, "6", G2); kenar(ax, E, F, "9", G2); kenar(ax, D, F, "7,5", G2, d=0.6)
ax.set_xlim(-1.0, 18.0); ax.set_ylim(-0.8, D[1] + 0.8)
kaydet(fig, __file__)
