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

# ABC eşkenar (kenar 3), [BC] uzatılıyor, |CD| = |CA|. m(ACD)=120, m(CAD)=m(CDA)=30, m(BAD)=90.
B = np.array([0.0, 0.0]); C = np.array([3.0, 0.0]); A = np.array([1.5, 1.5 * np.sqrt(3)]); D = np.array([6.0, 0.0])
print("BAC", olc(A, B, C), "ACD", olc(C, A, D), "CAD", olc(A, C, D), "CDA", olc(D, A, C), "BAD", olc(A, B, D))
fig, ax = sekil(6, 3.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(C, D, A), color=KIRMIZI)
for P, Q in ((A, B), (B, C), (C, A)): centik(ax, P, Q)
centik(ax, C, D, renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.12, dy=0.2); nokta(ax, *B, "B", dx=-0.35, dy=-0.35); nokta(ax, *C, "C", dx=-0.05, dy=-0.45)
nokta(ax, *D, "D", dx=0.12, dy=-0.35)
aci(ax, B, C, A, r=0.5, ad="60°", renk=MAVI)
aci(ax, A, B, C, r=0.45, ad="60°", renk=MAVI)
aci(ax, C, D, A, r=0.4, ad="120°", renk=KIRMIZI)
aci(ax, A, C, D, r=0.85, ad="30°", renk=KIRMIZI)
aci(ax, D, A, C, r=1.1, ad="30°", renk=KIRMIZI)
ax.set_xlim(-0.6, 6.6); ax.set_ylim(-0.7, A[1] + 0.55)
kaydet(fig, __file__)
