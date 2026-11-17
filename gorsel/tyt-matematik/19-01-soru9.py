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

# Alıştırma soru 9: |AB| = 6, |AC| = 10, |BC| = 12. [AD] boyunca katlanınca B, [AC] üzerinde E'ye gelir.
# |AE| = 6, |EC| = 4, |BD| = |DE| = 4,5, |DC| = 7,5. DEC çevresi = 4,5 + 7,5 + 4 = 16.
B = np.array([0.0, 0.0]); C = np.array([12.0, 0.0])
x = 80 / 24; A = np.array([x, np.sqrt(36 - x**2)])
D = np.array([4.5, 0.0]); E = A + 0.6 * (C - A)
print("AB", uz(A, B), "AC", uz(A, C), "AE", uz(A, E), "EC", uz(E, C), "BD", uz(B, D), "DE", uz(D, E), "DC", uz(D, C), "BAD", olc(A, B, D), "DAE", olc(A, D, E))
fig, ax = sekil(6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([D, E, C], closed=True, facecolor=SARI_ACIK, edgecolor="none", zorder=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, D), color=MAVI, ls="--", lw=1.8)
ax.plot(*zip(D, E), color=KIRMIZI, ls="--", lw=1.8)
nokta(ax, *A, "A", dx=-0.2, dy=0.3); nokta(ax, *B, "B", dx=-0.6, dy=-0.5); nokta(ax, *C, "C", dx=0.2, dy=-0.5)
nokta(ax, *D, "D", dx=-0.2, dy=-0.75); nokta(ax, *E, "E", dx=0.1, dy=0.25)
ax.text(*((A + B) / 2 + np.array([-0.35, 0.1])), "6", ha="right", va="center")
ax.text(*(A + 0.3 * (C - A) + np.array([0.15, 0.45])), "10", ha="left", va="center")
ax.annotate("", xy=(0, -1.45), xytext=(12, -1.45), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(6.0, -1.6, "12", ha="center", va="top")
ax.set_xlim(-1.0, 13.0); ax.set_ylim(-2.5, A[1] + 0.8)
kaydet(fig, __file__)
