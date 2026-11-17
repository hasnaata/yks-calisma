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

# Soru 8: 5 m merdiven. Önce alt ucu duvardan 1,4 m (üst ucu 4,8 m), sonra 3 m (üst ucu 4 m).
W = 0.0
P1, Q1 = np.array([1.4, 0]), np.array([0, 4.8]); P2, Q2 = np.array([3.0, 0]), np.array([0, 4.0])
print("merdiven", uz(P1, Q1), uz(P2, Q2))
fig, ax = sekil(4.4, 4.6); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Rectangle((-0.45, 0), 0.45, 5.6, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.4))
ax.plot([-0.6, 3.8], [0, 0], color=SOLUK, lw=1.6)
ax.plot(*zip(P1, Q1), color=MAVI, lw=3)
ax.plot(*zip(P2, Q2), color=KIRMIZI, lw=3, ls="--")
nokta(ax, *Q1, renk=MAVI); nokta(ax, *Q2, renk=KIRMIZI); nokta(ax, *P1, renk=MAVI); nokta(ax, *P2, renk=KIRMIZI)
ax.text(0.42, 1.5, "5 m", color=MAVI, ha="center"); ax.text(2.55, 1.6, "5 m", color=KIRMIZI, ha="center")
ax.annotate("", xy=(0, -0.35), xytext=(1.4, -0.35), arrowprops=dict(arrowstyle="<->", color=YAZI, lw=1.2))
ax.text(0.7, -0.75, "1,4 m", ha="center", fontsize=12)
ax.annotate("", xy=(1.4, -0.35), xytext=(3.0, -0.35), arrowprops=dict(arrowstyle="<->", color=YAZI, lw=1.2))
ax.text(2.2, -0.75, "1,6 m", ha="center", fontsize=12)
ax.text(1.5, 5.2, "1. durum", color=MAVI, fontsize=11); ax.text(1.5, 4.6, "2. durum", color=KIRMIZI, fontsize=11)
ax.text(-0.22, 5.8, "duvar", color=SARI, fontsize=11, ha="center")
ax.set_xlim(-0.8, 3.9); ax.set_ylim(-1.1, 6.1)
kaydet(fig, __file__)
