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

# Soru 5: |AB|=12, |AC|=6, |BC|=9. [AD] iç açıortay (|BD|=6, |DC|=3). [DE] ∥ [AB], E ∈ [AC]: |DE|=4, |AE|=4, |EC|=2.
A, B, C = ucgen(9, 6, 12)
D = B + (C - B) * 6 / 9; E = C + (A - C) / 3
print("BD", uz(B, D), "DC", uz(D, C), "DE", uz(D, E), "AE", uz(A, E), "EC", uz(E, C), "BAD", aci_olc(A, B, D), "DAC", aci_olc(A, D, C), "paralel", np.cross(np.append(E - D, 0), np.append(A - B, 0))[2])
Gm = (A + B + C) / 3

fig, ax = sekil(5.6, 3.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, D), color=KIRMIZI, lw=2)
ax.plot(*zip(D, E), color=MAVI, lw=2)
aci(ax, A, B, D, r=1.5, renk=KIRMIZI); aci(ax, A, D, C, r=1.75, renk=KIRMIZI)
for P, Q in ((B, D), (D, C)):
    w = (P - A) / np.linalg.norm(P - A) + (Q - A) / np.linalg.norm(Q - A); w /= np.linalg.norm(w)
    ax.text(*(A + 2.35 * w), "α", color=KIRMIZI, fontsize=12, ha="center", va="center")
nokta(ax, *A, "A", dx=-0.2, dy=0.3); nokta(ax, *B, "B", dx=-0.6, dy=-0.5); nokta(ax, *C, "C", dx=0.15, dy=-0.5)
nokta(ax, *D, "D", dx=-0.15, dy=-0.65, renk=KIRMIZI); nokta(ax, *E, "E", dx=-0.65, dy=0.2, renk=MAVI)
kenar(ax, A, B, "12", Gm, d=0.55)
olcu(ax, A, C, "6", Gm, d=0.5)
olcu(ax, B, C, "9", Gm, d=0.9)
ax.set_xlim(-1.0, 12.0); ax.set_ylim(-2.0, A[1] + 0.7)
kaydet(fig, __file__)
