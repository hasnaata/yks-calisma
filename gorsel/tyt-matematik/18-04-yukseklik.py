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

# |AB| = |AC|, m(A) = 50, m(B) = m(C) = 65, |BC| = 12, [AH] yükseklik.
B = np.array([0.0, 0.0]); C = np.array([6.0, 0.0]); A = np.array([3.0, 3.0 * np.tan(np.radians(65))]); H = np.array([3.0, 0.0])
print("A", olc(A, B, C), "BAH", olc(A, B, H), "HAC", olc(A, H, C), "B", olc(B, A, C), "AHB", olc(H, A, B), "BH", H[0] - B[0], "HC", C[0] - H[0])
fig, ax = sekil(4.6, 5)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(A, H), color=MAVI, lw=1.8)
dik(ax, H, C, A, k=0.3, renk=MAVI)
centik(ax, A, B); centik(ax, A, C)
centik(ax, B, H, 2, renk=MAVI); centik(ax, H, C, 2, renk=MAVI)
nokta(ax, *A, "A", dx=-0.12, dy=0.2); nokta(ax, *B, "B", dx=-0.45, dy=-0.35); nokta(ax, *C, "C", dx=0.12, dy=-0.35)
nokta(ax, *H, "H", dx=-0.15, dy=-0.55, renk=MAVI)
aci(ax, A, B, H, r=1.3, ad="25°", renk=KIRMIZI)
aci(ax, A, H, C, r=1.3, ad="25°", renk=KIRMIZI)
aci(ax, B, C, A, r=0.6, ad="65°", renk=YESIL)
aci(ax, C, A, B, r=0.6, ad="65°", renk=YESIL)
ax.text(1.5, -0.25, "6", ha="center", va="top", color=MAVI); ax.text(4.5, -0.25, "6", ha="center", va="top", color=MAVI)
ax.set_xlim(-0.8, 6.8); ax.set_ylim(-0.9, A[1] + 0.6)
kaydet(fig, __file__)
