import sys; sys.path.insert(0, "tools")
from cizim import *

P = lambda x, y: np.array([float(x), float(y)])
uz = lambda U, V: round(float(np.linalg.norm(U - V)), 4)
def acisi(K, U, V):
    u, v = U - K, V - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)
def birim(U, V):
    t = (V - U) / np.linalg.norm(V - U); return t, np.array([-t[1], t[0]])
def ayak(Q, U, V):
    t, _ = birim(U, V); return U + np.dot(Q - U, t) * t
def yansit(Q, U, V):
    return 2 * ayak(Q, U, V) - Q
def kesisim(U1, V1, U2, V2):
    M = np.array([V1 - U1, U2 - V2]).T; s = np.linalg.solve(M, U2 - U1); return U1 + s[0] * (V1 - U1)
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
def boya(noktalar, renk):
    ax.add_patch(patches.Polygon(noktalar, closed=True, facecolor=renk, edgecolor="none"))
def yay(K, U, V, r=0.8, renk=MAVI, n=1):
    for i in range(n): aci(ax, K, U, V, r=(r + 0.18 * i) * S, renk=renk)
def yay_yazi(K, U, V, metin, d=1.4, renk=MAVI, fs=12):
    """K köşesindeki U-K-V açısının ortasından d*S uzağa yazı."""
    u = (U - K) / np.linalg.norm(U - K); v = (V - K) / np.linalg.norm(V - K); o = (u + v) / np.linalg.norm(u + v)
    ax.text(*(K + d * S * o), metin, ha="center", va="center", color=renk, fontsize=fs)
def basla(xmin, xmax, ymin, ymax, en=5.5):
    global fig, ax
    fig, ax = sekil(en, en * (ymax - ymin) / (xmax - xmin))
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(xmin, xmax); ax.set_ylim(ymin, ymax)
def dortgen(A, B, C, D, dolgu=None):
    if dolgu: boya([A, B, C, D], dolgu)
    ax.plot(*zip(A, B, C, D, A), color=YAZI)
    for Q in (A, B, C, D): nokta(ax, *Q, "")
def koseler(A, B, C, D, d=0.55):
    O = (A + B + C + D) / 4
    for Q, ad in ((A, "A"), (B, "B"), (C, "C"), (D, "D")):
        y = (Q - O) / np.linalg.norm(Q - O); harf(Q, ad, d * np.sign(y[0]) * 1.1, d * np.sign(y[1]))
def dikdortgen(a, b):
    """A orijinde, [AB] yatay: A, B, C, D."""
    return P(0, 0), P(a, 0), P(a, b), P(0, b)
def dik_koseler(A, B, C, D, r=0.4):
    dik_isareti(A, B, D, r); dik_isareti(B, C, A, r); dik_isareti(C, D, B, r); dik_isareti(D, A, C, r)
def cerceve(noktalar, kenar=1.2):
    xs = [q[0] for q in noktalar]; ys = [q[1] for q in noktalar]
    return min(xs) - kenar * S, max(xs) + kenar * S, min(ys) - kenar * S, max(ys) + kenar * S

# Kural 4 (dış): d, D'den geçer; [AF] ⊥ d, [CE] ⊥ d; |AF| = 3, |CE| = 4 -> |FD| = 4, |DE| = 3, |FE| = 7, kenar 5.
D = P(0, 0); A = P(-4, -3); C = P(3, -4); B = A + C - D
F, E = P(-4, 0), P(3, 0)
S = 7 / 12
print("AB", uz(A, B), "BC", uz(B, C), "CD", uz(C, D), "DA", uz(D, A), "ADC", acisi(D, A, C), "AF", uz(A, F), "FD", uz(F, D), "DE", uz(D, E), "EC", uz(E, C))
basla(-5.6, 4.6, -7.9, 1.2, en=5.0)
boya([A, F, D], MAVI_ACIK); boya([D, E, C], MAVI_ACIK)
cizgi(P(-5.4, 0), P(4.4, 0), SOLUK, 1.6); harf(P(4.4, 0), "d", 0.0, 0.45, SOLUK)
dortgen(A, B, C, D)
dik_koseler(A, B, C, D, 0.4)
cizgi(A, F, KIRMIZI, 2.0); cizgi(C, E, KIRMIZI, 2.0)
dik_isareti(F, A, D, 0.4); dik_isareti(E, C, D, 0.4)
for Q, ad, dx, dy in ((A, "A", -0.55, -0.2), (B, "B", 0, -0.6), (C, "C", 0.55, -0.2), (D, "D", 0, 0.5), (F, "F", -0.3, 0.5), (E, "E", 0.3, 0.5)):
    nokta(ax, *Q, ""); harf(Q, ad, dx, dy)
olcu(A, F, "3", -0.5, KIRMIZI); olcu(E, C, "4", -0.5, KIRMIZI)
olcu(F, D, "4", 0.5, YESIL); olcu(D, E, "3", 0.5, YESIL)
yay(A, F, D, 1.0, MAVI); yay_yazi(A, F, D, "α", 1.8, MAVI)
yay(D, C, E, 1.0, MAVI); yay_yazi(D, C, E, "α", 1.8, MAVI)
kaydet(fig, __file__)
