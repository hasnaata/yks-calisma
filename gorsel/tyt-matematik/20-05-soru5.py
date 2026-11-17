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

# Alıştırma soru 5: m(B)=32°, m(C)=70°, m(A)=78°. d, [AB]'nin kenar orta dikmesi; [BC]'yi D'de keser.
# |DA|=|DB| → m(DAB)=32°, x = m(DAC) = 78° − 32° = 46°.
A, B, C = ucgen_aci(78, 32, a=9.0)
M = (A + B) / 2; n = np.array([-(A - B)[1], (A - B)[0]])
D = kesis(M, M + n, B, C)
print("A", aci_olc(A, B, C), "C", aci_olc(C, A, B), "DAB", aci_olc(A, B, D), "DAC", aci_olc(A, D, C), "DA DB", uz(D, A), uz(D, B))

fig, ax = sekil(5.4, 3.0)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, D), color=MAVI, lw=2)
u = (M - D) / np.linalg.norm(M - D)
ax.plot(*zip(D - 0.5 * u, M + 0.8 * u), color=KIRMIZI, lw=2, ls="--")
ax.text(*(M + 1.0 * u), "d", color=KIRMIZI, fontsize=14, ha="center", va="center")
dik(ax, M, A, M + u, s=0.3, renk=KIRMIZI)
centik(ax, A, M, 1); centik(ax, M, B, 1)
aci(ax, B, C, A, r=1.6, ad="32°", renk=YESIL)
aci(ax, C, A, B, r=0.8, ad="70°", renk=SARI)
aci(ax, A, D, C, r=0.9, ad="x", renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.1, dy=0.25); nokta(ax, *B, "B", dx=-0.55, dy=-0.5); nokta(ax, *C, "C", dx=0.15, dy=-0.5)
nokta(ax, *D, "D", dx=-0.15, dy=-0.65, renk=MAVI)
ax.set_xlim(-0.9, 9.8); ax.set_ylim(-0.8, A[1] + 0.8)
kaydet(fig, __file__)
