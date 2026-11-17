import sys; sys.path.insert(0, "tools")
from cizim import *

# [AB] // [CD]. [BC] iki paraleli birleştirir; m(ABC) = m(BCD) = 40° (iç ters açılar).
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
h = 3.0
B = np.array([4.0, h]); A = np.array([-0.6, h])
C = B + h / np.sin(np.radians(40)) * yon(220); D = np.array([5.0, 0.0])
fig, ax = sekil(6, 4.0)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B), color=YAZI); ax.plot(*zip(B, C), color=YAZI); ax.plot(*zip(C, D), color=YAZI)
ax.plot((A[0] + B[0]) / 2, h, ">", color=YAZI, markersize=7); ax.plot((C[0] + D[0]) / 2, 0, ">", color=YAZI, markersize=7)
nokta(ax, *A, "A", dx=-0.2, dy=0.2); nokta(ax, *B, "B", dx=0.0, dy=0.2)
nokta(ax, *C, "C", dx=-0.25, dy=-0.55); nokta(ax, *D, "D", dx=-0.1, dy=-0.55)
aci(ax, B, A, C, r=1.0, ad="40°", renk=MAVI)
aci(ax, C, D, B, r=1.0, ad="x", renk=MAVI)
ax.set_xlim(-1.2, 5.6); ax.set_ylim(-0.9, h + 0.8)
kaydet(fig, __file__)
