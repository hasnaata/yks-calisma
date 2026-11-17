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
# Alıştırma 6: |AB| = |AC|, D ∈ [BC], |AD| = |DC|, m(BAD) = 60, m(C) = x = 40.
L = 5.0
B = np.array([0.0, 0.0]); C = np.array([L, 0.0]); A = np.array([L / 2, L / 2 * np.tan(np.radians(40))])
M = (A + C) / 2; n = np.array([-(C - A)[1], (C - A)[0]])  # AC'nin orta dikmesi x eksenini D'de keser
D = M + (-M[1] / n[1]) * n
print("AB", np.linalg.norm(A - B), "AC", np.linalg.norm(A - C), "AD", np.linalg.norm(A - D), "DC", np.linalg.norm(D - C))
print("BAD", olc(A, B, D), "C", olc(C, A, B), "DAC", olc(A, D, C), "BAC", olc(A, B, C))
fig, ax = sekil(5.4, 2.8)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI); ax.plot(*zip(A, D), color=YAZI)
centik(ax, A, B); centik(ax, A, C)
centik(ax, A, D, 2, renk=MAVI); centik(ax, D, C, 2, renk=MAVI)
nokta(ax, *A, "A", dx=-0.12, dy=0.18); nokta(ax, *B, "B", dx=-0.4, dy=-0.3); nokta(ax, *C, "C", dx=0.1, dy=-0.3)
nokta(ax, *D, "D", dx=-0.12, dy=-0.45)
aci(ax, A, B, D, r=0.55, ad="60°", renk=KIRMIZI)
aci(ax, C, A, B, r=0.8, ad="x", renk=MAVI)
ax.set_xlim(-0.6, L + 0.6); ax.set_ylim(-0.6, A[1] + 0.5)
kaydet(fig, __file__)
