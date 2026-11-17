import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P) - np.asarray(Q))), 3)
def ucgen(a, b, c):
    """|BC|=a, |CA|=b, |AB|=c. B orijinde, C x ekseninde."""
    x = (c**2 - b**2 + a**2) / (2 * a)
    return np.array([x, np.sqrt(c**2 - x**2)]), np.array([0.0, 0.0]), np.array([float(a), 0.0])
def ucgen_aci(A_, B_, a=6.0):
    """B ve A köşelerindeki açılar (derece) ve |BC|=a ile üçgen."""
    C_ = 180 - A_ - B_; c = a * np.sin(np.radians(C_)) / np.sin(np.radians(A_))
    return c * np.array([np.cos(np.radians(B_)), np.sin(np.radians(B_))]), np.array([0.0, 0.0]), np.array([a, 0.0])
def cevrel(A, B, C):
    """Kenar orta dikmelerin kesim noktası."""
    M = 2 * np.array([B - A, C - A]); r = np.array([B @ B - A @ A, C @ C - A @ A])
    return np.linalg.solve(M, r)
def kenar(ax, P, Q, metin, G, d=0.45, renk=YAZI, fs=13):
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik(ax, K, P, Q, s=0.3, renk=SOLUK):
    """K köşesinde KP ile KQ arasındaki dik açı işareti."""
    u = (P - K) / np.linalg.norm(P - K) * s; v = (Q - K) / np.linalg.norm(Q - K) * s
    ax.plot(*zip(K + u, K + u + v, K + v), color=renk, lw=1.3)
def aci_olc(K, P, Q):
    u, v = P - K, Q - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)
def centik(ax, P, Q, n=1, renk=SOLUK, L=0.18, ara=0.12):
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]]); M = (P + Q) / 2
    for k in range(n):
        c = M + (k - (n - 1) / 2) * ara * u
        ax.plot(*zip(c - L * v, c + L * v), color=renk, lw=1.6)
def kesis(P, Q, R, S):
    """PQ doğrusu ile RS doğrusunun kesim noktası."""
    t = np.linalg.solve(np.array([Q - P, R - S]).T, R - P); return P + t[0] * (Q - P)

# Alıştırma soru 4: |AB|=8, |AC|=11, |BC|=13. d, [BC]'nin kenar orta dikmesi; [AC]'yi D'de keser.
# |DB| = |DC|, Ç(ABD) = |AB| + |AC| = 19.
A, B, C = ucgen(13, 11, 8)
M = (B + C) / 2
D = kesis(M, M + np.array([0.0, 1.0]), A, C)
print("DB", uz(D, B), "DC", uz(D, C), "AD", uz(A, D), "Ç(ABD)", uz(A, B) + uz(A, D) + uz(D, B))
Gm = (A + B + C) / 3

fig, ax = sekil(5.6, 3.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, D), color=MAVI, lw=2)
ax.plot(*zip(M - np.array([0, 0.6]), D + np.array([0, 0.9])), color=KIRMIZI, lw=2, ls="--")
ax.text(M[0] + 0.3, D[1] + 0.8, "d", color=KIRMIZI, fontsize=14, va="center")
dik(ax, M, C, D, s=0.4, renk=KIRMIZI)
centik(ax, B, M, 1); centik(ax, M, C, 1)
nokta(ax, *A, "A", dx=-0.2, dy=0.3); nokta(ax, *B, "B", dx=-0.6, dy=-0.5); nokta(ax, *C, "C", dx=0.15, dy=-0.5)
nokta(ax, *D, "D", dx=0.25, dy=-0.95, renk=KIRMIZI); nokta(ax, *M, "M", dx=0.2, dy=-0.7, renk=KIRMIZI)
kenar(ax, A, B, "8", Gm, d=0.45)
ax.annotate("", xy=C + np.array([0, -1.3]), xytext=B + np.array([0, -1.3]), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(6.5, -1.75, "13", ha="center", va="center", fontsize=13)
u = (C - A) / np.linalg.norm(C - A); v = np.array([-u[1], u[0]])
if np.dot(v, A - Gm) < 0: v = -v
ax.annotate("", xy=C + 0.6 * v, xytext=A + 0.6 * v, arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(*((A + C) / 2 + 1.0 * v), "11", ha="center", va="center", fontsize=13)
ax.set_xlim(-1.0, 14.2); ax.set_ylim(-2.1, A[1] + 1.2)
kaydet(fig, __file__)
