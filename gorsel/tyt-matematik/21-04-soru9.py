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

# Kule: yükseklik 30√3; A dibinden 30 m (60°), B dibinden 90 m (30°), aynı tarafta.
k = 0.05
K = np.array([0.0, 0.0]); T = np.array([0.0, 30 * np.sqrt(3) * k]); A = np.array([30 * k, 0.0]); B = np.array([90 * k, 0.0])
print("A", aci_olc(A, T, K), "B", aci_olc(B, T, A), "KA", uz(K, A) / k, "AB", uz(A, B) / k)
fig, ax = sekil(5.2, 2.6); ax.set_aspect("equal"); ax.axis("off")
ax.plot([-0.3, B[0] + 0.3], [0, 0], color=SOLUK, lw=1.6)
ax.add_patch(patches.Rectangle((-0.22, 0), 0.22, T[1], facecolor=CIZGI, edgecolor=SOLUK, lw=1))
ax.plot(*zip(A, T), color=MAVI, lw=1.6, ls="--"); ax.plot(*zip(B, T), color=YESIL, lw=1.6, ls="--")
aci(ax, A, T, K, r=0.3, ad="", renk=MAVI)
ax.text(A[0] - 0.75, 0.2, "60°", color=MAVI, fontsize=12, ha="center", va="center")
aci(ax, B, T, A, r=0.6, ad="30°", renk=YESIL)
ax.text(A[0] / 2, -0.22, "30 m", ha="center", va="center", fontsize=12)
ax.text((A[0] + B[0]) / 2, -0.22, "?", ha="center", va="center", fontsize=13)
nokta(ax, *A, "A", dx=-0.08, dy=-0.5); nokta(ax, *B, "B", dx=-0.08, dy=-0.5)
nokta(ax, *T, "T", dx=-0.45, dy=0.05)
ax.set_xlim(-0.6, B[0] + 0.4); ax.set_ylim(-0.6, T[1] + 0.3)
kaydet(fig, __file__)
