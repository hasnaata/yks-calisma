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

# Bölüm 3: aynı deltoid (|AC| = 14, |BD| = 24). Köşegenlerle kurulan 24'e 14 dikdörtgenin alanı 336, deltoid 168.
# KBC üçgeni ile dışındaki B-köşe-C üçgeni eştir (ikisi de 12'ye 9, alan 54).
A, B, C, D, K = deltoid(5, 9, 12)
S = 1.2
R = [P(-12, -5), P(12, -5), P(12, 9), P(-12, 9)]
print("dikdortgen", alan_hesap(*R), "deltoid", alan_hesap(A, B, C, D), "KBC", alan_hesap(K, B, C), "dis", alan_hesap(B, R[2], C))
basla(*cerceve(R, 1.3), en=5.2)
ax.add_patch(patches.Polygon(R, closed=True, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.4, ls="--"))
cokgen([A, B, C, D], MAVI_ACIK)
ax.add_patch(patches.Polygon([K, B, C], closed=True, facecolor="#c9daf5", edgecolor="none"))
ax.add_patch(patches.Polygon([B, R[2], C], closed=True, facecolor="#f6dfa6", edgecolor="none"))
cokgen([A, B, C, D])
cizgi(B, D, SOLUK, 1.4); cizgi(A, C, SOLUK, 1.4)
nokta(ax, *K, ""); harf(K, "K", -0.4, -0.4)
harf(A, "A", 0, -0.55, kutu=True); harf(C, "C", 0, 0.55, kutu=True); harf(B, "B", 0.6, 0); harf(D, "D", -0.6, 0)
olcu(R[0], R[1], "24", -0.6, SARI, f=0.25); olcu(R[1], R[2], "14", -0.85, SARI, f=0.22)
harf(P(4, 3), "54", 0, 0, MAVI, 13); harf(P(8, 6), "54", 0, 0, SARI, 13)
harf(P(-5, 1.6), "168", 0, 0, MAVI, 15)
kaydet(fig, __file__)
