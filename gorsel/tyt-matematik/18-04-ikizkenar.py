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

def dik(ax, K, P, Q, k=0.25, renk=YAZI):
    a = (np.asarray(P) - K) / np.linalg.norm(np.asarray(P) - K); b = (np.asarray(Q) - K) / np.linalg.norm(np.asarray(Q) - K)
    ax.plot(*zip(K + k * a, K + k * (a + b), K + k * b), color=renk, lw=1.3)

# |AB| = |AC|, m(A) = 40, m(B) = m(C) = 70.
B = np.array([0.0, 0.0]); C = np.array([3.0, 0.0]); A = np.array([1.5, 1.5 * np.tan(np.radians(70))])
print("A", olc(A, B, C), "B", olc(B, A, C), "C", olc(C, A, B))
fig, ax = sekil(4.2, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI)
centik(ax, A, B); centik(ax, A, C)
nokta(ax, *A, "A", dx=-0.1, dy=0.18); nokta(ax, *B, "B", dx=-0.35, dy=-0.3); nokta(ax, *C, "C", dx=0.1, dy=-0.3)
aci(ax, A, B, C, r=0.75, ad="40°", renk=MAVI)
aci(ax, B, C, A, r=0.45, ad="70°", renk=YESIL)
aci(ax, C, A, B, r=0.45, ad="70°", renk=YESIL)
ax.text(1.5, -0.35, "taban", ha="center", va="top", color=SOLUK, fontsize=12)
ax.text(0.35, 2.3, "yan kenar", ha="right", color=SOLUK, fontsize=12, rotation=70)
ax.text(2.65, 2.3, "yan kenar", ha="left", color=SOLUK, fontsize=12, rotation=-70)
ax.set_xlim(-1.0, 4.0); ax.set_ylim(-0.75, A[1] + 0.5)
kaydet(fig, __file__)
