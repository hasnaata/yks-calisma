import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P) - np.asarray(Q))), 3)
def kenar(ax, P, Q, metin, G, d=0.45, renk=YAZI, fs=13):
    """[PQ] kenarının ortasına, G'nin ters tarafına etiket."""
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik_ayak(P, Q, R):
    """R noktasından PQ doğrusuna inen dikmenin ayağı."""
    P, Q, R = (np.asarray(t, float) for t in (P, Q, R))
    u = (Q - P) / np.linalg.norm(Q - P); return P + np.dot(R - P, u) * u
def dik(ax, ayak, p1, p2, k=0.3, renk=YAZI):
    """ayak noktasında, ayak->p1 ve ayak->p2 yönleri arasında dik açı karesi."""
    ayak = np.asarray(ayak, float)
    u = (np.asarray(p1) - ayak) / np.linalg.norm(np.asarray(p1) - ayak); v = (np.asarray(p2) - ayak) / np.linalg.norm(np.asarray(p2) - ayak)
    ax.plot(*zip(ayak + k * u, ayak + k * (u + v), ayak + k * v), color=renk, lw=1.2)
def centik(ax, P, Q, n=1, renk=YAZI, L=0.18, ara=0.12):
    """[PQ] ortasına n tane eşlik çentiği."""
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    for i in range(n):
        c = M + (i - (n - 1) / 2) * ara * u
        ax.plot(*zip(c - L * v, c + L * v), color=renk, lw=1.3)

# m(A)=90, |AB|=6, |AC|=8, |BC|=10, D [BC]'nin orta noktası. Yükseklikler A'da kesişir; |AD| = 5.
A, B, C = np.array([0.0, 0.0]), np.array([0.0, 6.0]), np.array([8.0, 0.0])
D = (B + C) / 2; H = dik_ayak(B, C, A)
print("BC", uz(B, C), "AD", uz(A, D), "AH", uz(A, H))
G = (A + B + C) / 3
fig, ax = sekil(4.8, 3.8)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([A, B, C], color=YESIL_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.8)
dik(ax, A, B, C, k=0.45); dik(ax, H, A, C, k=0.4, renk=KIRMIZI)
nokta(ax, *D, "", renk=MAVI)
ax.text(D[0] + 0.25, D[1] + 0.25, "D (çeşme)", color=MAVI, fontsize=12)
for P, ad, d in ((A, "A", (-0.55, -0.55)), (B, "B", (-0.55, 0.1)), (C, "C", (0.2, -0.55)), (H, "H", (-0.05, 0.3))): ax.text(P[0] + d[0], P[1] + d[1], ad, fontsize=13, color=KIRMIZI if ad == "H" else YAZI)
kenar(ax, A, B, "6", G, d=0.45); kenar(ax, A, C, "8", G, d=0.5)
ax.set_xlim(-0.9, 9.6); ax.set_ylim(-0.9, 6.6)
kaydet(fig, __file__)
