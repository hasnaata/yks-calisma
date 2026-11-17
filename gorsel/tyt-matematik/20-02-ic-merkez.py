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

# |AB|=13, |BC|=14, |CA|=15, alan 84. D iç açıortayların kesim noktası, D'nin kenarlara uzaklığı r=4.
# A(DAB)=26, A(DBC)=28, A(DCA)=30.
A, B, C = ucgen(14, 15, 13)
D = (14 * A + 15 * B + 13 * C) / 42
def alan(P, Q, R): return round(abs(float((Q - P)[0] * (R - P)[1] - (Q - P)[1] * (R - P)[0])) / 2, 3)
H = dik_ayak(B, C, D)
print("A", A, "D", D, "alanlar", alan(D, A, B), alan(D, B, C), alan(D, C, A), "r", uz(D, H), uz(D, dik_ayak(A, B, D)), uz(D, dik_ayak(A, C, D)))
Gm = (A + B + C) / 3

fig, ax = sekil(5.0, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([D, A, B], color=MAVI_ACIK, lw=0))
ax.add_patch(plt.Polygon([D, B, C], color=SARI_ACIK, lw=0))
ax.add_patch(plt.Polygon([D, C, A], color=YESIL_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
for K in (A, B, C): ax.plot(*zip(K, D), color=KIRMIZI, lw=1.6)
ax.plot(*zip(D, H), color=SOLUK, lw=1.4, ls="--"); dik(ax, H, C, D, s=0.4)
ax.text(D[0] - 0.65, 2.0, "4", color=SOLUK, fontsize=12, va="center")
for P, Q, renk, m in ((A, B, MAVI, "26"), (B, C, SARI, "28"), (C, A, YESIL, "30")):
    M = (D + P + Q) / 3 + (np.array([2.0, -0.1]) if m == "28" else 0)
    ax.text(*M, m, color=renk, fontsize=14, ha="center", va="center", fontweight="bold")
nokta(ax, *A, "A", dx=-0.25, dy=0.35); nokta(ax, *B, "B", dx=-0.7, dy=-0.6); nokta(ax, *C, "C", dx=0.2, dy=-0.6)
nokta(ax, *D, "D", dx=0.25, dy=0.25, renk=KIRMIZI)
kenar(ax, A, B, "13", Gm, d=0.9); kenar(ax, C, A, "15", Gm, d=0.9); kenar(ax, B, C, "14", Gm, d=0.75)
ax.set_xlim(-1.2, 15.0); ax.set_ylim(-1.3, A[1] + 0.9)
kaydet(fig, __file__)
