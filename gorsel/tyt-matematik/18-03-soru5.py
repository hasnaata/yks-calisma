import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 5: m(BAC)=x=50, m(ABD)=30, m(ACD)=35, m(BDC)=115. Büyük üçgen: m(B)=m(C)=65.
B = np.array([0.0, 0.0]); C = np.array([5.0, 0.0])
A = np.array([2.5, 2.5 * np.tan(np.radians(65))])
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
D = kesis(B, yon(65 - 30), C, yon(115 + 35))
print("BDC", np.degrees(np.arccos(np.dot(B - D, C - D) / np.linalg.norm(B - D) / np.linalg.norm(C - D))))

fig, ax = sekil(5, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, D, C, A), color=YAZI)
nokta(ax, *A, "A", dx=-0.1, dy=0.2); nokta(ax, *B, "B", dx=-0.4, dy=-0.3); nokta(ax, *C, "C", dx=0.12, dy=-0.3)
nokta(ax, *D, "D", dx=-0.12, dy=0.22)
aci(ax, A, B, C, r=0.7, ad="x", renk=MAVI)
aci(ax, B, D, A, r=1.0, ad="30°", renk=YESIL)
aci(ax, C, A, D, r=1.0, ad="35°", renk=SARI)
aci(ax, D, C, B, r=0.4, ad="115°", renk=KIRMIZI)
ax.set_xlim(-0.7, 5.7); ax.set_ylim(-0.6, A[1] + 0.6)
kaydet(fig, __file__)
