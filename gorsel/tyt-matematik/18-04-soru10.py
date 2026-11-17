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
# Alıştırma 10: x = 30. A, C birinci çubukta; B ikinci çubukta. |OA| = |AB| = |BC| = 1, [BC] ⟂ [OB].
x = 30
O = np.array([0.0, 0.0]); u = np.array([1.0, 0.0]); v = np.array([np.cos(np.radians(x)), np.sin(np.radians(x))])
s = 1.6
A = s * u; B = 2 * s * np.cos(np.radians(x)) * v; C = A + 2 * (np.dot(B - A, u)) * u
print("OA", np.linalg.norm(A - O), "AB", np.linalg.norm(B - A), "BC", np.linalg.norm(C - B), "OBC", olc(B, O, C), "BAC", olc(A, B, C), "BCA", olc(C, B, A))
fig, ax = sekil(5.4, 2.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(O, 4.3 * u), color=SOLUK, lw=3); ax.plot(*zip(O, 4.3 * v), color=SOLUK, lw=3)
ax.plot(*zip(A, B, C), color=MAVI)
centik(ax, O, A, renk=MAVI); centik(ax, A, B, renk=MAVI); centik(ax, B, C, renk=MAVI)
dik(ax, B, C, O, k=0.22, renk=MAVI)
nokta(ax, *O, "O", dx=-0.35, dy=-0.1); nokta(ax, *A, "A", dx=-0.1, dy=-0.4); nokta(ax, *B, "B", dx=-0.15, dy=0.2); nokta(ax, *C, "C", dx=-0.1, dy=-0.4)
aci(ax, O, u, v, r=0.75, ad="x", renk=KIRMIZI)
ax.set_xlim(-0.6, 4.5); ax.set_ylim(-0.6, 4.3 * v[1] + 0.2)
kaydet(fig, __file__)
