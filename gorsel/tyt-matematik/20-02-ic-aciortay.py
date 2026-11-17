import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P) - np.asarray(Q))), 3)
def ucgen(a, b, c):
    """|BC|=a, |CA|=b, |AB|=c. B orijinde, C x ekseninde."""
    x = (c**2 - b**2 + a**2) / (2 * a)
    return np.array([x, np.sqrt(c**2 - x**2)]), np.array([0.0, 0.0]), np.array([float(a), 0.0])
def kenar(ax, P, Q, metin, G, d=0.45, renk=YAZI, fs=13):
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik_ayak(P, Q, R):
    """R noktasından PQ doğrusuna inen dikmenin ayağı."""
    u = (Q - P) / np.linalg.norm(Q - P); return P + np.dot(R - P, u) * u

# |AB|=6, |AC|=9, |BC|=10. [AD] iç açıortay: |BD|=4, |DC|=6.
A, B, C = ucgen(10, 9, 6)
D = B + (C - B) * 6 / 15
H1, H2 = dik_ayak(A, B, D), dik_ayak(A, C, D)
print("AB", uz(A, B), "AC", uz(A, C), "BD", uz(B, D), "DC", uz(D, C), "h1", uz(D, H1), "h2", uz(D, H2))
G = (A + B + C) / 3

fig, ax = sekil(5.6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([A, B, D], color=MAVI_ACIK, lw=0))
ax.add_patch(plt.Polygon([A, D, C], color=YESIL_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, D), color=KIRMIZI, lw=2)
ax.plot(*zip(D, H1), color=SOLUK, lw=1.4, ls="--"); ax.plot(*zip(D, H2), color=SOLUK, lw=1.4, ls="--")
aci(ax, A, B, D, r=0.9, ad="α", renk=KIRMIZI); aci(ax, A, D, C, r=1.1, ad="α", renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.15, dy=0.25); nokta(ax, *B, "B", dx=-0.5, dy=-0.45); nokta(ax, *C, "C", dx=0.15, dy=-0.45)
nokta(ax, *D, "D", dx=-0.15, dy=-0.6, renk=KIRMIZI)
kenar(ax, A, B, "6", G, d=0.4); kenar(ax, A, C, "9", G, d=0.4)
kenar(ax, B, D, "4", G, d=0.45, renk=MAVI); kenar(ax, D, C, "6", G, d=0.45, renk=YESIL)
ax.text(*((D + H1) / 2 + np.array([0.05, 0.28])), "h", color=SOLUK, fontsize=12, ha="center")
ax.text(*((D + H2) / 2 + np.array([-0.05, 0.3])), "h", color=SOLUK, fontsize=12, ha="center")
ax.set_xlim(-0.8, 10.6); ax.set_ylim(-0.9, A[1] + 0.6)
kaydet(fig, __file__)
