import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P) - np.asarray(Q))), 3)
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kenar(ax, P, Q, metin, G, d=0.45, renk=YAZI, fs=13):
    """[PQ] kenarının ortasına, G noktasından uzak tarafa etiket."""
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def centik(ax, P, Q, n=1, renk=SOLUK, L=0.18, ara=0.12):
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]]); M = (P + Q) / 2
    for k in range(n):
        c = M + (k - (n - 1) / 2) * ara * u
        ax.plot(*zip(c - L * v, c + L * v), color=renk, lw=1.6)

# Orta taban: |AB|=10, |AC|=12, |BC|=14; D ve E orta noktalar -> |DE|=7.
B = np.array([0.0, 0.0]); C = np.array([14.0, 0.0])
x = 152 / 28; A = np.array([x, np.sqrt(100 - x**2)])
D = (A + B) / 2; E = (A + C) / 2
print("AB", uz(A, B), "AC", uz(A, C), "DE", uz(D, E), "egim", D[1] - E[1])
G = (A + B + C) / 3
fig, ax = sekil(5.5, 4.0)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(D, E), color=MAVI, lw=2.6)
centik(ax, A, D, 1); centik(ax, D, B, 1); centik(ax, A, E, 2); centik(ax, E, C, 2)
nokta(ax, *A, "A", dx=-0.3, dy=0.35); nokta(ax, *B, "B", dx=-0.9, dy=-0.6); nokta(ax, *C, "C", dx=0.3, dy=-0.6)
nokta(ax, *D, "D", dx=-1.0, dy=0.0); nokta(ax, *E, "E", dx=0.35, dy=0.1)
kenar(ax, A, D, "5", G, d=0.6); kenar(ax, D, B, "5", G, d=0.6); kenar(ax, A, E, "6", G, d=0.6); kenar(ax, E, C, "6", G, d=0.6)
ax.text(*(D + E) / 2 + np.array([0, 0.5]), "7", ha="center", va="center", color=MAVI, fontsize=14)
ax.text(7, -0.8, "14", ha="center", va="center", fontsize=13)
ax.set_xlim(-1.3, 15.3); ax.set_ylim(-1.5, A[1] + 1.0)
kaydet(fig, __file__)
