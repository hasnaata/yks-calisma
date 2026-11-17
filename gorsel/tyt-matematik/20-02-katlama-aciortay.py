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

# Kâğıt ABC: |AB|=6, |AC|=8, |BC|=10 (A dik). [BA], [BC] üzerine katlanır; A, A' noktasına düşer.
# Katlama çizgisi [BD], B'nin açıortayı: |AD|/|DC| = 6/10 -> |AD|=3, |DC|=5. |BA'|=6, |A'C|=4, |A'D|=3.
A, B, C = ucgen(10, 8, 6)
A1 = np.array([6.0, 0.0]); D = A + (C - A) * 3 / 8
print("AD", uz(A, D), "DC", uz(D, C), "A'D", uz(A1, D), "A'C", uz(A1, C), "A", aci_olc(A, B, C), "A'", aci_olc(A1, B, D), "ABD", aci_olc(B, A, D), "DBC", aci_olc(B, D, C))
Gm = (A + B + C) / 3

fig, ax = sekil(5.8, 3.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([A, B, D], color=MAVI_ACIK, lw=0))
ax.add_patch(plt.Polygon([A1, B, D], color=SARI_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A1, D), color=SARI, lw=1.8)
ax.plot(*zip(B, D), color=KIRMIZI, lw=2, ls="--")
dik(ax, A, B, C, s=0.4); dik(ax, A1, C, D, s=0.4, renk=SARI)
aci(ax, B, A1, D, r=1.2, renk=KIRMIZI); aci(ax, B, D, A, r=1.4, renk=KIRMIZI)
ax.annotate("", xy=A1 + np.array([-0.5, 0.3]), xytext=A + np.array([0.15, -0.65]),
            arrowprops=dict(arrowstyle="->", color=SARI, lw=1.5, connectionstyle="arc3,rad=0.25"))
nokta(ax, *A, "A", dx=-0.25, dy=0.25); nokta(ax, *B, "B", dx=-0.55, dy=-0.5); nokta(ax, *C, "C", dx=0.15, dy=-0.5)
nokta(ax, *D, "D", dx=0.2, dy=0.2, renk=KIRMIZI); nokta(ax, *A1, "A'", dx=-0.2, dy=-0.65, renk=SARI)
kenar(ax, A, B, "6", Gm, d=0.4); kenar(ax, A, D, "3", Gm, d=0.4); kenar(ax, D, C, "5", Gm, d=0.4)
kenar(ax, B, A1, "6", Gm, d=0.45); kenar(ax, A1, C, "4", Gm, d=0.45)
ax.text(*((A1 + D) / 2 + np.array([0.3, 0.0])), "3", color=SARI, fontsize=13, ha="center", va="center")
ax.set_xlim(-0.8, 10.6); ax.set_ylim(-0.9, A[1] + 0.6)
kaydet(fig, __file__)
