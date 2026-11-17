import sys; sys.path.insert(0, "tools")
from cizim import *

# A ortak açı (60°). |AB|=6, |AC|=8; D ∈ [AB], |AD|=4; E ∈ [AC], |AE|=3.
# ADE ~ ACB (oran 1/2), bu yüzden m(ADE) = m(ACB).
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def acisi(K, P, Q):
    u, v = P - K, Q - K; return np.degrees(np.arccos(u @ v / np.linalg.norm(u) / np.linalg.norm(v)))
def kenar(ax, P, Q, metin, d, renk=YAZI):
    M = (P + Q) / 2 + d; ax.text(*M, metin, ha="center", va="center", color=renk, fontsize=13)
A = np.array([0.0, 0.0]); u, v = yon(-118), yon(-58)
B, C = A + 6 * u, A + 8 * v; D, E = A + 4 * u, A + 3 * v
print("ADE", acisi(D, A, E), "ACB", acisi(C, A, B))
fig, ax = sekil(5, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(D, E), color=MAVI, lw=2.4)
aci(ax, A, B, C, r=0.6, renk=SOLUK)
aci(ax, D, A, E, r=0.55, renk=KIRMIZI); aci(ax, C, A, B, r=0.75, renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.15, dy=0.3); nokta(ax, *B, "B", dx=-0.6, dy=-0.3); nokta(ax, *C, "C", dx=0.25, dy=-0.3)
nokta(ax, *D, "D", dx=-0.65, dy=-0.05); nokta(ax, *E, "E", dx=0.25, dy=0.0)
n1 = yon(-118 - 90) * 0.45; n2 = yon(-58 + 90) * 0.45
kenar(ax, A, D, "4", n1); kenar(ax, D, B, "x", n1); kenar(ax, A, E, "3", n2); kenar(ax, E, C, "5", n2)
ax.set_xlim(B[0] - 1.0, C[0] + 1.0); ax.set_ylim(C[1] - 0.8, 0.9)
kaydet(fig, __file__)
