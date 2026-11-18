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

# Soru 3: |AB| = |AD| = 17, |BD| = 16 → |KB| = 8, |AK| = 15. (Üst kenarlar 10, |CK| = 6; soruda verilmez.)
A, B, C, D, K = deltoid(15, 6, 8)
S = 1.0
print("AB", uz(A, B), "AD", uz(A, D), "BD", uz(B, D), "AK", uz(A, K), "CB", uz(C, B), "CD", uz(C, D))
basla(*cerceve([A, B, C, D], 1.1), en=3.8)
cokgen([A, B, C, D]); koseler(A, B, C, D, r=0.7)
cizgi(B, D, SOLUK, 1.6); cizgi(A, C, MAVI, 1.8)
nokta(ax, *K, ""); harf(K, "K", 0.45, 0.45)
harf(K, "BD = 16", -3.9, 0.5, SOLUK, 12)
olcu(A, B, "17", -1.0); olcu(D, A, "17", -1.0)
olcu(A, K, "?", 0.55, MAVI, 15)
kaydet(fig, __file__)
