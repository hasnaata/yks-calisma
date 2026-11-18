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


# Örnek 1: |AB| = 12, |AD| = 10, [DH] ⊥ [AB], |DH| = 8 (|AH| = 6); [BK] ⊥ [AD], |BK| = 9,6.
A, B, C, D = pk(12, 10, np.degrees(np.arctan2(8, 6)))
H = ayak(D, A, B); K = ayak(B, A, D)
S = 18 / 15
print("AD", uz(A, D), "DH", uz(D, H), "AH", uz(A, H), "BK", uz(B, K), "AK", uz(A, K), "alan", alan_hesap(A, B, C, D))
x0, x1, y0, y1 = cerceve([A, B, C, D], 1.0); basla(x0, x1, y0 - 0.6 * S, y1)
dortgen(A, B, C, D); koseler(A, B, C, D, 0.45)
cizgi(D, H, KIRMIZI, 2); cizgi(B, K, YESIL, 2)
dik_isareti(H, D, B, 0.35); dik_isareti(K, B, D, 0.35)
nokta(ax, *H, ""); harf(H, "H", 0, -0.5)
nokta(ax, *K, ""); harf(K, "K", -0.45, 0.2)
yo = -1.2 * S  # [AB] uzunluğu: H'yi bölmeyen ölçü çizgisi
ax.annotate("", xy=(B[0], yo), xytext=(A[0], yo), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2, shrinkA=0, shrinkB=0))
for Q in (A, B): ax.plot([Q[0], Q[0]], [yo - 0.15 * S, yo + 0.15 * S], color=SOLUK, lw=1.2)
ax.text((A[0] + B[0]) / 2, yo, "12", ha="center", va="center", color=YAZI, fontsize=13, bbox=dict(facecolor="white", edgecolor="none", pad=2))
olcu(A, D, "10", 0.5, f=0.3); olcu(D, H, "8", -0.4, KIRMIZI, f=0.7); olcu(B, K, "?", -0.45, YESIL, f=0.4)
kaydet(fig, __file__)
