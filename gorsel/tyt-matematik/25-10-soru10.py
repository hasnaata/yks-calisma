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

# Soru 10: kenarı 6 olan ABCD karesi; E ∈ [BC], F ∈ [DC], |CE| = |CF| = 2. AECF deltoid, alanı 12.
A, B, C, D = P(0, 0), P(6, 0), P(6, 6), P(0, 6); E, F = P(6, 4), P(4, 6)
S = 0.6
print("AE", uz(A, E), "AF", uz(A, F), "CE", uz(C, E), "CF", uz(C, F), "alan", alan_hesap(A, E, C, F))
basla(*cerceve([A, B, C, D], 1.2), en=3.6)
ax.add_patch(patches.Polygon([A, E, C, F], closed=True, facecolor=MAVI_ACIK, edgecolor="none"))
cokgen([A, B, C, D]); cizgi(A, E, MAVI, 2.0); cizgi(A, F, MAVI, 2.0)
nokta(ax, *E, ""); nokta(ax, *F, "")
harf(A, "A", -0.55, -0.5); harf(B, "B", 0.55, -0.5); harf(C, "C", 0.55, 0.5); harf(D, "D", -0.55, 0.5)
harf(E, "E", 0.6, 0); harf(F, "F", 0, 0.6)
olcu(A, B, "6", -0.6); olcu(E, C, "2", -0.55); olcu(C, F, "2", -0.6)
for Q, U, V in ((B, A, C), (D, C, A)): dik_isareti(Q, U, V, r=0.5)
kaydet(fig, __file__)
