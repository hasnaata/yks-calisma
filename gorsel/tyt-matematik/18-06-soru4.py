import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 4: |AB| = 4, |BC| = 9, |AD| = 3, |DC| = 10, |AC| = x (çizimde x = 10).
def nokta3(P, Q, r1, r2, ust):
    d = np.linalg.norm(Q - P); u = (Q - P) / d; n = np.array([-u[1], u[0]])
    a = (d * d + r1 * r1 - r2 * r2) / (2 * d); h = np.sqrt(r1 * r1 - a * a)
    return P + a * u + (h if ust else -h) * n
A = np.array([0.0, 0.0]); C = np.array([10.0, 0.0])
B = nokta3(A, C, 4, 9, True); D = nokta3(A, C, 3, 10, False)
print(B, D, np.linalg.norm(B - C), np.linalg.norm(D - C))

fig, ax = sekil(5.6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(A, C), color=KIRMIZI, lw=2.4, ls="--")
nokta(ax, *A, "A", dx=-0.6, dy=-0.1); nokta(ax, *B, "B", dx=-0.15, dy=0.25)
nokta(ax, *C, "C", dx=0.2, dy=-0.1); nokta(ax, *D, "D", dx=-0.2, dy=-0.6)
def yaz(P, Q, s, dx, dy, renk=YAZI):
    m = (P + Q) / 2; ax.text(m[0] + dx, m[1] + dy, s, ha="center", va="center", color=renk, fontsize=14)
yaz(A, B, "4", -0.4, 0.1); yaz(B, C, "9", 0.25, 0.35)
yaz(A, D, "3", -0.4, -0.1); yaz(D, C, "10", 0.45, -0.65)
yaz(A, C, "x", 0.6, 0.45, KIRMIZI)
ax.set_xlim(-1, 11); ax.set_ylim(D[1] - 0.9, B[1] + 0.8)
kaydet(fig, __file__)
