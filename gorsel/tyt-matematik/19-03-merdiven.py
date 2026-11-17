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
# Soru 8: A biçimli merdiven. |AB|=|AC|=180 cm, |AD|=|AE|=120 cm, |DE|=40 cm, [DE] ∥ zemin -> |BC|=60 cm.
B = np.array([0.0, 0.0]); C = np.array([60.0, 0.0]); A = np.array([30.0, np.sqrt(180**2 - 30**2)])
D = A + (120 / 180) * (B - A); E = A + (120 / 180) * (C - A)
print("AB", uz(A, B), "AC", uz(A, C), "AD", uz(A, D), "DE", uz(D, E), "BC", uz(B, C), "egim", D[1] - E[1])
G = (A + B + C) / 3
fig, ax = sekil(3.6, 5.0)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-40, 100], [0, 0], color=SOLUK, lw=1.4)
for k in range(-36, 100, 10): ax.plot([k, k - 6], [0, -6], color=CIZGI, lw=1)
ax.plot(*zip(B, A, C), color=YAZI, lw=3)
ax.plot(*zip(D, E), color=MAVI, lw=3)
nokta(ax, *A, "A", dx=-4, dy=7); nokta(ax, *B, "B", dx=-14, dy=6); nokta(ax, *C, "C", dx=5, dy=6)
nokta(ax, *D, "D", dx=-15, dy=-3); nokta(ax, *E, "E", dx=6, dy=-3)
kenar(ax, A, D, "120", G, d=20); kenar(ax, D, B, "60", G, d=14)
ax.text(*(D + E) / 2 + np.array([0, 7]), "40", ha="center", va="center", color=MAVI, fontsize=13)
ax.set_xlim(-40, 100); ax.set_ylim(-10, A[1] + 15)
kaydet(fig, __file__)
