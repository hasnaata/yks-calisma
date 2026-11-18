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
def alan(noktalar, metin, renk=YAZI, dx=0, dy=0, fs=13):
    """Çokgenin köşelerinin ortalamasına kalın yazı."""
    O = sum(noktalar) / len(noktalar)
    ax.text(O[0] + dx * S, O[1] + dy * S, metin, ha="center", va="center", color=renk, fontsize=fs, fontweight="bold")
def alan_hesap(*Q):
    return round(abs(sum(Q[i][0] * Q[(i + 1) % len(Q)][1] - Q[(i + 1) % len(Q)][0] * Q[i][1] for i in range(len(Q)))) / 2, 4)

# Örnek 6: 10 x 5 bahçe -> 12 x 4. Ortak 10 x 4 = 40, kaybedilen 10 x 1 = 10, kazanılan 2 x 4 = 8. Yeni alan 48.
A = P(0, 0)
S = 0.8
print("eski", 10 * 5, "yeni", 12 * 4, "kayip", 10 * 1, "kazanc", 2 * 4)
basla(-1.3, 13.3, -2.9, 5.8, en=5.6)
boya([P(0, 0), P(10, 0), P(10, 4), P(0, 4)], MAVI_ACIK)
boya([P(0, 4), P(10, 4), P(10, 5), P(0, 5)], KIRMIZI_ACIK)
boya([P(10, 0), P(12, 0), P(12, 4), P(10, 4)], YESIL_ACIK)
ax.plot(*zip(P(0, 0), P(10, 0), P(10, 5), P(0, 5), P(0, 0)), color=SOLUK, lw=1.8, ls="--")
ax.plot(*zip(P(0, 0), P(12, 0), P(12, 4), P(0, 4), P(0, 0)), color=YAZI, lw=2.2)
ax.text(5, 2, "40", ha="center", va="center", color=MAVI, fontsize=14, fontweight="bold")
ax.text(5, 4.5, "−10", ha="center", va="center", color=KIRMIZI, fontsize=13, fontweight="bold")
ax.text(11, 2, "+8", ha="center", va="center", color=YESIL, fontsize=13, fontweight="bold")
olcu(P(0, 0), P(10, 0), "10", -0.55); olcu(P(10, 0), P(12, 0), "2", -0.55, YESIL)
olcu(P(0, 0), P(0, 4), "4", 0.55); olcu(P(0, 4), P(0, 5), "1", 0.55, KIRMIZI)
ax.plot([0, 1.2], [-1.6, -1.6], color=SOLUK, lw=1.8, ls="--"); ax.text(1.5, -1.6, "eski: 10 · 5 = 50", va="center", color=SOLUK, fontsize=12)
ax.plot([0, 1.2], [-2.4, -2.4], color=YAZI, lw=2.2); ax.text(1.5, -2.4, "yeni: 12 · 4 = 48", va="center", color=YAZI, fontsize=12)
kaydet(fig, __file__)
