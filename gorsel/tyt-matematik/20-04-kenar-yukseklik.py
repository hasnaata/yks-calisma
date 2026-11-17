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

# Aynı üçgen: |BC|=14, |AC|=15, h_a=12. B'den [AC]'ye: h_b = 14*12/15 = 11,2.
B, C = np.array([0.0, 0.0]), np.array([14.0, 0.0]); H = np.array([5.0, 0.0]); A = np.array([5.0, 12.0])
E = dik_ayak(A, C, B)
print("hb", uz(B, E), "beklenen", 14 * 12 / 15)
G = (A + B + C) / 3
fig, ax = sekil(5.2, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, H), color=MAVI, lw=2.2); ax.plot(*zip(B, E), color=YESIL, lw=2.2)
dik(ax, H, A, C, k=0.75, renk=MAVI); dik(ax, E, B, C, k=0.75, renk=YESIL)
nokta(ax, *A, "A", dx=-0.35, dy=0.45); nokta(ax, *B, "B", dx=-0.9, dy=-0.9); nokta(ax, *C, "C", dx=0.3, dy=-0.9)
nokta(ax, *H, "H", dx=-0.35, dy=-1.25, renk=MAVI); nokta(ax, *E, "E", dx=0.35, dy=0.2, renk=YESIL)
ax.text(9.5, -1.0, "14", fontsize=14, ha="center", va="center")
P = A + 0.3 * (C - A); ax.text(P[0] + 0.75, P[1] + 0.45, "15", fontsize=14, ha="center", va="center")
ax.text(A[0] - 0.35, 8.6, "12", color=MAVI, fontsize=14, ha="right")
M = (B + E) / 2
ax.text(M[0] - 0.2, M[1] + 0.8, r"$h_b = ?$", color=YESIL, fontsize=14, ha="center", rotation=np.degrees(np.arctan2(E[1], E[0])))
ax.set_xlim(-1.2, 15.2); ax.set_ylim(-2.2, 13.2)
kaydet(fig, __file__)
