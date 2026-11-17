import sys; sys.path.insert(0, "tools")
from cizim import *

# ABC üçgeni: m(A)=70, m(B)=45, m(C)=65. A'dan BC'ye paralel d doğrusu.
B = np.array([0.0, 0.0]); C = np.array([6.0, 0.0])
tB, tC = np.radians(45), np.radians(65)
# A: B'den 45°, C'den 180-65 yönünde
t = 6 * np.sin(tC) / np.sin(np.radians(70))
A = B + t * np.array([np.cos(tB), np.sin(tB)])

fig, ax = sekil(6, 4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot([A[0] - 3.2, A[0] + 3.2], [A[1], A[1]], color=SOLUK, lw=1.6, ls="--")
ax.text(A[0] + 3.25, A[1] + 0.12, "d", color=SOLUK)
nokta(ax, *A, "A", dx=-0.12, dy=0.22); nokta(ax, *B, "B", dx=-0.4, dy=-0.35); nokta(ax, *C, "C", dx=0.12, dy=-0.35)
aci(ax, B, C, A, r=0.7, ad="45°", renk=MAVI)
aci(ax, C, A, B, r=0.7, ad="65°", renk=YESIL)
aci(ax, A, B, C, r=0.5, ad="70°", renk=KIRMIZI)
# d üzerindeki iç ters açılar
aci(ax, A, A + np.array([-1, 0]), B, r=0.85, ad="45°", renk=MAVI)
aci(ax, A, C, A + np.array([1, 0]), r=0.85, ad="65°", renk=YESIL)
ax.set_xlim(-0.8, 7.2); ax.set_ylim(-0.7, A[1] + 0.6)
kaydet(fig, __file__)
