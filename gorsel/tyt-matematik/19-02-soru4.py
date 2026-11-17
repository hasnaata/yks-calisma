import sys; sys.path.insert(0, "tools")
from cizim import *

# |AB|=8 (|AD|=6, |DB|=2), |AC|=12 (|AE|=4, |EC|=8). AED ~ ABC (oran 1/2) → m(AED) = m(ABC).
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def acisi(K, P, Q):
    u, v = P - K, Q - K; return np.degrees(np.arccos(u @ v / np.linalg.norm(u) / np.linalg.norm(v)))
def kenar(ax, P, Q, metin, d, renk=YAZI):
    ax.text(*((P + Q) / 2 + d), metin, ha="center", va="center", color=renk, fontsize=13)
A = np.array([0.0, 0.0]); u, v = yon(-115), yon(-60)
B, C = A + 8 * u, A + 12 * v; D, E = A + 6 * u, A + 4 * v
print("AED", acisi(E, A, D), "ABC", acisi(B, A, C))
fig, ax = sekil(5, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(D, E), color=MAVI, lw=2.4)
aci(ax, E, A, D, r=0.7, renk=KIRMIZI); aci(ax, B, A, C, r=0.8, renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.2, dy=0.35); nokta(ax, *B, "B", dx=-0.8, dy=-0.35); nokta(ax, *C, "C", dx=0.3, dy=-0.35)
nokta(ax, *D, "D", dx=-0.8, dy=-0.1); nokta(ax, *E, "E", dx=0.3, dy=0.0)
n1 = yon(-115 - 90) * 0.55; n2 = yon(-60 + 90) * 0.55
kenar(ax, A, D, "6", n1); kenar(ax, D, B, "2", n1); kenar(ax, A, E, "4", n2); kenar(ax, E, C, "x", n2)
ax.set_xlim(B[0] - 1.2, C[0] + 1.2); ax.set_ylim(C[1] - 1.0, 1.0)
kaydet(fig, __file__)
