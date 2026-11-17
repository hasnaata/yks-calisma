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

# ABCD karesi kenar 6; ABE eşkenar üçgeni karenin içinde; E'den [DC]'ye uzaklık 6 − 3√3.
k = 0.5
A = np.array([0.0, 0.0]); B = np.array([6 * k, 0.0]); C = np.array([6 * k, 6 * k]); D = np.array([0.0, 6 * k])
E = np.array([3 * k, 3 * np.sqrt(3) * k]); F = np.array([E[0], C[1]])
print("EA", uz(E, A) / k, "EB", uz(E, B) / k, "E->DC", uz(E, F) / k, "EAB", aci_olc(A, E, B))
fig, ax = sekil(3.6, 3.6); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.add_patch(patches.Polygon([A, B, E], closed=True, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.plot(*zip(E, F), color=KIRMIZI, lw=1.6, ls="--")
kenar(ax, A, B, "6", E, d=0.33)
for P, Q in ((A, E), (B, E), (A, B)):
    M = (P + Q) / 2; u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]]) * 0.1
    ax.plot(*zip(M - v, M + v), color=MAVI, lw=1.6)
nokta(ax, *A, "A", dx=-0.35, dy=-0.32); nokta(ax, *B, "B", dx=0.1, dy=-0.32)
nokta(ax, *C, "C", dx=0.1, dy=0.08); nokta(ax, *D, "D", dx=-0.35, dy=0.08)
nokta(ax, *E, "E", dx=0.12, dy=0.04)
ax.set_xlim(-0.5, B[0] + 0.5); ax.set_ylim(-0.55, C[1] + 0.4)
kaydet(fig, __file__)
