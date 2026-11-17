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

# Kâğıt ABC: |AB|=5, |AC|=8, |BC|=9. B ile C çakışacak biçimde katlanır; katlama çizgisi [DF].
# F, [BC]'nin orta noktası; [DF] ⟂ [BC]; |DB|=|DC|. Ç(ABD) = |AB| + |AC| = 13.
A, B, C = ucgen(9, 8, 5)
F = (B + C) / 2
t = (F[0] - A[0]) / (C[0] - A[0]); D = A + t * (C - A)
print("DB", uz(D, B), "DC", uz(D, C), "AD", uz(A, D), "Ç(ABD)", uz(A, B) + uz(A, D) + uz(D, B), "t", t)
Gm = (A + B + C) / 3

fig, ax = sekil(5.4, 3.2)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([A, B, D], color=MAVI_ACIK, lw=0))
ax.add_patch(plt.Polygon([B, D, C], color=SARI_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, D), color=SARI, lw=1.8)
ax.plot(*zip(D, F), color=KIRMIZI, lw=2, ls="--")
dik(ax, F, C, D, s=0.35, renk=KIRMIZI)
centik(ax, B, F, 1); centik(ax, F, C, 1)
centik(ax, B, D, 2, renk=SARI); centik(ax, D, C, 2, renk=SARI)
nokta(ax, *A, "A", dx=-0.2, dy=0.25); nokta(ax, *B, "B", dx=-0.55, dy=-0.5); nokta(ax, *C, "C", dx=0.15, dy=-0.5)
nokta(ax, *D, "D", dx=0.15, dy=0.2, renk=KIRMIZI); nokta(ax, *F, "F", dx=-0.15, dy=-0.65, renk=KIRMIZI)
kenar(ax, A, B, "5", Gm, d=0.4); u = (C - A) / np.linalg.norm(C - A); v = np.array([u[1], -u[0]])
if np.dot(v, A - Gm) < 0: v = -v
ax.annotate("", xy=C + 0.55 * v, xytext=A + 0.55 * v, arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(*((A + C) / 2 + 0.95 * v), "8", ha="center", va="center", fontsize=13)
ax.set_xlim(-0.8, 10.0); ax.set_ylim(-0.9, A[1] + 0.9)
kaydet(fig, __file__)
