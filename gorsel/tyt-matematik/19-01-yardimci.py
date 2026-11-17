import sys; sys.path.insert(0, "tools")
from cizim import *

def centik(ax, P, Q, n=1, renk=SOLUK, L=0.13, ara=0.09):
    """[PQ] kenarının ortasına n çentik (eş kenar işareti)."""
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]]); M = (P + Q) / 2
    for k in range(n):
        c = M + (k - (n - 1) / 2) * ara * u
        ax.plot(*zip(c - L * v, c + L * v), color=renk, lw=1.6)

def olc(K, P, Q):
    a, b = np.asarray(P) - K, np.asarray(Q) - K
    return round(float(np.degrees(np.arccos(np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b)))), 3)

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P) - np.asarray(Q))), 3)

def dik(ax, K, P, Q, k=0.25, renk=YAZI):
    K = np.asarray(K, float)
    a = (np.asarray(P) - K) / np.linalg.norm(np.asarray(P) - K); b = (np.asarray(Q) - K) / np.linalg.norm(np.asarray(Q) - K)
    ax.plot(*zip(K + k * a, K + k * (a + b), K + k * b), color=renk, lw=1.3)

def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])

# ABC ≅ DEF, |BC| = |EF| = 10, A'dan inen yükseklik 6. DEF, ABC'nin 180° döndürülmüş hâli.
B = np.array([0.0, 0.0]); C = np.array([10.0, 0.0]); A = np.array([3.0, 6.0]); H = np.array([3.0, 0.0]); M = (B + C) / 2
def don(P): return np.array([22.0, 6.0]) - P
D, E, F, Hd, Md = don(A), don(B), don(C), don(H), don(M)
print("AB", uz(A, B), "DE", uz(D, E), "AC", uz(A, C), "DF", uz(D, F), "EF", uz(E, F), "h", uz(D, Hd))
fig, ax = sekil(6.5, 2.8)
ax.set_aspect("equal"); ax.axis("off")
for P, Q, R, Hh, Mm in ((A, B, C, H, M), (D, E, F, Hd, Md)):
    ax.plot(*zip(P, Q, R, P), color=YAZI)
    ax.plot(*zip(P, Hh), color=MAVI, lw=1.8); ax.plot(*zip(P, Mm), color=YESIL, lw=1.8, ls="--")
    dik(ax, Hh, P, R, k=0.5, renk=MAVI)
    centik(ax, P, Q, 1, L=0.3, ara=0.22); centik(ax, P, R, 2, L=0.3, ara=0.22); centik(ax, Q, R, 3, L=0.3, ara=0.22)
nokta(ax, *A, "A", dx=-0.2, dy=0.35); nokta(ax, *B, "B", dx=-0.8, dy=-0.5); nokta(ax, *C, "C", dx=0.3, dy=-0.5)
nokta(ax, *D, "D", dx=-0.2, dy=-1.1); nokta(ax, *E, "E", dx=0.3, dy=0.1); nokta(ax, *F, "F", dx=-0.85, dy=0.1)
ax.text(2.6, 3.0, "6", ha="right", va="center", color=MAVI)
ax.text(19.4, 3.0, "?", ha="left", va="center", color=MAVI, fontsize=14)
ax.text(5.0, -0.5, "10", ha="center", va="top")
ax.set_xlim(-1.2, 23.2); ax.set_ylim(-1.5, 7.4)
kaydet(fig, __file__)
