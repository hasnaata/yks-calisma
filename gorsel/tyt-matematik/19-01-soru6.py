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

# Alıştırma soru 6: ABCD kare, |BE| = |CF|, m(BAE) = 28 -> ABE ≅ BCF, m(AGB) = 90.
A = np.array([0.0, 6.0]); B = np.array([0.0, 0.0]); C = np.array([6.0, 0.0]); D = np.array([6.0, 6.0])
be = 6 * np.tan(np.radians(28)); E = np.array([be, 0.0]); F = np.array([6.0, be])
u, v = E - A, F - B; s = np.linalg.solve(np.array([u, -v]).T, B - A); G = A + s[0] * u
print("BE", round(be, 3), "CF", uz(C, F), "BAE", olc(A, B, E), "CBF", olc(B, C, F), "AGB", olc(G, A, B))
fig, ax = sekil(4.4, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(A, E), color=MAVI); ax.plot(*zip(B, F), color=YESIL)
centik(ax, B, E, 1); centik(ax, C, F, 1)
dik(ax, B, A, C, k=0.35); dik(ax, C, B, D, k=0.35)
aci(ax, A, B, E, r=1.1, renk=MAVI)
ax.text(*(A + 1.55 * yon(-76)), "28°", color=MAVI, ha="center", va="center", fontsize=12)
aci(ax, G, A, B, r=0.4, renk=KIRMIZI)
ax.text(*(G + 0.75 * yon(170)), "x", color=KIRMIZI, ha="center", va="center", fontsize=13)
nokta(ax, *A, "A", dx=-0.45, dy=0.1); nokta(ax, *B, "B", dx=-0.45, dy=-0.45); nokta(ax, *C, "C", dx=0.15, dy=-0.45)
nokta(ax, *D, "D", dx=0.15, dy=0.1); nokta(ax, *E, "E", dx=-0.1, dy=-0.5); nokta(ax, *F, "F", dx=0.18, dy=-0.1)
nokta(ax, *G, "G", dx=0.12, dy=0.18)
ax.set_xlim(-0.8, 6.8); ax.set_ylim(-0.8, 6.7)
kaydet(fig, __file__)
