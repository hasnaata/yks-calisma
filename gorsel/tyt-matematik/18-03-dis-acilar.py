import sys; sys.path.insert(0, "tools")
from cizim import *

# m(A)=50, m(B)=60, m(C)=70. Kenarlar sırayla uzatılır: CA → A'nın ötesine, AB → B'nin ötesine, BC → C'nin ötesine.
B = np.array([0.0, 0.0]); C = np.array([6.0, 0.0])
t = 6 * np.sin(np.radians(70)) / np.sin(np.radians(50))
A = B + t * np.array([np.cos(np.radians(60)), np.sin(np.radians(60))])

def uzat(p, q, L):  # p'den q'ya giden doğrultuyu q'nun ötesine L kadar uzat
    u = (q - p) / np.linalg.norm(q - p); return q + L * u

fig, ax = sekil(6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI)
for p, q in ((C, A), (A, B), (B, C)):
    r = uzat(p, q, 1.6); ax.plot(*zip(q, r), color=SOLUK, lw=1.6, ls="--")
nokta(ax, *A, "A", dx=0.22, dy=0.0); nokta(ax, *B, "B", dx=-0.55, dy=0.0); nokta(ax, *C, "C", dx=0.05, dy=-0.5)
aci(ax, A, B, C, r=0.8, ad="50°", renk=MAVI)
aci(ax, B, C, A, r=0.6, ad="60°", renk=MAVI)
aci(ax, C, A, B, r=0.6, ad="70°", renk=MAVI)
aci(ax, A, uzat(C, A, 1), B, r=0.55, ad="130°", renk=KIRMIZI)
aci(ax, B, uzat(A, B, 1), C, r=0.55, ad="120°", renk=KIRMIZI)
aci(ax, C, uzat(B, C, 1), A, r=0.55, ad="110°", renk=KIRMIZI)
ax.set_xlim(-1.6, 8.0); ax.set_ylim(-1.6, A[1] + 1.7)
kaydet(fig, __file__)
