import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P, float) - np.asarray(Q, float))), 3)
def kenar(ax, P, Q, metin, G, d=0.45, renk=YAZI, fs=13):
    """[PQ] kenarının ortasına, G noktasından uzak tarafa etiket."""
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G, float)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik(ax, K, P, Q, s=0.3, renk=SOLUK):
    """K köşesinde KP ile KQ arasındaki dik açı işareti."""
    K, P, Q = (np.asarray(t, float) for t in (K, P, Q))
    u = (P - K) / np.linalg.norm(P - K) * s; v = (Q - K) / np.linalg.norm(Q - K) * s
    ax.plot(*zip(K + u, K + u + v, K + v), color=renk, lw=1.3)
def aci_olc(K, P, Q):
    u, v = np.asarray(P, float) - K, np.asarray(Q, float) - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)

# Soru 6: [AH] ⊥ [BC], D ∈ [AH]. AB=10, AC=8, DB=7, DC=x=√13.
# |HB|²=40, |HC|²=4, |AH|²=60, |DH|²=9.
H = np.array([0.0, 0.0]); B = np.array([-np.sqrt(40), 0]); C = np.array([2.0, 0]); A = np.array([0, np.sqrt(60)]); D = np.array([0, 3.0])
print("AB AC DB DC^2", uz(A, B), uz(A, C), uz(D, B), round(uz(D, C) ** 2, 3))
fig, ax = sekil(4.6, 5.0); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, H), color=YAZI, lw=1.6)
ax.plot(*zip(B, D, C), color=YAZI, lw=1.6)
dik(ax, H, A, C, s=0.4)
kenar(ax, A, B, "10", D, d=0.45); kenar(ax, A, C, "8", B, d=0.4)
ax.text(-3.2, 1.95, "7", ha="center", va="center")
ax.text(0.85, 0.85, "x", ha="center", va="center", fontsize=15)
nokta(ax, *A, "A", dx=-0.2, dy=0.3); nokta(ax, *B, "B", dx=-0.65, dy=-0.2); nokta(ax, *C, "C", dx=0.2, dy=-0.25)
nokta(ax, *H, "H", dx=-0.25, dy=-0.75); nokta(ax, *D, "D", dx=-0.75, dy=0.15)
ax.set_xlim(-7.3, 3.2); ax.set_ylim(-1.0, 8.8)
kaydet(fig, __file__)
