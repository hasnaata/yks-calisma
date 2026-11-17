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

# Yol üzerinde H, B, C sırasıyla. |AH|=8, |AB|=10, |AC|=17 => |HB|=6, |HC|=15, |BC|=9, alan 36.
H, B, C, A = np.array([0.0, 0.0]), np.array([6.0, 0.0]), np.array([15.0, 0.0]), np.array([0.0, 8.0])
print("AB", uz(A, B), "AC", uz(A, C))
fig, ax = sekil(6, 3.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-2.5, 17.5], [0, 0], color=SOLUK, lw=3, alpha=0.5, solid_capstyle="butt")
ax.text(17.3, 0.35, "yol", color=SOLUK, fontsize=12, ha="right")
ax.add_patch(plt.Polygon([A, B, C], color=MAVI_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=2, ls="--")
dik(ax, H, A, B, k=0.6, renk=KIRMIZI)
nokta(ax, *A, "", renk=MAVI); ax.text(A[0] - 0.4, A[1] + 0.4, "A (fener)", fontsize=12, color=MAVI)
for P, ad in ((H, "H"), (B, "B"), (C, "C")): nokta(ax, *P, ""); ax.text(P[0], -1.1, ad, fontsize=13, ha="center")
ax.text(-0.4, 4, "8", color=KIRMIZI, fontsize=13, ha="right")
G = (A + B + C) / 3
kenar(ax, A, B, "10", (9, -5), d=0.7); kenar(ax, A, C, "17", G, d=0.6)
ax.set_xlim(-2.6, 17.6); ax.set_ylim(-1.6, 9.4)
kaydet(fig, __file__)
