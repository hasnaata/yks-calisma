import sys; sys.path.insert(0, "tools")
from cizim import *

# K.K.K.: ABC kenarları 4, 6, 7; KLM kenarları 8, 12, 14 (her biri 2 katı).
def ucgen(B, a, b, c, k=1.0):
    a, b, c = a * k, b * k, c * k
    x = (c**2 - b**2 + a**2) / (2 * a); y = np.sqrt(c**2 - x**2)
    return B + np.array([x, y]), B, B + np.array([a, 0.0])
def kenar(ax, P, Q, metin, G, d=0.55, renk=YAZI):
    M = (P + Q) / 2; n = M - G; n = n / np.linalg.norm(n)
    ax.text(*(M + d * n), metin, ha="center", va="center", color=renk, fontsize=13)
# |BC|=7, |AC|=6, |AB|=4
A, B, C = ucgen(np.array([0.0, 0.0]), 7, 6, 4)
K, L, M = ucgen(np.array([10.0, 0.0]), 7, 6, 4, 2)
print(np.linalg.norm(K - L), np.linalg.norm(L - M), np.linalg.norm(K - M))
fig, ax = sekil(6, 3.0)
ax.set_aspect("equal"); ax.axis("off")
for P, Q, R in ((A, B, C), (K, L, M)):
    ax.plot(*zip(P, Q, R, P), color=YAZI)
G1, G2 = (A + B + C) / 3, (K + L + M) / 3
nokta(ax, *A, "A", dx=-0.2, dy=0.3); nokta(ax, *B, "B", dx=-0.85, dy=-0.25); nokta(ax, *C, "C", dx=0.3, dy=-0.25)
nokta(ax, *K, "K", dx=-0.2, dy=0.3); nokta(ax, *L, "L", dx=-0.85, dy=-0.25); nokta(ax, *M, "M", dx=0.3, dy=-0.25)
kenar(ax, A, B, "4", G1, renk=YESIL); kenar(ax, A, C, "6", G1, d=0.7, renk=MAVI); kenar(ax, B, C, "7", G1, renk=KIRMIZI)
kenar(ax, K, L, "8", G2, renk=YESIL); kenar(ax, K, M, "12", G2, d=0.8, renk=MAVI); kenar(ax, L, M, "14", G2, renk=KIRMIZI)
aci(ax, A, B, C, r=0.6, renk=KIRMIZI); aci(ax, K, L, M, r=0.9, renk=KIRMIZI)
ax.set_xlim(-1.1, 25.2); ax.set_ylim(-1.0, K[1] + 0.9)
kaydet(fig, __file__)
