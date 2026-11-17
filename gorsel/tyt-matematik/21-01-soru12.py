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

# Soru 12: AB kule (B'de dik). AD = 6√2 halat yerle 45°; AC halatı yerle 30°. AB=6, BD=6, BC=6√3, AC=12.
B = np.array([0.0, 0.0]); A = np.array([0.0, 6.0]); D = np.array([6.0, 0]); C = np.array([6 * np.sqrt(3), 0])
print("AD", uz(A, D), "AC", uz(A, C), "D", aci_olc(D, A, B), "C", aci_olc(C, A, B))
fig, ax = sekil(5.4, 3.6); ax.set_aspect("equal"); ax.axis("off")
ax.plot([-1.0, 11.4], [0, 0], color=SOLUK, lw=1.6)
ax.add_patch(patches.Rectangle((-0.35, 0), 0.35, 6.0, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.4))
ax.plot(*zip(A, D), color=MAVI); ax.plot(*zip(A, C), color=KIRMIZI)
dik(ax, B, A, D, s=0.4)
aci(ax, D, A, B, r=0.7, ad="", renk=MAVI); ax.text(D[0] - 1.5, 0.3, "45°", color=MAVI, fontsize=12, ha="center")
aci(ax, C, A, B, r=1.3, ad="", renk=KIRMIZI); ax.text(C[0] - 1.85, 0.42, "30°", color=KIRMIZI, fontsize=12, ha="center")
kenar(ax, A, D, "6√2", C, d=0.55, renk=MAVI)
nokta(ax, *A, "A", dx=-0.85, dy=0.0); nokta(ax, *B, "B", dx=-0.85, dy=-0.6); nokta(ax, *D, "D", dx=-0.2, dy=-0.75); nokta(ax, *C, "C", dx=-0.2, dy=-0.75)
ax.set_xlim(-1.3, 11.6); ax.set_ylim(-1.0, 6.8)
kaydet(fig, __file__)
