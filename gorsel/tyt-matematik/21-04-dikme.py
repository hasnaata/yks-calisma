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

# ABC üçgeni: m(B)=45°, m(C)=30°, |AC|=8. AH ⊥ BC: |AH|=4, |HC|=4√3, |BH|=4.
k = 0.5
H = np.array([0.0, 0.0]); A = np.array([0.0, 4 * k]); B = np.array([-4 * k, 0.0]); C = np.array([4 * np.sqrt(3) * k, 0.0])
print("AC", uz(A, C) / k, "AH", uz(A, H) / k, "BH", uz(B, H) / k, "HC", uz(H, C) / k, "B", aci_olc(B, A, C), "C", aci_olc(C, A, B))
fig, ax = sekil(5.6, 3); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.8, ls="--")
dik(ax, H, A, C, s=0.22)
kenar(ax, A, C, "8", H, d=0.3, renk=YAZI)
ax.text(H[0] + 0.15, A[1] / 2, "4", color=KIRMIZI, fontsize=13, ha="left", va="center")
ax.text((B[0] + H[0]) / 2, -0.32, "4", color=MAVI, fontsize=13, ha="center", va="center")
ax.text((H[0] + C[0]) / 2, -0.32, "4√3", color=YESIL, fontsize=13, ha="center", va="center")
aci(ax, B, C, A, r=0.55, ad="45°", renk=MAVI)
aci(ax, C, A, B, r=0.9, ad="30°", renk=YESIL)
nokta(ax, *A, "A", dx=-0.1, dy=0.18); nokta(ax, *B, "B", dx=-0.4, dy=-0.35); nokta(ax, *C, "C", dx=0.12, dy=-0.35)
nokta(ax, *H, "H", dx=-0.42, dy=-0.4)
ax.set_xlim(B[0] - 0.6, C[0] + 0.6); ax.set_ylim(-0.6, A[1] + 0.5)
kaydet(fig, __file__)
