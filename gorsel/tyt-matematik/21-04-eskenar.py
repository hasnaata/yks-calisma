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

# Kenarı 2 birim olan eşkenar ABC üçgeni; A'dan [BC]'ye AH yüksekliği. ABH: 30°-60°-90°, kenarlar 1, √3, 2.
k = 2.0  # 1 birim = 2 çizim birimi
B = np.array([0.0, 0.0]); C = np.array([2 * k, 0.0]); A = np.array([k, k * np.sqrt(3)]); H = np.array([k, 0.0])
print("AB", uz(A, B) / k, "BH", uz(B, H) / k, "AH", uz(A, H) / k, "B", aci_olc(B, A, C), "BAH", aci_olc(A, B, H), "H", aci_olc(H, A, B))
fig, ax = sekil(5, 4.2); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, H], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
ax.plot(*zip(A, C, H), color=SOLUK, lw=1.8)
ax.plot(*zip(H, B, A, H), color=MAVI)
dik(ax, H, A, B)
G0 = (A + B + H) / 3
kenar(ax, A, B, "2", G0, d=0.3, renk=MAVI); kenar(ax, B, H, "1", G0, d=0.3, renk=MAVI)
ax.text(H[0] + 0.22, A[1] / 2, "√3", color=MAVI, fontsize=13, ha="left", va="center")
kenar(ax, A, C, "2", (A + C + H) / 3, d=0.3, renk=SOLUK); kenar(ax, H, C, "1", (A + C + H) / 3, d=0.3, renk=SOLUK)
aci(ax, B, H, A, r=0.45, ad="60°", renk=YAZI)
aci(ax, A, B, H, r=0.6, ad="30°", renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.1, dy=0.2); nokta(ax, *B, "B", dx=-0.4, dy=-0.4); nokta(ax, *C, "C", dx=0.15, dy=-0.4)
nokta(ax, *H, "H", dx=-0.12, dy=-0.5)
ax.set_xlim(-0.7, 4.7); ax.set_ylim(-0.7, A[1] + 0.6)
kaydet(fig, __file__)
