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

# Alıştırma 11: 1 m'lik kol O'da; önce 40°, sonra 140°. Uçlar aynı yükseklikte; yatay fark 2·cos 40°.
O = P(0, 0); U1, U2 = kutup(40), kutup(140); print("U1", np.round(U1, 4), "U2", np.round(U2, 4), "fark", round(U1[0] - U2[0], 4))
fig, ax = sekil(5.2, 3.2); ax.set_aspect("equal"); ax.axis("off")
ax.plot([-1.35, 1.35], [0, 0], color=SOLUK, lw=1.3, ls="--")
ax.add_patch(patches.Rectangle((-0.16, -0.18), 0.32, 0.18, facecolor=CIZGI, edgecolor=SOLUK, lw=1.2))
ax.add_patch(patches.Arc(O, 2, 2, theta1=40, theta2=140, color=CIZGI, lw=1.4, ls=":"))
ax.plot(*zip(O, U1), color=MAVI, lw=4, solid_capstyle="round"); ax.plot(*zip(O, U2), color=KIRMIZI, lw=4, solid_capstyle="round")
nok(ax, O); nok(ax, U1, MAVI); nok(ax, U2, KIRMIZI)
ax.plot([U2[0], U1[0]], [U1[1], U1[1]], color=YAZI, lw=1.2, ls="--")
yaz(ax, P(0, U1[1] + 0.05), "?", ha="center", va="bottom", fs=14)
yay(ax, 0, 40, 0.3, "40°", renk=MAVI, k=1.65, fs=11)
yay(ax, 0, 140, 0.18, renk=KIRMIZI); yaz(ax, P(-0.07, 0.3), "140°", KIRMIZI, ha="center", va="center", fs=11)
yaz(ax, P(0.33, 0.42), "1 m", MAVI, ha="right", va="bottom", fs=12)
yaz(ax, U1 + P(0.05, 0.03), "1. konum", MAVI, ha="left", va="bottom", fs=11)
yaz(ax, U2 + P(-0.05, 0.03), "2. konum", KIRMIZI, ha="right", va="bottom", fs=11)
yaz(ax, P(0.06, -0.06), "O", ha="left", va="top", fs=12)
ax.set_xlim(-1.4, 1.4); ax.set_ylim(-0.3, 1.06)
kaydet(fig, __file__)
