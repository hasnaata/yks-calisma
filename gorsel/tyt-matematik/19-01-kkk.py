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

# K.K.K.: |AB| = |AD|, |CB| = |CD|, [AC] ortak. m(BAD) = 70, m(BCD) = 50 -> m(B) = m(D) = 120.
A = np.array([0.0, 0.0]); C = np.array([7.0, 0.0])
ab = 7 * np.sin(np.radians(25)) / np.sin(np.radians(120))
B = A + ab * yon(35); D = A + ab * yon(-35)
print("BAD", olc(A, B, D), "BCD", olc(C, B, D), "ABC", olc(B, A, C), "ADC", olc(D, A, C), "AB", uz(A, B), "AD", uz(A, D), "CB", uz(C, B), "CD", uz(C, D))
fig, ax = sekil(5.6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(A, C), color=MAVI, ls="--", lw=1.6)
centik(ax, A, B, 1); centik(ax, A, D, 1); centik(ax, C, B, 2); centik(ax, C, D, 2)
aci(ax, A, B, D, r=0.75, renk=YESIL)
ax.text(1.25, 0.0, "70°", color=YESIL, ha="left", va="center", fontsize=12, bbox=dict(facecolor="white", edgecolor="none", pad=1))
aci(ax, C, D, B, r=0.9, renk=SARI)
ax.text(5.85, 0.0, "50°", color=SARI, ha="right", va="center", fontsize=12, bbox=dict(facecolor="white", edgecolor="none", pad=1))
aci(ax, B, A, C, r=0.35, ad="x", renk=KIRMIZI)
aci(ax, D, C, A, r=0.35, ad="", renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.45, dy=-0.12); nokta(ax, *B, "B", dx=-0.1, dy=0.2); nokta(ax, *C, "C", dx=0.15, dy=-0.12); nokta(ax, *D, "D", dx=-0.1, dy=-0.5)
ax.set_xlim(-0.8, 7.7); ax.set_ylim(D[1] - 0.7, B[1] + 0.7)
kaydet(fig, __file__)
