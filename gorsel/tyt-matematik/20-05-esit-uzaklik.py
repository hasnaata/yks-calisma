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

# Ders örneği 1: |AB|=10, |AC|=7, |BC|=12. [AB]'nin kenar orta dikmesi [BC]'yi D'de keser.
# |DA| = |DB|, Ç(ADC) = |AC| + |BC| = 19.
A, B, C = ucgen(12, 7, 10)
M = (A + B) / 2
D = kesis(M, M + np.array([-(A - B)[1], (A - B)[0]]), B, C)
print("DA", uz(D, A), "DB", uz(D, B), "Ç(ADC)", uz(A, D) + uz(D, C) + uz(A, C))
Gm = (A + B + C) / 3

fig, ax = sekil(5.6, 3.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([A, D, C], color=MAVI_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, D), color=MAVI, lw=2)
u = (M - D) / np.linalg.norm(M - D)
ax.plot(*zip(D - 0.6 * u, M + 0.7 * u), color=KIRMIZI, lw=2, ls="--")
ax.text(*(D - 0.75 * u + np.array([0.35, 0])), "d", color=KIRMIZI, fontsize=14, ha="center", va="center")
dik(ax, M, A, M + u, s=0.35, renk=KIRMIZI)
centik(ax, A, M, 1); centik(ax, M, B, 1)
centik(ax, D, A, 2, renk=MAVI); centik(ax, B, D, 2, renk=MAVI)
nokta(ax, *A, "A", dx=-0.1, dy=0.3); nokta(ax, *B, "B", dx=-0.6, dy=-0.5); nokta(ax, *C, "C", dx=0.15, dy=-0.5)
nokta(ax, *D, "D", dx=-0.2, dy=-0.7, renk=MAVI); nokta(ax, *M, "M", dx=-0.85, dy=-0.55, renk=KIRMIZI)
kenar(ax, A, C, "7", Gm, d=0.45)
ax.annotate("", xy=C + np.array([0, -1.25]), xytext=B + np.array([0, -1.25]), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(6, -1.6, "12", ha="center", va="center", fontsize=13)
v = np.array([-(A - B)[1], (A - B)[0]]) / 10
n = v / np.linalg.norm(v)
ax.annotate("", xy=A + 1.0 * n, xytext=B + 1.0 * n, arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(*(B + 0.3 * (A - B) + 1.4 * n), "10", ha="center", va="center", fontsize=13)
ax.set_xlim(-2.0, 12.8); ax.set_ylim(-2.0, A[1] + 1.0)
kaydet(fig, __file__)
