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

# Alıştırma 9: saat 13.40; yelkovan 8'i gösterir. 3 → 0°, her rakam 30°: 8 → 90° − 8·30° = −150° (210°).
# Akrep: 1 + 40/60 saat → 12'den 50° saat yönünde → 40°.
fig, ax = sekil(4.6, 4.6); cember(ax, x=(-1.5, 1.5), y=(-1.5, 1.5))
for n in range(1, 13):
    a = 90 - 30 * n; Z = kutup(a, 1.17)
    ax.text(*Z, str(n), ha="center", va="center", fontsize=12, color=YAZI, bbox=dict(facecolor="white", edgecolor="none", pad=0.6), zorder=4)
    ax.plot(*zip(kutup(a, 0.93), kutup(a, 1.0)), color=YAZI, lw=1.4)
U = kutup(90 - 30 * 8); H = kutup(90 - 50, 0.55); kontrol("U", U)
ax.plot(*zip(P(0, 0), U), color=KIRMIZI, lw=3, zorder=3); ax.plot(*zip(P(0, 0), H), color=SOLUK, lw=4.5, zorder=3, solid_capstyle="round")
nok(ax, P(0, 0)); nok(ax, U, KIRMIZI); yaz(ax, P(-0.62, -0.47), "U", KIRMIZI, ha="center", va="top")
yaz(ax, P(0.06, -0.06), "O", ha="left", va="top", fs=12)
kaydet(fig, __file__)
