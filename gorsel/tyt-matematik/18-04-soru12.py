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
# Alıştırma 12: ABC eşkenar, |BD| = |BC|, m(ABD) = 20, D [AC]'nin dışında. m(ADC) = 150 (m(ABD)'den bağımsız).
s = 3.0
B = np.array([0.0, 0.0]); C = np.array([s, 0.0]); A = np.array([s / 2, s * np.sqrt(3) / 2])
D = s * np.array([np.cos(np.radians(40)), np.sin(np.radians(40))])
print("BD", np.linalg.norm(D - B), "ABD", olc(B, A, D), "BAD", olc(A, B, D), "BDA", olc(D, A, B), "BDC", olc(D, B, C), "ADC", olc(D, A, C))
for t in (5, 20, 35, 50):
    Dt = s * np.array([np.cos(np.radians(60 - t)), np.sin(np.radians(60 - t))]); print(t, olc(Dt, A, C))
fig, ax = sekil(4.4, 3.8)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI); ax.plot(*zip(B, D), color=YAZI); ax.plot(*zip(A, D, C), color=MAVI)
for P, Q in ((A, B), (B, C), (C, A)): centik(ax, P, Q)
centik(ax, B, D)
nokta(ax, *A, "A", dx=-0.15, dy=0.18); nokta(ax, *B, "B", dx=-0.38, dy=-0.3); nokta(ax, *C, "C", dx=0.1, dy=-0.3)
nokta(ax, *D, "D", dx=0.13, dy=0.05)
aci(ax, B, A, D, r=1.1, ad="20°", renk=KIRMIZI)
aci(ax, D, A, C, r=0.3, ad="", renk=MAVI)
ax.text(D[0] - 0.62, D[1] - 0.12, "?", color=MAVI, fontsize=14)
ax.set_xlim(-0.6, s + 0.6); ax.set_ylim(-0.6, A[1] + 0.5)
kaydet(fig, __file__)
