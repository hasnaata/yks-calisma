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

# |AB|=30, |AC|=25, |AH|=24, H ∈ [BC] => |BH|=18, |HC|=7, |BC|=25; C'den [AB]'ye yükseklik = 25*24/30 = 20.
B, C, H, A = np.array([0.0, 0.0]), np.array([25.0, 0.0]), np.array([18.0, 0.0]), np.array([18.0, 24.0])
F = dik_ayak(A, B, C)
print("AB", uz(A, B), "AC", uz(A, C), "CF", uz(C, F))
G = (A + B + C) / 3
fig, ax = sekil(4.6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI); ax.plot(*zip(A, H), color=KIRMIZI, lw=2.2)
ax.plot(*zip(C, F), color=MAVI, lw=1.8, ls="--")
dik(ax, H, A, C, k=1.3, renk=KIRMIZI); dik(ax, F, A, C, k=1.3, renk=MAVI)
for P, ad, d in ((A, "A", (-0.6, 1.0)), (B, "B", (-1.8, -1.6)), (C, "C", (0.7, -1.6))): ax.text(P[0] + d[0], P[1] + d[1], ad, fontsize=13)
ax.text(H[0] - 0.7, -2.6, "H", color=KIRMIZI, fontsize=13)
ax.text(F[0] - 2.4, F[1] - 1.6, "F", color=MAVI, fontsize=13)
P = B + 0.72 * (A - B); ax.text(P[0] - 1.6, P[1] + 0.8, "30", fontsize=13, ha="center"); kenar(ax, A, C, "25", G, d=1.6)
ax.text(H[0] - 0.7, 17.5, "24", color=KIRMIZI, fontsize=13, ha="right")
M = (C + F) / 2; ax.text(M[0] + 0.3, M[1] - 2.3, "?", color=MAVI, fontsize=15, ha="center")
ax.set_xlim(-2.5, 27.5); ax.set_ylim(-3.2, 26.2)
kaydet(fig, __file__)
