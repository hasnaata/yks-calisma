import sys; sys.path.insert(0, "tools")
from cizim import *

# ABC: m(A)=40, m(B)=m(C)=70. D içeride: m(ABD)=25, m(ACD)=30 → m(BDC)=95.
# [BD] uzatılıp [AC]'yi E'de keser: m(BEC)=65.
B = np.array([0.0, 0.0]); C = np.array([5.0, 0.0])
A = np.array([2.5, 2.5 * np.tan(np.radians(70))])
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
uB = yon(70 - 25)          # B'de BA yönü 70°, 25° içeri döner
uC = yon(180 - 70 + 30)    # C'de CA yönü 110°, 30° içeri döner
D = kesis(B, uB, C, uC)
E = kesis(B, uB, A, C - A)
print("BDC", np.degrees(np.arccos(np.dot(B - D, C - D) / np.linalg.norm(B - D) / np.linalg.norm(C - D))))

fig, ax = sekil(5, 5.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=CIZGI, lw=1.6)
ax.plot(*zip(A, B, D, C, A), color=YAZI)
ax.plot(*zip(D, E), color=SOLUK, lw=1.5, ls="--")
nokta(ax, *A, "A", dx=-0.1, dy=0.2); nokta(ax, *B, "B", dx=-0.4, dy=-0.3); nokta(ax, *C, "C", dx=0.12, dy=-0.3)
nokta(ax, *D, "D", dx=-0.45, dy=0.12); nokta(ax, *E, "E", dx=0.15, dy=0.05, renk=SOLUK)
aci(ax, A, B, C, r=0.8, ad="40°", renk=MAVI)
aci(ax, B, D, A, r=1.0, ad="25°", renk=YESIL)
aci(ax, C, A, D, r=1.0, ad="30°", renk=SARI)
aci(ax, D, C, B, r=0.4, ad="95°", renk=KIRMIZI)
aci(ax, E, C, B, r=0.35, ad="", renk=SOLUK)
ax.text(E[0] - 0.05, E[1] - 0.75, "65°", color=SOLUK, fontsize=12, ha="center")
ax.set_xlim(-0.7, 5.7); ax.set_ylim(-0.6, A[1] + 0.6)
kaydet(fig, __file__)
