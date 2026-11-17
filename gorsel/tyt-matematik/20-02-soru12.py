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

# Soru 12: |AB|=10, |AC|=6, |BC|=8, C dik. [AE] iç açıortay (|BE|=5, |EC|=3), [AD] dış açıortay (|CD|=12).
# A(AED) = |ED|·|AC|/2 = 15·6/2 = 45.
A, B, C = ucgen(8, 6, 10)
E = np.array([5.0, 0.0]); D = np.array([20.0, 0.0])
P = A + 2.4 * (A - B) / np.linalg.norm(A - B)
print("A", A, "C", aci_olc(C, A, B), "BAE", aci_olc(A, B, E), "EAC", aci_olc(A, E, C), "PAD", aci_olc(A, P, D), "DAC", aci_olc(A, D, C), "EAD", aci_olc(A, E, D))
Gm = (A + B + C) / 3

fig, ax = sekil(6, 2.9)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([A, E, D], color=SARI_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(C, D), color=SOLUK, lw=1.6, ls="--")
ax.plot(*zip(A, P), color=SOLUK, lw=1.6, ls="--")
ax.plot(*zip(A, E), color=MAVI, lw=2)
ax.plot(*zip(A, D), color=KIRMIZI, lw=2)
dik(ax, C, D, A, s=0.6)
aci(ax, A, B, E, r=1.6, ad="α", renk=MAVI); aci(ax, A, E, C, r=1.85, ad="α", renk=MAVI)
aci(ax, A, P, D, r=1.4, ad="β", renk=KIRMIZI); aci(ax, A, D, C, r=1.65, ad="β", renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.9, dy=0.2); nokta(ax, *B, "B", dx=-0.8, dy=-1.0); nokta(ax, *C, "C", dx=-0.3, dy=-1.1)
nokta(ax, *E, "E", dx=-0.3, dy=-1.1, renk=MAVI); nokta(ax, *D, "D", dx=0.1, dy=-1.1, renk=KIRMIZI)
kenar(ax, A, B, "10", Gm, d=0.7); kenar(ax, A, C, "6", Gm, d=0.55)
olcu(ax, B, C, "8", Gm, d=1.9, ek=0.6)
ax.set_xlim(-1.2, 21.0); ax.set_ylim(-3.2, P[1] + 0.3)
kaydet(fig, __file__)
