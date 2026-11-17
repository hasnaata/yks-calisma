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

# K'nin yeri: dar açılı (70-60-50) içinde, dik (B=90°, 6-8-10) hipotenüsün orta noktasında,
# geniş açılı (A=120°) üçgenin dışında, en uzun kenarın ötesinde.
fig, eks = plt.subplots(1, 3, figsize=(6.5, 3.0))
ucgenler = [ucgen_aci(70, 60, a=6.0),
            (np.array([0.0, 4.5]), np.array([0.0, 0.0]), np.array([6.0, 0.0])),
            ucgen_aci(120, 35, a=6.0)]
basliklar = ["Dar açılı\nK içeride", "Dik\nK hipotenüste", "Geniş açılı\nK dışarıda"]
for ax, (A, B, C), bas in zip(eks, ucgenler, basliklar):
    ax.set_aspect("equal"); ax.axis("off")
    K = cevrel(A, B, C); R = uz(K, A)
    print(bas.replace("\n", " "), "K", K.round(3), "R", R, uz(K, B), uz(K, C))
    ax.add_patch(plt.Polygon([A, B, C], color=MAVI_ACIK, lw=0))
    ax.plot(*zip(A, B, C, A), color=YAZI, lw=1.8)
    for P, Q in ((B, C), (C, A), (A, B)):
        M = (P + Q) / 2
        if np.linalg.norm(K - M) > 1e-6:
            u = (K - M) / np.linalg.norm(K - M)
            ax.plot(*zip(M - 0.3 * u, K + 0.4 * u), color=KIRMIZI, lw=1.3, ls="--")
    if bas.startswith("Dik"):
        dik(ax, B, A, C, s=0.45, renk=YAZI)
    ax.plot(*K, "o", color=KIRMIZI, markersize=7, zorder=5)
    ax.set_title(bas, fontsize=13, color=YAZI, pad=10)
    xs = [p[0] for p in (A, B, C, K)]; ys = [p[1] for p in (A, B, C, K)]
    ax.set_xlim(min(xs) - 0.9, max(xs) + 0.9); ax.set_ylim(min(ys) - 0.9, max(ys) + 1.0)
    kd = {"Dar": (0.25, -0.8), "Dik": (0.3, 0.2), "Gen": (0.3, -0.1)}[bas[:3]]
    ax.text(K[0] + kd[0], K[1] + kd[1], "K", color=KIRMIZI, fontsize=13)
    ax.text(A[0] - 0.2, A[1] + 0.3, "A", fontsize=13)
    ax.text(B[0] - 0.6, B[1] - 0.6, "B", fontsize=13); ax.text(C[0] + 0.15, C[1] - 0.6, "C", fontsize=13)
fig.subplots_adjust(wspace=0.15)
kaydet(fig, __file__)
