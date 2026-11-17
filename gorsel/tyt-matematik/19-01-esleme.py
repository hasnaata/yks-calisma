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

# ABC ≅ DEF: |AB| = |DE| = 5, |BC| = |EF| = 7, |AC| = |DF| = 6. DEF, ABC'nin aynadaki görüntüsü (E sağda, F solda).
B = np.array([0.0, 0.0]); C = np.array([7.0, 0.0])
ax_ = (25 - 36 + 49) / 14; A = np.array([ax_, np.sqrt(25 - ax_**2)])
def ayna(P): return np.array([16.5 - P[0], P[1]])
D, E, F = ayna(A), ayna(B), ayna(C)
print("AB", uz(A, B), "BC", uz(B, C), "AC", uz(A, C), "DE", uz(D, E), "EF", uz(E, F), "DF", uz(D, F))
print("A", olc(A, B, C), "D", olc(D, E, F), "B", olc(B, A, C), "E", olc(E, D, F))

fig, ax = sekil(6.5, 2.9)
ax.set_aspect("equal"); ax.axis("off")
for P, Q, R in ((A, B, C), (D, E, F)):
    ax.plot(*zip(P, Q, R, P), color=YAZI)
    centik(ax, P, Q, 1, L=0.25, ara=0.17); centik(ax, Q, R, 2, L=0.25, ara=0.17); centik(ax, P, R, 3, L=0.25, ara=0.17)
    aci(ax, P, Q, R, r=0.6, renk=MAVI)
    aci(ax, Q, P, R, r=0.6, renk=YESIL)
    aci(ax, R, P, Q, r=0.6, renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.15, dy=0.25); nokta(ax, *B, "B", dx=-0.55, dy=-0.45); nokta(ax, *C, "C", dx=0.15, dy=-0.45)
nokta(ax, *D, "D", dx=-0.15, dy=0.25); nokta(ax, *E, "E", dx=0.15, dy=-0.45); nokta(ax, *F, "F", dx=-0.55, dy=-0.45)
ax.text(*(A + B) / 2 + np.array([-0.55, 0.0]), "5", ha="right", va="center")
ax.text(*(A + C) / 2 + np.array([0.35, 0.1]), "6", ha="left", va="center")
ax.text(3.5, -0.45, "7", ha="center", va="top")
ax.set_xlim(-0.8, 17.3); ax.set_ylim(-1.0, A[1] + 0.7)
kaydet(fig, __file__)
