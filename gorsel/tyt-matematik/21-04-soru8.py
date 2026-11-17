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

# 4 m merdiven: önce yerle 60° (alt uç duvardan 2 m), sonra 45° (alt uç 2√2 m).
k = 1.0
O = np.array([0.0, 0.0])
P1 = np.array([2 * k, 0.0]); T1 = np.array([0.0, 2 * np.sqrt(3) * k])
P2 = np.array([2 * np.sqrt(2) * k, 0.0]); T2 = np.array([0.0, 2 * np.sqrt(2) * k])
print("L1", uz(P1, T1) / k, "L2", uz(P2, T2) / k, "a1", aci_olc(P1, T1, O), "a2", aci_olc(P2, T2, O))
fig, ax = sekil(4, 4); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Rectangle((-0.35, 0), 0.35, 4.0, facecolor=CIZGI, edgecolor="none"))
ax.plot([-0.35, 3.8], [0, 0], color=SOLUK, lw=2)
ax.plot([0, 0], [0, 4.0], color=SOLUK, lw=2)
ax.plot(*zip(P1, T1), color=MAVI, lw=3)
ax.plot(*zip(P2, T2), color=KIRMIZI, lw=3, ls="--")
kenar(ax, P1, T1, "4 m", O, d=-0.3, renk=MAVI)
kenar(ax, P2, T2, "4 m", O, d=0.3, renk=KIRMIZI)
aci(ax, P1, T1, O, r=0.3, ad="", renk=MAVI)
ax.text(P1[0] - 0.62, 0.17, "60°", color=MAVI, fontsize=12, ha="center", va="center")
aci(ax, P2, T2, O, r=0.3, ad="", renk=KIRMIZI)
ax.text(P2[0] - 0.5, 0.14, "45°", color=KIRMIZI, fontsize=11, ha="center", va="center")
nokta(ax, *T1, "", renk=MAVI); nokta(ax, *T2, "", renk=KIRMIZI)
ax.annotate("", xy=(0.25, T2[1]), xytext=(0.25, T1[1]), arrowprops=dict(arrowstyle="->", color=YAZI, lw=1.4))
ax.text(0.35, (T1[1] + T2[1]) / 2, "?", fontsize=14, va="center")
ax.text(2.0, 3.6, "önce", color=MAVI, fontsize=12); ax.text(2.0, 3.2, "sonra", color=KIRMIZI, fontsize=12)
ax.plot([1.55, 1.9], [3.7, 3.7], color=MAVI, lw=3); ax.plot([1.55, 1.9], [3.3, 3.3], color=KIRMIZI, lw=3, ls="--")
ax.set_xlim(-0.5, 3.9); ax.set_ylim(-0.3, 4.1)
kaydet(fig, __file__)
