import sys; sys.path.insert(0, "tools")
from cizim import *

def P(x, y): return np.array([x, y], float)
def kutup(derece, r=1.0): return P(r * np.cos(np.radians(derece)), r * np.sin(np.radians(derece)))
def cember(ax, x=(-1.45, 1.45), y=(-1.45, 1.45), eksen_adi=True):
    """Orijin merkezli birim çember ve oklu eksenler."""
    ax.set_aspect("equal"); ax.axis("off")
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(t), np.sin(t), color=YAZI, lw=2, zorder=2)
    ok = dict(arrowstyle="-|>", color=SOLUK, lw=1.3, mutation_scale=12)
    ax.annotate("", xy=(x[1], 0), xytext=(x[0], 0), arrowprops=ok)
    ax.annotate("", xy=(0, y[1]), xytext=(0, y[0]), arrowprops=ok)
    if eksen_adi:
        ax.text(x[1], -0.08, "x", ha="center", va="top", color=SOLUK, fontsize=12)
        ax.text(0.08, y[1], "y", ha="left", va="center", color=SOLUK, fontsize=12)
    ax.set_xlim(x[0] - 0.05, x[1] + 0.12); ax.set_ylim(y[0] - 0.05, y[1] + 0.1)
def dik(ax, K, A, B, s=0.08, renk=SOLUK):
    """K köşesinde KA ile KB arasındaki dik açı işareti."""
    K, A, B = P(*K), P(*A), P(*B)
    u = (A - K) / np.linalg.norm(A - K) * s; v = (B - K) / np.linalg.norm(B - K) * s
    ax.plot(*zip(K + u, K + u + v, K + v), color=renk, lw=1.2)
def yay(ax, a1, a2, r, ad="", renk=MAVI, k=1.55, fs=12):
    """Orijinde a1 dereceden a2 dereceye (saat yönünün tersine) açı yayı."""
    ax.add_patch(patches.Arc((0, 0), 2 * r, 2 * r, theta1=a1, theta2=a2, color=renk, lw=1.6))
    if ad:
        m = np.radians((a1 + a2) / 2)
        ax.text(k * r * np.cos(m), k * r * np.sin(m), ad, ha="center", va="center", color=renk, fontsize=fs)
def nok(ax, xy, renk=YAZI, ms=6): ax.plot(*xy, "o", color=renk, markersize=ms, zorder=5)
def yaz(ax, xy, metin, renk=YAZI, fs=13, **k): ax.text(xy[0], xy[1], metin, color=renk, fontsize=fs, **k)
def kontrol(ad, K): print(ad, np.round(K, 4), "x²+y² =", round(float(K @ K), 6))

# Ders, bölüm 4: 30°, 150°, 210°, 330° noktaları birbirinin eksenlere ve orijine göre simetriğidir.
K, L, M, N = kutup(30), kutup(150), kutup(210), kutup(330)
for ad, Q in zip("KLMN", (K, L, M, N)): kontrol(ad, Q)
fig, ax = sekil(5.8, 4.2); cember(ax, x=(-2.1, 2.1), y=(-1.3, 1.3))
ax.plot(*zip(K, L, M, N, K), color=SOLUK, lw=1.3, ls="--", zorder=1)
for Q, renk in ((K, MAVI), (L, YESIL), (M, KIRMIZI), (N, SARI)):
    ax.plot(*zip(P(0, 0), Q), color=renk, lw=1.8, zorder=3); nok(ax, Q, renk)
yaz(ax, K + P(0.06, 0.07), "K(√3/2, 1/2)", MAVI, ha="left", va="bottom", fs=12)
yaz(ax, L + P(-0.06, 0.07), "L(−√3/2, 1/2)", YESIL, ha="right", va="bottom", fs=12)
yaz(ax, M + P(-0.06, -0.07), "M(−√3/2, −1/2)", KIRMIZI, ha="right", va="top", fs=12)
yaz(ax, N + P(0.06, -0.07), "N(√3/2, −1/2)", SARI, ha="left", va="top", fs=12)
yay(ax, 0, 30, 0.4, "30°", renk=MAVI, k=1.45, fs=11)
yay(ax, 0, 150, 0.2, renk=YESIL)
yaz(ax, P(-0.24, 0.31), "150°", YESIL, ha="center", va="center", fs=11)
yaz(ax, P(-0.27, -0.075), "O", ha="center", va="center", fs=11)
kaydet(fig, __file__)
