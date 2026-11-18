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

# Örnek 1: ikizkenar yamuk, taban açısı 70° (x = 30: 2x + 10 = 70, 3x + 20 = 110).
a, kol, t = 10, 5, np.radians(70)
A, B = P(0, 0), P(a, 0); D = P(kol * np.cos(t), kol * np.sin(t)); C = P(a - kol * np.cos(t), kol * np.sin(t))
S = a / 14
print("A", acisi(A, B, D), "B", acisi(B, A, C), "C", acisi(C, B, D), "D", acisi(D, A, C), "AD", uz(A, D), "BC", uz(B, C))
basla(-1.2, a + 1.2, -0.9, D[1] + 0.9)
yamuk(A, B, C, D, MAVI_ACIK); koseler(A, B, C, D)
cetik(A, D); cetik(B, C); paralel_isareti(A, B, 0.5); paralel_isareti(D, C, 0.5)
aci(ax, A, B, D, r=0.8, renk=MAVI); aci(ax, B, C, A, r=0.8, renk=MAVI)
aci(ax, C, D, B, r=0.6, renk=YESIL); aci(ax, D, A, C, r=0.6, renk=YESIL)
harf(A, "(2x + 10)°", 3.0, 0.75, MAVI); harf(B, "α", -1.35, 0.6, MAVI)
harf(C, "(3x + 20)°", -2.9, -0.75, YESIL); harf(D, "β", 1.15, -0.6, YESIL)
kaydet(fig, __file__)
