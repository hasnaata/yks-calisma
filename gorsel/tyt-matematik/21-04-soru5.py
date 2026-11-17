import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P, float) - np.asarray(Q, float))), 3)
def kenar(ax, P, Q, metin, G, d=0.35, renk=YAZI, fs=13):
    """[PQ] kenarının ortasına, G noktasından uzak tarafa etiket."""
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G, float)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik(ax, K, P, Q, s=0.25, renk=SOLUK):
    """K köşesinde KP ile KQ arasındaki dik açı işareti."""
    K, P, Q = (np.asarray(t, float) for t in (K, P, Q))
    u = (P - K) / np.linalg.norm(P - K) * s; v = (Q - K) / np.linalg.norm(Q - K) * s
    ax.plot(*zip(K + u, K + u + v, K + v), color=renk, lw=1.3)
def aci_olc(K, P, Q):
    K = np.asarray(K, float); u, v = np.asarray(P, float) - K, np.asarray(Q, float) - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)

# ABCD dikdörtgeni: m(BAC)=30°, |BC|=5 (|AB| = 5√3).
k = 0.5
A = np.array([0.0, 0.0]); B = np.array([5 * np.sqrt(3) * k, 0.0]); C = B + [0, 5 * k]; D = A + [0, 5 * k]
print("BC", uz(B, C) / k, "AB", uz(A, B) / k, "BAC", aci_olc(A, B, C), "B", aci_olc(B, A, C))
fig, ax = sekil(4.6, 3); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI); ax.plot(*zip(A, C), color=MAVI, lw=1.8)
dik(ax, B, A, C, s=0.2)
kenar(ax, B, C, "5", A, d=0.25, renk=YAZI)
aci(ax, A, B, C, r=0.9, ad="30°", renk=MAVI)
nokta(ax, *A, "A", dx=-0.38, dy=-0.35); nokta(ax, *B, "B", dx=0.12, dy=-0.35)
nokta(ax, *C, "C", dx=0.12, dy=0.1); nokta(ax, *D, "D", dx=-0.38, dy=0.1)
ax.set_xlim(-0.6, B[0] + 0.6); ax.set_ylim(-0.6, C[1] + 0.5)
kaydet(fig, __file__)
