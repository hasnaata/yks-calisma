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
# Soru 12: çadır ön yüzü, ikizkenar üçgen; taban 3 m, yükseklik 2,4 m; ip yerden 0,8 m'de, tabana paralel -> ip 2 m.
B = np.array([0.0, 0.0]); C = np.array([3.0, 0.0]); A = np.array([1.5, 2.4]); H = np.array([1.5, 0.0])
t = (2.4 - 0.8) / 2.4; D = A + t * (B - A); E = A + t * (C - A)
print("D", D, "E", E, "DE", uz(D, E))
fig, ax = sekil(4.6, 4.0)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-0.5, 3.6], [0, 0], color=SOLUK, lw=1.4)
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=SARI_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(A, H), color=SOLUK, lw=1.5, ls="--")
ax.plot(*zip(H + [0, 0.15], H + [0.15, 0.15], H + [0.15, 0]), color=SOLUK, lw=1.2)
ax.plot(*zip(D, E), color=MAVI, lw=2.6)
nokta(ax, *A, "A", dx=-0.08, dy=0.1); nokta(ax, *B, "B", dx=-0.25, dy=-0.25); nokta(ax, *C, "C", dx=0.08, dy=-0.25)
nokta(ax, *D, "D", dx=-0.3, dy=-0.05); nokta(ax, *E, "E", dx=0.1, dy=-0.05)
ax.annotate("", xy=(-0.35, 2.4), xytext=(-0.35, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.plot([-0.45, 1.35], [2.4, 2.4], color=SOLUK, lw=0.8, ls=":")
ax.text(-0.45, 1.2, "2,4 m", ha="right", va="center", fontsize=12, color=SOLUK)
ax.annotate("", xy=(3.35, 0.8), xytext=(3.35, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.plot([E[0] + 0.4, 3.45], [0.8, 0.8], color=SOLUK, lw=0.8, ls=":")
ax.text(3.45, 0.4, "0,8 m", ha="left", va="center", fontsize=12, color=SOLUK)
ax.text(1.5, -0.25, "3 m", ha="center", va="center", fontsize=12)
ax.text(1.0, 0.95, "ip", ha="center", va="center", fontsize=12, color=MAVI)
ax.set_xlim(-1.15, 4.2); ax.set_ylim(-0.45, 2.75)
kaydet(fig, __file__)
