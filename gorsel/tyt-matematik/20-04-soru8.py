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

# Dik üçgen tarla: m(A)=90, |AB|=30, |AC|=40, |BC|=50. A'dan [BC]'ye en kısa yol = 30*40/50 = 24.
A, B, C = np.array([0.0, 0.0]), np.array([0.0, 30.0]), np.array([40.0, 0.0])
H = dik_ayak(B, C, A)
print("BC", uz(B, C), "AH", uz(A, H))
G = (A + B + C) / 3
fig, ax = sekil(5.2, 4.0)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([A, B, C], color=YESIL_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, H), color=KIRMIZI, lw=2, ls="--")
dik(ax, A, B, C, k=1.8); dik(ax, H, A, C, k=1.8, renk=KIRMIZI)
nokta(ax, *A, "", renk=MAVI)
for P, ad, d in ((A, "A", (-2.6, -2.6)), (B, "B", (-2.6, 0.3)), (C, "C", (0.8, -2.6)), (H, "H", (0.8, 0.8))): ax.text(P[0] + d[0], P[1] + d[1], ad, fontsize=13, color=KIRMIZI if ad == "H" else YAZI)
ax.text(A[0] + 2.5, A[1] - 3.5, "kuyu", color=MAVI, fontsize=12)
kenar(ax, A, B, "30", G, d=2.2); kenar(ax, A, C, "40", G, d=2.4)
M = (A + H) / 2; ax.text(M[0] + 1.4, M[1] - 1.6, "?", color=KIRMIZI, fontsize=15)
ax.set_xlim(-4, 44); ax.set_ylim(-5, 33)
kaydet(fig, __file__)
