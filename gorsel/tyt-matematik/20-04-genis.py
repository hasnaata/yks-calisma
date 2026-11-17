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

# Geniş açılı: H, B, C sırasıyla. |AH|=12, |AB|=13 => |HB|=5. |BC|=11 => |HC|=16, |AC|=20.
H = np.array([0.0, 0.0]); B = np.array([5.0, 0.0]); C = np.array([16.0, 0.0]); A = np.array([0.0, 12.0])
print("AB", uz(A, B), "AC", uz(A, C), "HC", uz(H, C))
G = (A + B + C) / 3
fig, ax = sekil(6, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([A, B, C], color=MAVI_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(H, B), color=SOLUK, lw=1.6, ls="--")
ax.plot(*zip(A, H), color=KIRMIZI, lw=2.2)
dik(ax, H, A, B, k=0.8, renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.5, dy=0.5); nokta(ax, *B, "B", dx=0.05, dy=-1.4); nokta(ax, *C, "C", dx=0.3, dy=-1.1)
nokta(ax, *H, "H", dx=-0.4, dy=-1.4, renk=KIRMIZI)
kenar(ax, A, B, "13", (8, -3), d=1.0)
ax.text(-0.5, 6, "12", color=KIRMIZI, fontsize=14, ha="right", va="center")
ax.text(2.5, -0.9, "5", color=SOLUK, fontsize=14, ha="center")
ax.text(10.5, -0.9, "11", color=YAZI, fontsize=14, ha="center")
kenar(ax, A, C, "?", G, d=0.8, renk=MAVI, fs=15)
ax.set_xlim(-2.2, 17.2); ax.set_ylim(-2.0, 13.2)
kaydet(fig, __file__)
