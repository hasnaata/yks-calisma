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

# [AH] ⊥ [BC], |AH|=12, |BH|=16, |HC|=35  =>  |AB|=20, |AC|=37.
B, C, H, A = np.array([0.0, 0.0]), np.array([51.0, 0.0]), np.array([16.0, 0.0]), np.array([16.0, 12.0])
print("AB", uz(A, B), "AC", uz(A, C))
G = (A + B + C) / 3
fig, ax = sekil(6, 2.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI); ax.plot(*zip(A, H), color=KIRMIZI, lw=2.2)
dik(ax, H, A, C, k=1.6, renk=KIRMIZI)
for P, ad, d in ((A, "A", (-0.8, 1.0)), (B, "B", (-2.4, -1.6)), (C, "C", (0.8, -1.6))): ax.text(P[0] + d[0], P[1] + d[1], ad, fontsize=13)
ax.text(H[0] - 0.9, -3.6, "H", color=KIRMIZI, fontsize=13)
ax.text(H[0] - 0.8, 5.4, "12", color=KIRMIZI, fontsize=13, ha="right")
ax.text(8, -3.4, "16", fontsize=13, ha="center"); ax.text(33.5, -3.4, "35", fontsize=13, ha="center")
kenar(ax, A, C, "?", G, d=2.2, renk=MAVI, fs=15)
ax.set_xlim(-3, 54); ax.set_ylim(-4.5, 14.5)
kaydet(fig, __file__)
