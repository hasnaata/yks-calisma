import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders, kural 2: m(B)=m(C)=65, m(A)=50 => |AB|=|AC|.
B = np.array([0.0, 0.0]); C = np.array([4.0, 0.0])
A = np.array([2.0, 2.0 * np.tan(np.radians(65))])
print("AB", np.linalg.norm(A - B), "AC", np.linalg.norm(A - C), "BC", 4.0)
u, v = B - A, C - A
print("A", np.degrees(np.arccos(u @ v / np.linalg.norm(u) / np.linalg.norm(v))))

fig, ax = sekil(4.4, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
def centik(P, Q, renk=MAVI):
    m = (P + Q) / 2; d = (Q - P) / np.linalg.norm(Q - P); n = np.array([-d[1], d[0]])
    ax.plot(*zip(m - 0.2 * n, m + 0.2 * n), color=renk, lw=2.4)
centik(A, B); centik(A, C)
nokta(ax, *A, "A", dx=-0.12, dy=0.22); nokta(ax, *B, "B", dx=-0.4, dy=-0.15); nokta(ax, *C, "C", dx=0.15, dy=-0.15)
aci(ax, A, B, C, r=0.6, ad="50°", renk=SOLUK)
aci(ax, B, A, C, r=0.6, ad="65°", renk=KIRMIZI)
aci(ax, C, A, B, r=0.6, ad="65°", renk=KIRMIZI)
ax.set_xlim(-1.2, 5.2); ax.set_ylim(-0.6, A[1] + 0.6)
kaydet(fig, __file__)
