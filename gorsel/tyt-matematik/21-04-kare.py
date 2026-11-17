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

# Kenarı 1 birim olan ABCD karesi; [AC] köşegeni √2. ABC: 45°-45°-90°.
k = 3.0
A = np.array([0.0, 0.0]); B = np.array([k, 0.0]); C = np.array([k, k]); D = np.array([0.0, k])
print("AC", uz(A, C) / k, "BAC", aci_olc(A, B, C), "BCA", aci_olc(C, A, B))
fig, ax = sekil(4.2, 4); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=YESIL_ACIK, edgecolor="none"))
ax.plot(*zip(C, D, A), color=SOLUK, lw=1.8)
ax.plot(*zip(A, B, C, A), color=YESIL)
dik(ax, B, A, C, s=0.25)
G0 = (A + B + C) / 3
kenar(ax, A, B, "1", G0, d=0.3, renk=YESIL); kenar(ax, B, C, "1", G0, d=0.3, renk=YESIL)
kenar(ax, A, C, "√2", G0, d=0.35, renk=YESIL)
aci(ax, A, B, C, r=0.75, ad="45°", renk=YAZI)
aci(ax, C, A, B, r=0.75, ad="45°", renk=YAZI)
nokta(ax, *A, "A", dx=-0.4, dy=-0.4); nokta(ax, *B, "B", dx=0.12, dy=-0.4)
nokta(ax, *C, "C", dx=0.12, dy=0.12); nokta(ax, *D, "D", dx=-0.4, dy=0.12)
ax.set_xlim(-0.7, k + 0.7); ax.set_ylim(-0.7, k + 0.6)
kaydet(fig, __file__)
