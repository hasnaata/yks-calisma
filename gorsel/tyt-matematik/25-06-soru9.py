import sys; sys.path.insert(0, "tools")
from cizim import *

P = lambda x, y: np.array([float(x), float(y)])
uz = lambda U, V: round(float(np.linalg.norm(U - V)), 4)
def acisi(K, U, V):
    u, v = U - K, V - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)
def birim(U, V):
    t = (V - U) / np.linalg.norm(V - U); return t, np.array([-t[1], t[0]])
def dondur(Q, derece):
    a = np.radians(derece); return P(Q[0] * np.cos(a) - Q[1] * np.sin(a), Q[0] * np.sin(a) + Q[1] * np.cos(a))
def ayak(Q, U, V):
    t, _ = birim(U, V); return U + np.dot(Q - U, t) * t
def paralel_isareti(U, V, n=1, f=0.5):
    t, _ = birim(U, V)
    for i in range(n):
        M = U + f * (V - U) + (i - (n - 1) / 2) * 0.32 * S * t
        ax.annotate("", xy=M + 0.22 * S * t, xytext=M - 0.22 * S * t, arrowprops=dict(arrowstyle="-|>", color=SOLUK, lw=1.3, mutation_scale=13))
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
        y = (Q - O) / np.linalg.norm(Q - O); harf(Q, ad, d * y[0] * 1.3, d * y[1])
def pk(AB, AD, derece):
    """A orijinde, [AB] yatay; ABCD paralelkenarının köşeleri."""
    a = np.radians(derece); A, B = P(0, 0), P(AB, 0); D = P(AD * np.cos(a), AD * np.sin(a)); return A, B, B + D, D
def cerceve(noktalar, kenar=1.2):
    xs = [q[0] for q in noktalar]; ys = [q[1] for q in noktalar]
    return min(xs) - kenar * S, max(xs) + kenar * S, min(ys) - kenar * S, max(ys) + kenar * S
def alan(noktalar, metin, renk=YAZI, dx=0, dy=0, fs=13):
    """Çokgenin ağırlık merkezine (köşelerin ortalaması) yazı."""
    O = sum(noktalar) / len(noktalar)
    ax.text(O[0] + dx * S, O[1] + dy * S, metin, ha="center", va="center", color=renk, fontsize=fs, fontweight="bold")
def kesisim(P1, P2, P3, P4):
    """[P1P2] ve [P3P4] doğrularının kesişimi."""
    d1, d2 = P2 - P1, P4 - P3
    x2 = lambda u, v: u[0] * v[1] - u[1] * v[0]
    t = x2(P3 - P1, d2) / x2(d1, d2); return P1 + t * d1
def alan_hesap(*Q):
    return round(abs(sum(Q[i][0] * Q[(i + 1) % len(Q)][1] - Q[(i + 1) % len(Q)][0] * Q[i][1] for i in range(len(Q)))) / 2, 4)


# Soru 9: halı ABCD; O ∈ [AC], |AO| : |OC| = 3 : 2; ANOK 18, OLCM 8, toplam 50; yeşil parçalar 12.
A, B, C, D = pk(5, 4, 65)
t = 3 / 5
O = A + t * (C - A); K = A + t * (B - A); N = A + t * (D - A); L = B + t * (C - B); M = D + t * (C - D)
S = 7 / 15
T = alan_hesap(A, B, C, D)
print("ANOK", 50 * alan_hesap(A, K, O, N) / T, "OLCM", 50 * alan_hesap(O, L, C, M) / T, "DNOM", 50 * alan_hesap(D, N, O, M) / T)
basla(*cerceve([A, B, C, D], 1.0))
boya([A, K, O, N], KIRMIZI_ACIK); boya([O, L, C, M], MAVI_ACIK); boya([D, N, O, M], YESIL_ACIK); boya([K, B, L, O], YESIL_ACIK)
dortgen(A, B, C, D); koseler(A, B, C, D, 0.5)
cizgi(N, L, SOLUK, 1.6); cizgi(M, K, SOLUK, 1.6); cizgi(A, C, YAZI, 1.6, "--")
for Q, ad, dx, dy in ((N, "N", -0.55, 0.1), (L, "L", 0.55, -0.1), (M, "M", 0, 0.5), (K, "K", 0, -0.5)): nokta(ax, *Q, ""); harf(Q, ad, dx, dy)
nokta(ax, *O, ""); harf(O, "O", -0.5, 0.45)
alan([A, K, O, N], "18", KIRMIZI, 0.35, -0.35); alan([O, L, C, M], "8", MAVI, -0.15, 0.2); alan([D, N, O, M], "?", YESIL)
kaydet(fig, __file__)
