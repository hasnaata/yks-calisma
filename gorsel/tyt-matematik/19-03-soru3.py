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
# Soru 3: d1 ∥ d2 ∥ d3. |AB|=6, |BC|=9, |DE|=4, |EF|=x (6).
a1 = 140; C = np.array([12.0, 0.0]); B = C + 9 * yon(a1); A = C + 15 * yon(a1)
a2 = np.degrees(np.arcsin(B[1] / 6)); F = np.array([14.0, 0.0]); E = F + 6 * yon(a2); D = F + 10 * yon(a2)
print("AB", uz(A, B), "BC", uz(B, C), "DE", uz(D, E), "EF", uz(E, F), "yB", B[1], "yE", E[1], "yA", A[1], "yD", D[1])
fig, ax = sekil(5.5, 4.4)
ax.set_aspect("equal"); ax.axis("off")
x0, x1 = -1.0, 19.0
for y, ad in ((A[1], "d₁"), (B[1], "d₂"), (0, "d₃")):
    ax.annotate("", xy=(x1, y), xytext=(x0, y), arrowprops=dict(arrowstyle="<->", color=MAVI, lw=1.8))
    ax.text(x1 + 0.3, y, ad, color=MAVI, va="center", fontsize=13)
ax.plot(*zip(C - 0.9 * yon(a1), A + 0.9 * yon(a1)), color=YAZI)
ax.plot(*zip(F - 0.9 * yon(a2), D + 0.9 * yon(a2)), color=YAZI)
nokta(ax, *A, "A", dx=-0.3, dy=0.45); nokta(ax, *B, "B", dx=-0.4, dy=0.45); nokta(ax, *C, "C", dx=-1.2, dy=-1.0)
nokta(ax, *D, "D", dx=0.5, dy=-1.0); nokta(ax, *E, "E", dx=0.5, dy=-1.0); nokta(ax, *F, "F", dx=0.5, dy=-1.0)
kenar(ax, A, B, "6", (20, 0), d=0.8); kenar(ax, B, C, "9", (20, 0), d=0.8)
kenar(ax, D, E, "4", (0, 0), d=0.8); kenar(ax, E, F, "x", (0, 0), d=0.8)
ax.set_xlim(x0 - 0.3, x1 + 1.5); ax.set_ylim(-1.6, A[1] + 1.4)
kaydet(fig, __file__)
