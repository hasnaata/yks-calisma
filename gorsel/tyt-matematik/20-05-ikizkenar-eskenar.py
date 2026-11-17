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

# Sol: ikizkenar |AB|=|AC|=5, |BC|=6. [BC]'nin kenar orta dikmesi A'dan geçer (yükseklik = kenarortay = açıortay), K bu doğrudadır.
# Sağ: eşkenar, kenar 6. K = G; |KA| = 2√3 ≈ 3,464, |KD| = √3 ≈ 1,732.
fig, eks = plt.subplots(1, 2, figsize=(6.4, 3.6))
ax = eks[0]; ax.set_aspect("equal"); ax.axis("off")
A, B, C = ucgen(6, 5, 5); D = (B + C) / 2; K = cevrel(A, B, C)
print("ikizkenar K", K.round(3), "KA", uz(K, A), "KD", uz(K, D))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(D - np.array([0, 0.4]), A + np.array([0, 0.4])), color=KIRMIZI, lw=2, ls="--")
for P, Q in ((A, B), (A, C)):
    M = (P + Q) / 2; u = (K - M) / np.linalg.norm(K - M)
    ax.plot(*zip(M - 0.3 * u, K + 0.3 * u), color=SOLUK, lw=1.1, ls="--")
dik(ax, D, C, A, s=0.32, renk=KIRMIZI)
centik(ax, B, D, 1); centik(ax, D, C, 1); centik(ax, A, B, 2, renk=MAVI); centik(ax, A, C, 2, renk=MAVI)
nokta(ax, *A, "A", dx=0.15, dy=0.2); nokta(ax, *B, "B", dx=-0.5, dy=-0.5); nokta(ax, *C, "C", dx=0.15, dy=-0.5)
nokta(ax, *D, "D", dx=0.15, dy=-0.55); nokta(ax, *K, "K", dx=0.22, dy=-0.38, renk=KIRMIZI)
ax.set_title("İkizkenar", fontsize=13, color=YAZI)
ax.set_xlim(-0.8, 6.8); ax.set_ylim(-1.0, A[1] + 1.0)

ax = eks[1]; ax.set_aspect("equal"); ax.axis("off")
A, B, C = ucgen(6, 6, 6); K = cevrel(A, B, C)
D, E, F = (B + C) / 2, (C + A) / 2, (A + B) / 2
print("eşkenar K", K.round(3), "KA", uz(K, A), "KD", uz(K, D), "AD", uz(A, D))
ax.plot(*zip(A, B, C, A), color=YAZI)
for P, Q in ((A, D), (B, E), (C, F)):
    ax.plot(*zip(P, Q), color=KIRMIZI, lw=1.6, ls="--")
dik(ax, D, C, A, s=0.32, renk=KIRMIZI)
nokta(ax, *A, "A", dx=0.15, dy=0.2); nokta(ax, *B, "B", dx=-0.5, dy=-0.5); nokta(ax, *C, "C", dx=0.15, dy=-0.5)
nokta(ax, *D, "D", dx=0.15, dy=-0.55); nokta(ax, *K, "K", dx=-0.62, dy=0.32, renk=KIRMIZI)
ax.text(3.08, 2.75, r"$2\sqrt{3}$", ha="left", va="center", fontsize=12, color=KIRMIZI)
ax.text(3.45, 0.75, r"$\sqrt{3}$", ha="left", va="center", fontsize=13, color=KIRMIZI)
ax.text(3, -0.95, "6", ha="center", va="center", fontsize=13)
ax.set_title("Eşkenar", fontsize=13, color=YAZI)
ax.set_xlim(-0.8, 6.8); ax.set_ylim(-1.3, A[1] + 1.0)
fig.subplots_adjust(wspace=0.1)
kaydet(fig, __file__)
