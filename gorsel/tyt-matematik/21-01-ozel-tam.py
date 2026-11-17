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

# Kenarları tam sayı olan özel dik üçgenler. Her biri kendi içinde doğru oranlı (yatay dik kenar 4 birim çizilir).
ucgenler = [((3, 4, 5), "k", (0.0, 2.6)), ((8, 15, 17), "x", (6.2, 2.6)),
            ((5, 12, 13), "a", (0.0, 0.0)), ((7, 24, 25), "b", (6.2, 0.0))]
fig, ax = sekil(6.2, 3.6); ax.set_aspect("equal"); ax.axis("off")
renkler = [MAVI, YESIL, SARI, KIRMIZI]
for ((p, q, r), h, (ox, oy)), rk in zip(ucgenler, renkler):
    assert p * p + q * q == r * r
    s = 4.0 / q
    B = np.array([ox, oy]); C = B + [q * s, 0]; A = B + [0, p * s]
    print(p, q, r, "AC/BC", round(uz(A, C) / uz(B, C), 4), round(r / q, 4))
    ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor="none", edgecolor=rk, lw=2.2))
    dik(ax, B, A, C, s=0.25)
    G0 = (A + B + C) / 3
    kenar(ax, A, B, f"{p}{h}", G0, d=0.42, renk=rk); kenar(ax, B, C, f"{q}{h}", G0, d=0.3, renk=rk)
    kenar(ax, A, C, f"{r}{h}", G0, d=0.38, renk=rk)
ax.set_xlim(-0.9, 10.6); ax.set_ylim(-0.6, 5.9)
kaydet(fig, __file__)
