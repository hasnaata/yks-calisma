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

# m(A)=50, m(B)=70, m(C)=60. [BE] ⊥ [AC], [CF] ⊥ [AB], K kesişim. m(BKC) = 180 - 50 = 130.
B, C = np.array([0.0, 0.0]), np.array([6.0, 0.0])
t = 6 * np.sin(np.radians(60)) / np.sin(np.radians(50))
A = B + t * np.array([np.cos(np.radians(70)), np.sin(np.radians(70))])
E, F = dik_ayak(A, C, B), dik_ayak(A, B, C)
M = np.array([C - B, A - C]); K = np.linalg.solve(M, np.array([np.dot(C - B, A), np.dot(A - C, B)]))
u, v = B - K, C - K
print("A", np.degrees(np.arccos(np.dot(B - A, C - A) / uz(A, B) / uz(A, C))), "BKC", np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v))))
fig, ax = sekil(4.6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, E), color=MAVI, lw=1.8); ax.plot(*zip(C, F), color=YESIL, lw=1.8)
ax.plot(*zip(B, K, C), color=KIRMIZI, lw=0)  # yalnız konum
dik(ax, E, A, B, k=0.28, renk=MAVI); dik(ax, F, B, C, k=0.28, renk=YESIL)
aci(ax, A, B, C, r=0.6, ad="50°", renk=YAZI)
aci(ax, K, B, C, r=0.45, ad="", renk=KIRMIZI)
ax.text(K[0], K[1] - 0.95, "?", color=KIRMIZI, fontsize=15, ha="center")
nokta(ax, *K, "", renk=YAZI); ax.text(K[0] - 0.1, K[1] + 0.3, "K", fontsize=13, ha="center", fontweight="bold")
for P, ad, d in ((A, "A", (-0.15, 0.25)), (B, "B", (-0.45, -0.4)), (C, "C", (0.15, -0.4)), (E, "E", (0.2, 0.05)), (F, "F", (-0.45, 0.05))): ax.text(P[0] + d[0], P[1] + d[1], ad, fontsize=13)
ax.set_xlim(-0.7, 6.7); ax.set_ylim(-0.7, A[1] + 0.6)
kaydet(fig, __file__)
