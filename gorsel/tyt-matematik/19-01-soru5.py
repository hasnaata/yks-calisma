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

# Alıştırma soru 5: |AB| = |AD|, |CB| = |CD|. m(DAC) = 32, m(ADC) = 118 -> m(ACD) = 30, m(BCD) = 60.
A = np.array([0.0, 0.0]); C = np.array([7.0, 0.0])
ad_ = 7 * np.sin(np.radians(30)) / np.sin(np.radians(118))
D = A + ad_ * yon(-32); B = A + ad_ * yon(32)
print("DAC", olc(A, D, C), "ADC", olc(D, A, C), "ACD", olc(C, A, D), "BCD", olc(C, B, D), "AB", uz(A, B), "AD", uz(A, D), "CB", uz(C, B), "CD", uz(C, D))
fig, ax = sekil(5.6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(A, C), color=YAZI, lw=1.6)
centik(ax, A, B, 1); centik(ax, A, D, 1); centik(ax, C, B, 2); centik(ax, C, D, 2)
aci(ax, A, C, D, r=1.0, renk=MAVI)
ax.text(*(A + 1.45 * yon(-14)), "32°", color=MAVI, ha="center", va="center", fontsize=12)
aci(ax, D, C, A, r=0.4, ad="118°", renk=YESIL)
aci(ax, C, D, B, r=0.8, renk=KIRMIZI)
ax.text(*(C + 1.15 * yon(160)), "x", color=KIRMIZI, ha="center", va="center", fontsize=13)
nokta(ax, *A, "A", dx=-0.45, dy=-0.12); nokta(ax, *B, "B", dx=-0.1, dy=0.2); nokta(ax, *C, "C", dx=0.15, dy=-0.12); nokta(ax, *D, "D", dx=-0.1, dy=-0.5)
ax.set_xlim(-0.8, 7.7); ax.set_ylim(D[1] - 0.7, B[1] + 0.7)
kaydet(fig, __file__)
