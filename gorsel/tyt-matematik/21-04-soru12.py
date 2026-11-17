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

# Direk boyu 4√3; ışın 60° iken gölge 4 m, 30° iken gölge 12 m.
k = 0.35
P = np.array([0.0, 0.0]); T = np.array([0.0, 4 * np.sqrt(3) * k]); G1 = np.array([4 * k, 0.0]); G2 = np.array([12 * k, 0.0])
print("a1", aci_olc(G1, T, P), "a2", aci_olc(G2, T, P), "PG1", uz(P, G1) / k, "PG2", uz(P, G2) / k)
fig, ax = sekil(5, 2.6); ax.set_aspect("equal"); ax.axis("off")
ax.plot([-0.3, G2[0] + 0.3], [0, 0], color=SOLUK, lw=1.6)
ax.plot(*zip(P, T), color=YAZI, lw=3.5)
ax.plot(*zip(T, G1), color=SARI, lw=1.6, ls="--"); ax.plot(*zip(T, G2), color=SARI, lw=1.6, ls="--")
ax.plot(*zip(P, G1), color=MAVI, lw=4); ax.plot(*zip(G1, G2), color=KIRMIZI, lw=4)
aci(ax, G1, T, P, r=0.3, ad="60°", renk=YAZI)
aci(ax, G2, T, P, r=0.7, ad="30°", renk=YAZI)
ax.text(G1[0] / 2, -0.25, "4 m", ha="center", va="center", fontsize=12, color=MAVI)
ax.text((G1[0] + G2[0]) / 2, -0.25, "?", ha="center", va="center", fontsize=13, color=KIRMIZI)
ax.set_xlim(-0.5, G2[0] + 0.4); ax.set_ylim(-0.5, T[1] + 0.3)
kaydet(fig, __file__)
