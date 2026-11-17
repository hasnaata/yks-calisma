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

def centik(ax, P, Q, n=1, renk=SOLUK, L=0.18, ara=0.12):
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]]); M = (P + Q) / 2
    for k in range(n):
        c = M + (k - (n - 1) / 2) * ara * u
        ax.plot(*zip(c - L * v, c + L * v), color=renk, lw=1.6)

def olcu(ax, P, Q, metin, Gm, d=0.55, renk=SOLUK, yazi=YAZI, ek=0.4):
    """[PQ] boyunca, şeklin dışına doğru oklu ölçü çizgisi ve etiketi."""
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, (P + Q) / 2 - np.asarray(Gm)) < 0: v = -v
    ax.annotate("", xy=Q + d * v, xytext=P + d * v, arrowprops=dict(arrowstyle="<->", color=renk, lw=1.2))
    ax.text(*((P + Q) / 2 + (d + ek) * v), metin, ha="center", va="center", fontsize=13, color=yazi)

# Soru 10: kâğıt ABC, |AB|=7, |AC|=9, |BC|=10. B ile C çakışacak biçimde katlanır; katlama çizgisi [DF], D ∈ [AC].
# |DB|=|DC| -> Ç(ABD) = |AB| + |AD| + |DC| = |AB| + |AC| = 16.
A, B, C = ucgen(10, 9, 7)
F = (B + C) / 2
t = (F[0] - A[0]) / (C[0] - A[0]); D = A + t * (C - A)
print("t", t, "DB", uz(D, B), "DC", uz(D, C), "Ç(ABD)", uz(A, B) + uz(A, D) + uz(D, B))
Gm = (A + B + C) / 3

fig, ax = sekil(5.4, 3.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([A, B, D], color=MAVI_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, D), color=MAVI, lw=1.8)
ax.plot(*zip(D, F), color=KIRMIZI, lw=2, ls="--")
dik(ax, F, C, D, s=0.35, renk=KIRMIZI)
centik(ax, B, F, 1); centik(ax, F, C, 1)
nokta(ax, *A, "A", dx=-0.2, dy=0.3); nokta(ax, *B, "B", dx=-0.6, dy=-0.5); nokta(ax, *C, "C", dx=0.15, dy=-0.5)
nokta(ax, *D, "D", dx=0.2, dy=0.2, renk=KIRMIZI); nokta(ax, *F, "F", dx=-0.15, dy=-0.7, renk=KIRMIZI)
kenar(ax, A, B, "7", Gm, d=0.45)
olcu(ax, A, C, "9", Gm, d=0.55)
olcu(ax, B, C, "10", Gm, d=1.0)
ax.set_xlim(-0.9, 11.0); ax.set_ylim(-2.1, A[1] + 1.0)
kaydet(fig, __file__)
