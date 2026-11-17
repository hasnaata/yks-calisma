import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders, örnek 5: |AC| = b = 8, |AB| = c = 5, m(A) > m(B) olduğundan a > 8. Çizimde a = |BC| = 10.
B = np.array([0.0, 0.0]); C = np.array([10.0, 0.0])
x = (10**2 + 5**2 - 8**2) / 20; A = np.array([x, np.sqrt(25 - x * x)])
def acisi(P, Q, R):
    u, v = Q - P, R - P; return np.degrees(np.arccos(u @ v / np.linalg.norm(u) / np.linalg.norm(v)))
print("AB", np.linalg.norm(A - B), "AC", np.linalg.norm(A - C), "A", acisi(A, B, C), "B", acisi(B, A, C))

fig, ax = sekil(5.6, 3.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, C), color=KIRMIZI, lw=3)
aci(ax, A, B, C, r=0.7, renk=KIRMIZI)
aci(ax, B, A, C, r=1.1, renk=MAVI)
nokta(ax, *A, "A", dx=-0.2, dy=0.3); nokta(ax, *B, "B", dx=-0.65, dy=-0.2); nokta(ax, *C, "C", dx=0.25, dy=-0.2)
ax.text(*(A / 2 + np.array([-0.45, 0.2])), "5", ha="center", fontsize=14)
ax.text(*((A + C) / 2 + np.array([0.35, 0.25])), "8", ha="center", fontsize=14)
ax.text(5, -0.35, "a > 8", ha="center", va="top", color=KIRMIZI, fontsize=14, fontweight="bold")
ax.text(A[0] + 0.15, A[1] - 1.45, "büyük açı", color=KIRMIZI, fontsize=11, ha="center")
ax.text(1.75, 0.18, "küçük", color=MAVI, fontsize=11)
ax.set_xlim(-1, 11); ax.set_ylim(-1.2, A[1] + 0.9)
kaydet(fig, __file__)
