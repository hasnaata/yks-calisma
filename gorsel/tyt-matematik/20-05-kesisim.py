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

# Dar açılı ABC (A=70°, B=60°, C=50°). Üç kenar orta dikme K'de kesişir; K üç köşeye eşit uzaklıktadır.
A, B, C = ucgen_aci(70, 60, a=6.0)
K = cevrel(A, B, C); R = uz(K, A)
print("KA KB KC", uz(K, A), uz(K, B), uz(K, C))

fig, ax = sekil(5.0, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Circle(K, R, fill=False, ls=(0, (4, 3)), color=SOLUK, lw=1.3))
ax.plot(*zip(A, B, C, A), color=YAZI)
for (P, Q), renk, n in (((B, C), MAVI, 1), ((C, A), YESIL, 2), ((A, B), KIRMIZI, 3)):
    M = (P + Q) / 2; u = (K - M) / np.linalg.norm(K - M)
    ax.plot(*zip(M - 0.35 * u, K + 0.8 * u), color=renk, lw=1.9, ls="--")
    dik(ax, M, Q, K, s=0.25, renk=renk)
    centik(ax, P, M, n, renk=renk, L=0.14, ara=0.1); centik(ax, M, Q, n, renk=renk, L=0.14, ara=0.1)
for P in (A, B, C):
    ax.plot(*zip(K, P), color=SARI, lw=1.4)
nokta(ax, *A, "A", dx=-0.1, dy=0.2); nokta(ax, *B, "B", dx=-0.45, dy=-0.4); nokta(ax, *C, "C", dx=0.15, dy=-0.4)
nokta(ax, *K, "K", dx=0.3, dy=-0.62, renk=SARI)
ax.set_xlim(K[0] - R - 0.4, K[0] + R + 0.4); ax.set_ylim(K[1] - R - 0.3, K[1] + R + 0.3)
kaydet(fig, __file__)
