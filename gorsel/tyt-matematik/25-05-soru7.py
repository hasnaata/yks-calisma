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

# Alıştırma 7: m(DAB) = 100°, ABE eşkenar üçgen, E içeride. |AD| = |AE| → m(AED) = 70°.
A, B, C, D, _ = eskenar(6, 100)
E = P(3, 3 * np.sqrt(3))
s, t_ = np.linalg.solve(np.array([B - A, D - A]).T, E - A)
S = 6 / 10
print("ic mi", round(s, 3), round(t_, 3), "AE", uz(A, E), "BE", uz(B, E), "DAE", acisi(A, D, E), "AED", acisi(E, A, D), "ADE", acisi(D, A, E))
xs = [A[0], B[0], C[0], D[0]]; ys = [A[1], B[1], C[1], D[1]]
basla(min(xs) - 0.9, max(xs) + 0.9, min(ys) - 0.8, max(ys) + 0.8)
dortgen(A, B, C, D); koseler(A, B, C, D)
ucgen_dolgu(A, B, E, MAVI_ACIK)
cizgi(A, E, MAVI); cizgi(B, E, MAVI); cizgi(D, E, YAZI, 1.8)
nokta(ax, *E, ""); harf(E, "E", 0.5, 0.15)
aci(ax, A, B, D, r=0.75, ad="100°", renk=YESIL)
aci(ax, E, A, D, r=0.6, ad="x", renk=KIRMIZI)
for U, V in ((A, B), (B, C), (C, D), (D, A)): cetik(U, V, f=0.35)
cetik(A, E, 1, MAVI); cetik(B, E, 1, MAVI)
kaydet(fig, __file__)
