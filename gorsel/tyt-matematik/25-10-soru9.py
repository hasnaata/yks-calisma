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
def olcu(U, V, metin, d=0.5, renk=YAZI, fs=13, f=0.5, kutu=False):
    """[UV] üzerinde f oranındaki noktaya, U->V yönünün soluna d*S uzağa yazı (d < 0: sağına)."""
    M = U + f * (V - U); _, m = birim(U, V)
    ax.text(*(M + d * S * m), metin, ha="center", va="center", color=renk, fontsize=fs, zorder=7,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5) if kutu else None)
def dik_isareti(K, U, V, r=0.4):
    a_ = (U - K) / np.linalg.norm(U - K) * r * S; b_ = (V - K) / np.linalg.norm(V - K) * r * S
    ax.plot(*zip(K + a_, K + a_ + b_, K + b_), color=SOLUK, lw=1.3)
def harf(Q, metin, dx, dy, renk=YAZI, fs=13, kutu=False):
    ax.text(Q[0] + dx * S, Q[1] + dy * S, metin, ha="center", va="center", color=renk, fontsize=fs, zorder=7,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5) if kutu else None)
def cizgi(U, V, renk=YAZI, lw=2.2, ls="-"):
    ax.plot(*zip(U, V), color=renk, lw=lw, ls=ls)
def basla(xmin, xmax, ymin, ymax, en=5.0):
    global fig, ax
    fig, ax = sekil(en, en * (ymax - ymin) / (xmax - xmin))
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(xmin, xmax); ax.set_ylim(ymin, ymax)
def cokgen(noktalar, dolgu=None, kenar=YAZI, lw=2.2):
    if dolgu: ax.add_patch(patches.Polygon(noktalar, closed=True, facecolor=dolgu, edgecolor="none"))
    ax.plot(*zip(*(list(noktalar) + [noktalar[0]])), color=kenar, lw=lw)
    for Q in noktalar: nokta(ax, *Q, "")
def cerceve(noktalar, kenar=1.0):
    xs = [q[0] for q in noktalar]; ys = [q[1] for q in noktalar]
    return min(xs) - kenar * S, max(xs) + kenar * S, min(ys) - kenar * S, max(ys) + kenar * S
def deltoid(ak, ck, kb):
    """K orijinde; A altta, C üstte, D solda, B sağda. |AB| = |AD|, |CB| = |CD|."""
    return P(0, -ak), P(kb, 0), P(0, ck), P(-kb, 0), P(0, 0)
def koseler(A, B, C, D, r=0.5):
    harf(A, "A", 0, -r); harf(B, "B", r, 0); harf(C, "C", 0, r); harf(D, "D", -r, 0)
def alan_hesap(*Q):
    return round(abs(sum(Q[i][0] * Q[(i + 1) % len(Q)][1] - Q[(i + 1) % len(Q)][0] * Q[i][1] for i in range(len(Q)))) / 2, 4)

# Soru 9: ABCD yamuk, [AB] ∥ [DC]; E ∈ [AD]; DEBC deltoid: |DE| = |DC| = 4, |BE| = |BC|. |AE| = 5 → |AB| = |AD| = 9.
t = np.radians(62)
A, B = P(0, 0), P(9, 0); D = 9 * P(np.cos(t), np.sin(t)); C = D + P(4, 0); E = D + (A - D) * 4 / 9
S = 0.7
print("BE", uz(B, E), "BC", uz(B, C), "DE", uz(D, E), "DC", uz(D, C), "AE", uz(A, E), "EDB", acisi(D, E, B), "BDC", acisi(D, B, C), "ABD", acisi(B, A, D))
basla(*cerceve([A, B, C, D], 1.2), en=4.2)
ax.add_patch(patches.Polygon([D, E, B, C], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
cokgen([A, B, C, D]); cizgi(E, B, YAZI, 1.8); nokta(ax, *E, "")
harf(A, "A", -0.5, -0.4); harf(B, "B", 0.5, -0.4); harf(C, "C", 0.5, 0.4); harf(D, "D", -0.5, 0.4); harf(E, "E", -0.6, 0)
olcu(D, C, "4", 0.5); olcu(E, D, "4", -0.55); olcu(A, E, "5", -0.55); olcu(A, B, "?", -0.6, fs=15)
cetik(D, E, 1, f=0.3); cetik(D, C, 1, f=0.7); cetik(B, E, 2); cetik(B, C, 2)
kaydet(fig, __file__)
