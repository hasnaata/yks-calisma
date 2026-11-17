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
# Soru 10: dik üçgen park. |AB|=30, |AC|=40, |BC|=50 m; D, E, F orta noktalar. Yol A->D->E->F = 15+25+15 = 55 m.
A = np.array([0.0, 0.0]); B = np.array([0.0, 30.0]); C = np.array([40.0, 0.0])
D = (A + B) / 2; E = (A + C) / 2; F = (B + C) / 2
print("AD", uz(A, D), "DE", uz(D, E), "EF", uz(E, F), "DF", uz(D, F), "BC", uz(B, C))
G = (A + B + C) / 3
fig, ax = sekil(5.2, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=YESIL_ACIK, edgecolor=YAZI, lw=2.2))
for P, Q in ((D, E), (E, F), (F, D)): ax.plot(*zip(P, Q), color=SOLUK, lw=1.8, ls="--")
ax.plot(*zip(A, D, E, F), color=KIRMIZI, lw=2.6)
ax.plot(*zip(A + [0, 2.2], A + [2.2, 2.2], A + [2.2, 0]), color=YAZI, lw=1.3)
centik(ax, A, D, 1, L=0.9, ara=0.6); centik(ax, D, B, 1, L=0.9, ara=0.6)
centik(ax, A, E, 2, L=0.9, ara=0.6); centik(ax, E, C, 2, L=0.9, ara=0.6)
centik(ax, B, F, 3, L=0.9, ara=0.6); centik(ax, F, C, 3, L=0.9, ara=0.6)
nokta(ax, *A, "A", dx=-3.2, dy=-1.2); nokta(ax, *B, "B", dx=-3.0, dy=0.8); nokta(ax, *C, "C", dx=1.0, dy=-1.5)
nokta(ax, *D, "D", dx=-3.2, dy=-0.8); nokta(ax, *E, "E", dx=0.8, dy=1.0); nokta(ax, *F, "F", dx=1.0, dy=1.0)
def olcu(P, Q, metin, kay, d):
    P, Q = np.asarray(P, float) + kay, np.asarray(Q, float) + kay
    ax.annotate("", xy=Q, xytext=P, arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.1))
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]]) * d; r = np.degrees(np.arctan2(u[1], u[0]))
    if r > 90 or r < -90: r -= 180
    ax.text(*((P + Q) / 2 + v), metin, ha="center", va="center", fontsize=12, color=SOLUK, rotation=r)
olcu(A, B, "30 m", np.array([-6.5, 0]), 2.2)
olcu(A, C, "40 m", np.array([0, -6.5]), -2.2)
olcu(B, C, "50 m", np.array([3.6, 4.8]), 2.2)
ax.set_xlim(-13, 48); ax.set_ylim(-11, 38)
kaydet(fig, __file__)
