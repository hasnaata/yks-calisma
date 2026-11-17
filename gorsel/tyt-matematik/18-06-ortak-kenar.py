import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders, kural 2: |AB| = 5, |AD| = 8, |BC| = 6, |CD| = 12, |BD| = x (çizimde x = 10).
def nokta3(P, Q, r1, r2, ust):
    d = np.linalg.norm(Q - P); u = (Q - P) / d; n = np.array([-u[1], u[0]])
    a = (d * d + r1 * r1 - r2 * r2) / (2 * d); h = np.sqrt(r1 * r1 - a * a)
    return P + a * u + (h if ust else -h) * n
B = np.array([0.0, 0.0]); D = np.array([10.0, 0.0])
A = nokta3(B, D, 5, 8, True); C = nokta3(B, D, 6, 12, False)
print(np.linalg.norm(A - B), np.linalg.norm(A - D), np.linalg.norm(C - B), np.linalg.norm(C - D))

fig, ax = sekil(5.6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, D], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
ax.add_patch(patches.Polygon([C, B, D], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(B, D), color=KIRMIZI, lw=2.6, ls="--")
nokta(ax, *A, "A", dx=-0.15, dy=0.25); nokta(ax, *B, "B", dx=-0.55, dy=-0.1)
nokta(ax, *C, "C", dx=-0.2, dy=-0.6); nokta(ax, *D, "D", dx=0.2, dy=-0.1)
def yaz(P, Q, s, dx, dy, renk=YAZI):
    m = (P + Q) / 2; ax.text(m[0] + dx, m[1] + dy, s, ha="center", va="center", color=renk, fontsize=14)
yaz(A, B, "5", -0.35, 0.15); yaz(A, D, "8", 0.25, 0.35)
yaz(B, C, "6", -0.4, -0.15); yaz(C, D, "12", 0.55, -0.6)
yaz(B, D, "x", 0, 0.5, KIRMIZI)
ax.set_xlim(-1, 11); ax.set_ylim(C[1] - 0.9, A[1] + 0.8)
kaydet(fig, __file__)
