import sys; sys.path.insert(0, "tools")
from cizim import *

P = lambda x, y: np.array([float(x), float(y)])
uz = lambda U, V: round(float(np.linalg.norm(U - V)), 4)
def acisi(K, U, V):
    u, v = U - K, V - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)
def birim(U, V):
    t = (V - U) / np.linalg.norm(V - U); return t, np.array([-t[1], t[0]])
def cetik(U, V, n=1, renk=SOLUK, f=0.5):
    M = U + f * (V - U); t, m = birim(U, V)
    for i in range(n):
        c = M + (i - (n - 1) / 2) * 0.2 * S * t
        ax.plot(*zip(c - 0.22 * S * m, c + 0.22 * S * m), color=renk, lw=1.5)
def olcu(U, V, metin, d=0.5, renk=YAZI, fs=13, f=0.5):
    """[UV] üzerinde f oranındaki noktaya, U->V yönünün soluna d*S uzağa yazı (d < 0: sağına)."""
    M = U + f * (V - U); _, m = birim(U, V)
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
def dortgen(A, B, C, D, dolgu=None):
    if dolgu: ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=dolgu, edgecolor="none"))
    ax.plot(*zip(A, B, C, D, A), color=YAZI)
    for Q in (A, B, C, D): nokta(ax, *Q, "")
def ucgen_dolgu(U, V, W, renk):
    ax.add_patch(patches.Polygon([U, V, W], closed=True, facecolor=renk, edgecolor="none"))
def eskenar(a, derece):
    """A(0,0), B(a,0), A'daki açı derece olan eşkenar dörtgen; E köşegenlerin kesişimi."""
    t = np.radians(derece)
    A, B, D = P(0, 0), P(a, 0), P(a * np.cos(t), a * np.sin(t)); C = B + D
    return A, B, C, D, (A + C) / 2
def koseler(A, B, C, D):
    harf(A, "A", -0.45, -0.4); harf(B, "B", 0.45, -0.4); harf(C, "C", 0.45, 0.4); harf(D, "D", -0.45, 0.4)

# Bölüm 4: kenar 8, m(A) = 60°. ABD eşkenar üçgen: |BD| = 8; |AC| = 8√3.
A, B, C, D, E = eskenar(8, 60)
S = 8 / 11
print("BD", uz(B, D), "AC", uz(A, C), "8kok3", round(8 * np.sqrt(3), 4), "ABD", acisi(B, A, D), "ADB", acisi(D, A, B))
basla(-1.0, C[0] + 1.0, -0.9, C[1] + 0.9)
ucgen_dolgu(A, B, D, MAVI_ACIK)
dortgen(A, B, C, D); koseler(A, B, C, D)
cizgi(B, D, MAVI); cizgi(A, C, SOLUK, 1.6, "--")
nokta(ax, *E, ""); harf(E, "E", 0.15, 0.62)
olcu(A, B, "8", -0.5); olcu(D, A, "8", -0.5); olcu(B, C, "8", -0.5); olcu(C, D, "8", -0.5)
olcu(B, D, "8", 0.5, MAVI, f=0.32)
olcu(A, C, r"$8\sqrt{3}$", 0.55, SOLUK, f=0.78)
aci(ax, A, B, D, r=0.9, renk=MAVI); harf(A, "60°", 2.0, 0.42, MAVI, 12)
aci(ax, B, D, A, r=0.75, ad="60°", renk=MAVI); aci(ax, D, A, B, r=0.75, ad="60°", renk=MAVI)
kaydet(fig, __file__)
