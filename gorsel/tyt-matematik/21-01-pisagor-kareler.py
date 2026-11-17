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

# Dik kenarlar 3 ve 4, hipotenüs 5. Her kenarın üstüne kare çizilir: 9 + 16 = 25.
B = np.array([0.0, 0.0]); C = np.array([4.0, 0.0]); A = np.array([0.0, 3.0])
print("AC", uz(A, C), "B açısı", aci_olc(B, A, C))
fig, ax = sekil(5.2, 5.2); ax.set_aspect("equal"); ax.axis("off")
def kare(P, Q, renk, acik):
    P, Q = np.asarray(P, float), np.asarray(Q, float); u = Q - P; v = np.array([u[1], -u[0]])  # PQ'nun sağına
    pts = [P, Q, Q + v, P + v]
    ax.add_patch(patches.Polygon(pts, closed=True, facecolor=acik, edgecolor=renk, lw=1.6))
    return (P + Q + v) / 2 + 0 * v
mB = kare(B, C, MAVI, MAVI_ACIK)      # BC altında
mA = kare(A, B, YESIL, YESIL_ACIK)    # AB solunda
mH = kare(C, A, KIRMIZI, KIRMIZI_ACIK)  # hipotenüs dışında
ax.plot(*zip(A, B, C, A), color=YAZI, lw=2.4)
dik(ax, B, A, C, s=0.35)
ax.text(*(mB), "$4^2 = 16$", ha="center", va="center", color=MAVI, fontsize=15)
ax.text(*(mA), "$3^2 = 9$", ha="center", va="center", color=YESIL, fontsize=15)
ax.text(*(mH), "$5^2 = 25$", ha="center", va="center", color=KIRMIZI, fontsize=15)
G0 = (A + B + C) / 3
kenar(ax, B, C, "4", G0, d=-0.3); kenar(ax, A, B, "3", G0, d=-0.3); kenar(ax, A, C, "5", G0, d=-0.3)
nokta(ax, *A, "A", dx=-0.45, dy=0.1); nokta(ax, *B, "B", dx=-0.45, dy=-0.45); nokta(ax, *C, "C", dx=0.15, dy=-0.45)
ax.set_xlim(-3.4, 7.4); ax.set_ylim(-4.4, 7.4)
kaydet(fig, __file__)
