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

# Ders, bölüm 3: α = 30°, K(cos α, sin α) = (√3/2, 1/2); x ekseni kosinüs, y ekseni sinüs ekseni.
O = P(0, 0); K = kutup(30); T = P(K[0], 0); kontrol("K", K)
fig, ax = sekil(5.9, 4.4); cember(ax, x=(-1.45, 2.4), eksen_adi=False)
ax.add_patch(patches.Polygon([O, T, K], closed=True, facecolor=MAVI_ACIK, edgecolor="none", zorder=1))
ax.plot(*zip(O, K), color=MAVI, lw=2.4, zorder=3); ax.plot(*zip(O, T), color=YESIL, lw=3.4, zorder=3); ax.plot(*zip(T, K), color=KIRMIZI, lw=3.4, zorder=3)
dik(ax, T, O, K, s=0.07)
yay(ax, 0, 30, 0.3, "α", renk=YAZI, k=1.35)
nok(ax, K, MAVI); yaz(ax, K + P(0.08, 0.06), "K(cos α, sin α)", MAVI, ha="left", va="bottom", fs=12)
yaz(ax, (O + K) / 2 + P(-0.06, 0.06), "1", MAVI, ha="right", va="bottom")
yaz(ax, P(K[0] / 2, -0.07), "cos α", YESIL, ha="center", va="top")
yaz(ax, P(1.05, 0.33), "sin α", KIRMIZI, ha="left", va="center")
yaz(ax, P(-0.06, -0.06), "O", ha="right", va="top", fs=12)
for xy, ad, d, ha, va in ((P(1, 0), "A", P(0.05, 0.04), "left", "bottom"), (P(0, 1), "B", P(-0.06, 0.05), "right", "bottom"),
                          (P(-1, 0), "C", P(-0.05, 0.06), "right", "bottom"), (P(0, -1), "D", P(0.06, -0.06), "left", "top")):
    nok(ax, xy); yaz(ax, xy + d, ad, ha=ha, va=va, fs=12)
yaz(ax, P(1.1, -0.08), "x (kosinüs ekseni)", SOLUK, ha="left", va="top", fs=11)
yaz(ax, P(0.08, 1.45), "y (sinüs ekseni)", SOLUK, ha="left", va="center", fs=11)
kaydet(fig, __file__)
