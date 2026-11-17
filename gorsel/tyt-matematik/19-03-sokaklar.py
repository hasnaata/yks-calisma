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
# Soru 9: üç paralel cadde, iki yol. |AB|=120, |BC|=180, |DE|=160 m -> |EF|=240, |DF|=400 m.
s = 0.01  # 1 birim = 100 m
a1 = 80; C = np.array([0.0, 0.0]); B = C + 1.8 * yon(a1); A = C + 3.0 * yon(a1)
a2 = 180 - np.degrees(np.arcsin(B[1] / 2.4)); F = np.array([4.0, 0.0]); E = F + 2.4 * yon(a2); D = F + 4.0 * yon(a2)
print("AB", uz(A, B) * 100, "BC", uz(B, C) * 100, "DE", uz(D, E) * 100, "EF", uz(E, F) * 100, "yB", B[1], "yE", E[1], "yA", A[1], "yD", D[1], "Dx", D[0])
fig, ax = sekil(5.5, 4.2)
ax.set_aspect("equal"); ax.axis("off")
x0, x1 = -0.8, 4.8
for y, ad in ((A[1], "1. cadde"), (B[1], "2. cadde"), (0, "3. cadde")):
    ax.fill_between([x0, x1], y - 0.07, y + 0.07, color=MAVI_ACIK, zorder=0)
    ax.plot([x0, x1], [y, y], color=MAVI, lw=2)
    ax.text(x1 + 0.08, y, ad, color=MAVI, va="center", fontsize=12)
ax.plot(*zip(C - 0.25 * yon(a1), A + 0.25 * yon(a1)), color=YAZI)
ax.plot(*zip(F - 0.25 * yon(a2), D + 0.25 * yon(a2)), color=YAZI)
ax.text(*(C - 0.35 * yon(a1)) + np.array([0, -0.05]), "1. yol", ha="center", va="top", fontsize=12)
ax.text(*(F - 0.35 * yon(a2)) + np.array([0, -0.05]), "2. yol", ha="center", va="top", fontsize=12)
nokta(ax, *A, "A", dx=-0.3, dy=0.1); nokta(ax, *B, "B", dx=-0.3, dy=0.1); nokta(ax, *C, "C", dx=-0.3, dy=0.1)
nokta(ax, *D, "D", dx=0.12, dy=0.1); nokta(ax, *E, "E", dx=0.12, dy=0.1); nokta(ax, *F, "F", dx=0.12, dy=0.1)
kenar(ax, A, B, "120 m", (5, 0), d=0.5, fs=12); kenar(ax, B, C, "180 m", (5, 0), d=0.5, fs=12)
kenar(ax, D, E, "160 m", (0, 3), d=0.42, fs=12)
ax.set_xlim(x0 - 0.3, x1 + 1.1); ax.set_ylim(-0.75, A[1] + 0.35)
kaydet(fig, __file__)
