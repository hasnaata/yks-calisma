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

def dik(ax, K, P, Q, s=0.3, renk=SOLUK):
    """K köşesinde KP ile KQ arasındaki dik açı işareti."""
    u = (P - K) / np.linalg.norm(P - K) * s; v = (Q - K) / np.linalg.norm(Q - K) * s
    ax.plot(*zip(K + u, K + u + v, K + v), color=renk, lw=1.3)
def aci_olc(K, P, Q):
    u, v = P - K, Q - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)

# |AB|=9, |AC|=6, |BC|=5. A'daki dış açıortay BC uzantısını D'de keser: |DC|=10, |DB|=15.
# [AE] iç açıortay: |BE|=3, |EC|=2. m(EAD)=90.
A, B, C = ucgen(5, 6, 9)
D = np.array([15.0, 0.0]); E = np.array([3.0, 0.0])
P = A + 2.2 * (A - B) / np.linalg.norm(A - B)
print("AB", uz(A, B), "AC", uz(A, C), "DC", uz(D, C), "DB", uz(D, B), "PAD", aci_olc(A, P, D), "DAC", aci_olc(A, D, C), "EAD", aci_olc(A, E, D))
Gm = (A + B + C) / 3

fig, ax = sekil(6, 3.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(C, D), color=SOLUK, lw=1.6, ls="--")
ax.plot(*zip(A, P), color=SOLUK, lw=1.6, ls="--")
ax.plot(*zip(A, D), color=KIRMIZI, lw=2)
ax.plot(*zip(A, E), color=MAVI, lw=1.6, ls=(0, (4, 3)))
aci(ax, A, P, D, r=1.15, ad="β", renk=KIRMIZI); aci(ax, A, D, C, r=1.3, ad="β", renk=KIRMIZI)
dik(ax, A, E, D, s=0.4, renk=MAVI)
nokta(ax, *A, "A", dx=-0.55, dy=0.15); nokta(ax, *B, "B", dx=-0.6, dy=-0.6); nokta(ax, *C, "C", dx=0.15, dy=-0.7)
nokta(ax, *D, "D", dx=0.2, dy=-0.7, renk=KIRMIZI); nokta(ax, *E, "E", dx=-0.6, dy=0.2, renk=MAVI)
kenar(ax, A, B, "9", Gm, d=0.45); kenar(ax, A, C, "6", Gm, d=0.4)
for x0, x1, m, r in ((0, 5, "5", YAZI), (5, 15, "10", KIRMIZI)):
    ax.annotate("", xy=(x1, -1.15), xytext=(x0, -1.15), arrowprops=dict(arrowstyle="<->", color=r, lw=1.2))
    ax.text((x0 + x1) / 2, -1.25, m, ha="center", va="top", fontsize=13, color=r)
ax.set_xlim(-0.8, 15.6); ax.set_ylim(-2.0, P[1] + 0.3)
kaydet(fig, __file__)
