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

# Yüksekliklerin kesim noktası K: dar açılıda içte, dik açılıda dik köşede, geniş açılıda dışta.
def ciz(ax, A, B, C, uzat=False):
    ax.set_aspect("equal"); ax.axis("off")
    ax.plot(*zip(A, B, C, A), color=YAZI, lw=1.8)
    Fa, Fb, Fc = dik_ayak(B, C, A), dik_ayak(C, A, B), dik_ayak(A, B, C)
    M = np.array([C - B, A - C]); K = np.linalg.solve(M, np.array([np.dot(C - B, A), np.dot(A - C, B)]))
    for P, F, rk in ((A, Fa, KIRMIZI), (B, Fb, MAVI), (C, Fc, YESIL)):
        ax.plot(*zip(P, F), color=rk, lw=1.6)
        if uzat:
            ax.plot(*zip(F, K) if np.linalg.norm(F - P) < np.linalg.norm(K - P) else zip(P, K), color=rk, lw=1.3, ls=":")
    if uzat:
        ax.plot(*zip(A, Fb), color=SOLUK, lw=1.1, ls="--"); ax.plot(*zip(A, Fc), color=SOLUK, lw=1.1, ls="--")
    nokta(ax, *K, "", renk=YAZI)
    return K
fig, axs = plt.subplots(1, 3, figsize=(6.4, 2.9))
# dar
A, B, C = np.array([2.2, 3.4]), np.array([0.0, 0.0]), np.array([4.0, 0.0])
K = ciz(axs[0], A, B, C)
for P, ad, d in ((A, "A", (-0.15, 0.2)), (B, "B", (-0.35, -0.4)), (C, "C", (0.1, -0.4))): axs[0].text(P[0] + d[0], P[1] + d[1], ad, fontsize=12)
axs[0].text(K[0] + 0.12, K[1] - 0.6, "K", fontsize=12, fontweight="bold")
axs[0].set_title("Dar açılı:\nK içte", fontsize=12, color=YAZI)
# dik (A = 90)
A, B, C = np.array([0.0, 0.0]), np.array([0.0, 3.0]), np.array([4.0, 0.0])
K = ciz(axs[1], A, B, C)
dik(axs[1], A, B, C, k=0.3)
for P, ad, d in ((A, "A = K", (0.15, -0.5)), (B, "B", (-0.4, 0.05)), (C, "C", (0.1, -0.4))): axs[1].text(P[0] + d[0], P[1] + d[1], ad, fontsize=12)
axs[1].set_title("Dik açılı:\nK dik köşede", fontsize=12, color=YAZI)
# geniş (A geniş)
A, B, C = np.array([1.6, 1.0]), np.array([0.0, 0.0]), np.array([4.0, 0.0])
K = ciz(axs[2], A, B, C, uzat=True)
for P, ad, d in ((A, "A", (0.12, 0.3)), (B, "B", (-0.35, -0.4)), (C, "C", (0.1, -0.4))): axs[2].text(P[0] + d[0], P[1] + d[1], ad, fontsize=12)
axs[2].text(K[0] + 0.2, K[1] - 0.05, "K", fontsize=12, fontweight="bold")
axs[2].set_title("Geniş açılı:\nK dışta", fontsize=12, color=YAZI)
print("K genis", K)
for a in axs: a.set_xlim(-0.6, 4.6); a.set_ylim(-0.7, 4.4)
axs[2].set_ylim(-0.7, max(4.4, K[1] + 0.4))
fig.subplots_adjust(wspace=0.08)
kaydet(fig, __file__)
