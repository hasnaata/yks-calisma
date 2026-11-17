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

# Alıştırma soru 4: |AO| = |OC| = 6, |BO| = |OD| = 10, m(AOB) = 120 -> |AB| = |CD| = 14. 3x - 4 = x + 8 -> x = 6.
Oo = np.array([0.0, 0.0])
A = Oo + 0.6 * yon(170); C = -A
B = Oo + 1.0 * yon(290); D = -B
print("AB", uz(A, B) * 10, "CD", uz(C, D) * 10, "AOB", olc(Oo, A, B))
fig, ax = sekil(5, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B), color=YAZI); ax.plot(*zip(C, D), color=YAZI)
ax.plot(*zip(A, C), color=YAZI); ax.plot(*zip(B, D), color=YAZI)
centik(ax, A, Oo, 1, L=0.05, ara=0.035); centik(ax, Oo, C, 1, L=0.05, ara=0.035)
centik(ax, B, Oo, 2, L=0.05, ara=0.035); centik(ax, Oo, D, 2, L=0.05, ara=0.035)
nokta(ax, *A, "A", dx=-0.17, dy=0.03); nokta(ax, *B, "B", dx=-0.04, dy=-0.17); nokta(ax, *C, "C", dx=0.06, dy=-0.05)
nokta(ax, *D, "D", dx=-0.03, dy=0.07); nokta(ax, *Oo, "O", dx=-0.16, dy=-0.2)
ax.text(*((A + B) / 2 + np.array([-0.08, -0.05])), "3x − 4", ha="right", va="center")
ax.text(*((C + D) / 2 + np.array([0.08, 0.05])), "x + 8", ha="left", va="center")
ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.15, 1.15)
kaydet(fig, __file__)
