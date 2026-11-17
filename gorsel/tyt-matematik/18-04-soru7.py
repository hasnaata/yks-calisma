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
# Alıştırma 7: ABC eşkenar, |CA| = |CD|, m(ACD) = 40, D ile B [AC]'nin farklı yanlarında. m(BAD) = 60 + 70 = 130.
s = 3.0
B = np.array([0.0, 0.0]); C = np.array([s, 0.0]); A = np.array([s / 2, s * np.sqrt(3) / 2])
def don(v, d):
    t = np.radians(d); return np.array([v[0] * np.cos(t) - v[1] * np.sin(t), v[0] * np.sin(t) + v[1] * np.cos(t)])
D = C + don(A - C, -40)   # CA'yı C etrafında saat yönünde 40° döndür (B'den uzağa)
print("CD", np.linalg.norm(D - C), "ACD", olc(C, A, D), "CAD", olc(A, C, D), "BAD", olc(A, B, D), "BCD", olc(C, B, D))
fig, ax = sekil(5, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI); ax.plot(*zip(A, D, C), color=YAZI)
for P, Q in ((A, B), (B, C), (C, A)): centik(ax, P, Q)
centik(ax, C, D)
nokta(ax, *A, "A", dx=-0.12, dy=0.18); nokta(ax, *B, "B", dx=-0.38, dy=-0.3); nokta(ax, *C, "C", dx=-0.05, dy=-0.45)
nokta(ax, *D, "D", dx=0.12, dy=0.05)
aci(ax, C, D, A, r=0.6, ad="40°", renk=KIRMIZI)
ax.set_xlim(-0.6, D[0] + 0.6); ax.set_ylim(-0.65, A[1] + 0.5)
kaydet(fig, __file__)
