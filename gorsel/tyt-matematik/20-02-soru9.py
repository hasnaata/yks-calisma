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

# Soru 9: bahçe ABC, |AB|=10, |BC|=24, |AC|=26 (B dik), alan 120. D iç açıortayların kesim noktası (r=4).
# Parseller: A(DAB)=20, A(DBC)=48, A(DCA)=52.
A, B, C = ucgen(24, 26, 10)
D = (24 * A + 26 * B + 10 * C) / 60
def alan(P, Q, R): return abs(float((Q - P)[0] * (R - P)[1] - (Q - P)[1] * (R - P)[0])) / 2
print("A", A, "D", D, "parseller", alan(D, A, B), alan(D, B, C), alan(D, C, A), "B", aci_olc(B, A, C))
Gm = (A + B + C) / 3

fig, ax = sekil(5.6, 3.0)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([D, A, B], color=MAVI_ACIK, lw=0))
ax.add_patch(plt.Polygon([D, B, C], color=SARI_ACIK, lw=0))
ax.add_patch(plt.Polygon([D, C, A], color=YESIL_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
for K in (A, B, C): ax.plot(*zip(K, D), color=KIRMIZI, lw=1.8)
dik(ax, B, A, C, s=0.9)
for K, P, Q, r in ((A, B, D, 2.2), (A, D, C, 2.6), (B, A, D, 2.0), (B, D, C, 2.4), (C, B, D, 4.5), (C, D, A, 5.2)):
    aci(ax, K, P, Q, r=r, renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.4, dy=0.5); nokta(ax, *B, "B", dx=-1.3, dy=-1.0); nokta(ax, *C, "C", dx=0.4, dy=-1.0)
nokta(ax, *D, "D", dx=0.5, dy=0.4, renk=KIRMIZI)
kenar(ax, A, B, "10 m", Gm, d=2.2); kenar(ax, B, C, "24 m", Gm, d=1.1); kenar(ax, C, A, "26 m", Gm, d=1.3)
ax.set_xlim(-4.2, 25.5); ax.set_ylim(-2.0, A[1] + 1.4)
kaydet(fig, __file__)
