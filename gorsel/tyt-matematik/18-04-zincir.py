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

# D ∈ [BC], |AB| = |AD| = |DC|, m(C) = 32. m(DAC)=32, m(ADB)=64, m(ABD)=64, m(BAD)=52, m(BAC)=84.
s = 3.0
D = np.array([0.0, 0.0]); C = np.array([s, 0.0])
A = s * np.array([np.cos(np.radians(116)), np.sin(np.radians(116))]); B = np.array([2 * A[0], 0.0])
print("AB", np.linalg.norm(A - B), "AD", np.linalg.norm(A - D), "DC", s)
print("C", olc(C, A, D), "DAC", olc(A, D, C), "ADB", olc(D, A, B), "ABD", olc(B, A, D), "BAD", olc(A, B, D), "BAC", olc(A, B, C))
fig, ax = sekil(6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(A, D), color=YAZI)
centik(ax, A, B); centik(ax, A, D); centik(ax, D, C)
nokta(ax, *A, "A", dx=-0.12, dy=0.2); nokta(ax, *B, "B", dx=-0.4, dy=-0.35); nokta(ax, *C, "C", dx=0.1, dy=-0.35)
nokta(ax, *D, "D", dx=-0.1, dy=-0.5)
aci(ax, C, A, D, r=0.9, ad="32°", renk=MAVI)
aci(ax, A, D, C, r=0.9, ad="32°", renk=MAVI)
aci(ax, D, A, B, r=0.4, ad="64°", renk=KIRMIZI)
aci(ax, B, D, A, r=0.4, ad="64°", renk=KIRMIZI)
aci(ax, A, B, D, r=0.7, ad="52°", renk=YESIL)
ax.set_xlim(B[0] - 0.6, s + 0.6); ax.set_ylim(-0.75, A[1] + 0.55)
kaydet(fig, __file__)
