import sys; sys.path.insert(0, "tools")
from cizim import *

P = lambda x, y: np.array([float(x), float(y)])
uz = lambda U, V: round(float(np.linalg.norm(U - V)), 4)
def acisi(K, U, V):
    u, v = U - K, V - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)
def kesis(p, u, q, v):
    t = np.linalg.solve(np.array([u, -v]).T, q - p); return p + t[0] * u
def birim(U, V):
    t = (V - U) / np.linalg.norm(V - U); return t, np.array([-t[1], t[0]])
def paralel_isareti(U, V, f=0.5):
    M = U + f * (V - U); t, _ = birim(U, V)
    ax.annotate("", xy=M + 0.3 * S * t, xytext=M - 0.3 * S * t, arrowprops=dict(arrowstyle="-|>", color=SOLUK, lw=1.4, mutation_scale=14))
def cetik(U, V, n=1, renk=SOLUK, f=0.5):
    M = U + f * (V - U); t, m = birim(U, V)
    for i in range(n):
        c = M + (i - (n - 1) / 2) * 0.2 * S * t
        ax.plot(*zip(c - 0.22 * S * m, c + 0.22 * S * m), color=renk, lw=1.5)
def olcu(U, V, metin, d=0.5, renk=YAZI, fs=13):
    """[UV] ortasına, U->V yönünün soluna d*S uzağa yazı (d < 0: sağına)."""
    M = (U + V) / 2; _, m = birim(U, V)
    ax.text(*(M + d * S * m), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik_isareti(K, U, V, r=0.4):
    a_ = (U - K) / np.linalg.norm(U - K) * r * S; b_ = (V - K) / np.linalg.norm(V - K) * r * S
    ax.plot(*zip(K + a_, K + a_ + b_, K + b_), color=SOLUK, lw=1.3)
def harf(Q, metin, dx, dy, renk=YAZI, fs=13):
    ax.text(Q[0] + dx * S, Q[1] + dy * S, metin, ha="center", va="center", color=renk, fontsize=fs)
def cizgi(U, V, renk=YAZI, lw=2.2, ls="-"):
    ax.plot(*zip(U, V), color=renk, lw=lw, ls=ls)
def basla(xmin, xmax, ymin, ymax, en=5.5):
    global fig, ax
    fig, ax = sekil(en, en * (ymax - ymin) / (xmax - xmin))
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(xmin, xmax); ax.set_ylim(ymin, ymax)
def yamuk(A, B, C, D, dolgu=None):
    if dolgu: ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=dolgu, edgecolor="none"))
    ax.plot(*zip(A, B, C, D, A), color=YAZI)
    for Q in (A, B, C, D): nokta(ax, *Q, "")
def koseler(A, B, C, D):
    harf(A, "A", -0.5, -0.4); harf(B, "B", 0.5, -0.4); harf(C, "C", 0.5, 0.4); harf(D, "D", -0.5, 0.4)

# Soru 8: çanta, ön yüz ikizkenar yamuk: üst 40, alt 24, yükseklik 15 -> yan kenar 17.
A, B, C, D = P(8, 0), P(32, 0), P(40, 15), P(0, 15); H = P(8, 15)
S = 40 / 14
print("yan", uz(A, D), uz(B, C), "h", uz(A, H))
basla(-3.5, 43.5, -3.0, 26.5)
# sap
tt = np.linspace(0, np.pi, 60)
ax.plot(20 + 10 * np.cos(tt), 15 + 9 * np.sin(tt), color=SARI, lw=4, solid_capstyle="round")
ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.plot(*zip(A, B, C, D, A), color=YAZI)
cizgi(A, H, KIRMIZI, 1.6, "--"); dik_isareti(H, A, C, 0.35)
olcu(D, C, "40", -0.5); olcu(A, B, "24", -0.5); olcu(A, H, "15", -0.5, KIRMIZI)
kaydet(fig, __file__)
