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

# Köşegenleri dik dörtgen: [AC] ⊥ [BD], O kesim noktası. AB=10, BC=5, CD=11, DA=x=14.
# |OA|²=87, |OB|²=13, |OC|²=12, |OD|²=109 seçildi: 87+13=100, 13+12=25, 12+109=121, 109+87=196.
O = np.array([0.0, 0.0]); A = np.array([0, np.sqrt(87)]); B = np.array([-np.sqrt(13), 0]); C = np.array([0, -np.sqrt(12)]); D = np.array([np.sqrt(109), 0])
print("AB BC CD DA", uz(A, B), uz(B, C), uz(C, D), uz(D, A))
fig, ax = sekil(5.2, 5.2); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(A, C), color=MAVI, lw=1.6, ls="--"); ax.plot(*zip(B, D), color=MAVI, lw=1.6, ls="--")
dik(ax, O, A, D, s=0.45, renk=MAVI)
Gm = O
kenar(ax, A, B, "10", Gm, d=0.5, renk=KIRMIZI); kenar(ax, C, D, "11", Gm, d=0.55, renk=KIRMIZI)
kenar(ax, B, C, "5", Gm, d=0.45, renk=YESIL); kenar(ax, D, A, "x", Gm, d=0.55, renk=YESIL, fs=15)
nokta(ax, *A, "A", dx=-0.2, dy=0.3); nokta(ax, *B, "B", dx=-0.75, dy=-0.15); nokta(ax, *C, "C", dx=-0.2, dy=-0.8)
nokta(ax, *D, "D", dx=0.3, dy=-0.15); nokta(ax, *O, "O", dx=-0.75, dy=0.25, renk=MAVI)
ax.set_xlim(-5.0, 11.6); ax.set_ylim(-4.5, 10.6)
kaydet(fig, __file__)
