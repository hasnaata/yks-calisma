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

# Ders, bölüm 5: α = 60°. OK ışını x = 1 doğrusunu N(1, √3)'te, y = 1 doğrusunu R(√3/3, 1)'de keser.
O, A, B = P(0, 0), P(1, 0), P(0, 1); K = kutup(60)
N = P(1, np.tan(np.radians(60))); R = P(1 / np.tan(np.radians(60)), 1); U = P(2.05 / np.tan(np.radians(60)), 2.05)
kontrol("K", K); print("N", N, "R", R, "|AN| =", N[1], "|BR| =", R[0])
fig, ax = sekil(5.4, 5.0); cember(ax, x=(-1.35, 2.35), y=(-1.35, 2.2))
ax.plot([1, 1], [-1.25, 2.15], color=MAVI, lw=1.4, zorder=1); ax.plot([-1.25, 2.3], [1, 1], color=YESIL, lw=1.4, zorder=1)
ax.plot(*zip(O, U), color=SARI, lw=1.8, zorder=3)
ax.plot(*zip(A, N), color=KIRMIZI, lw=3.6, zorder=3); ax.plot(*zip(B, R), color=KIRMIZI, lw=3.6, zorder=3)
dik(ax, A, O, N); dik(ax, B, O, R)
yay(ax, 0, 60, 0.22, "α", renk=YAZI, k=1.5)
nok(ax, K, SARI); yaz(ax, K + P(-0.12, -0.16), "K", SARI, ha="right", va="center")
nok(ax, N); yaz(ax, N + P(0.07, 0.0), "N(1, √3)", ha="left", va="center", fs=12)
nok(ax, R); yaz(ax, R + P(0.05, -0.05), "R", ha="left", va="top", fs=12)
nok(ax, A); yaz(ax, A + P(0.06, -0.06), "A", ha="left", va="top", fs=12)
nok(ax, B); yaz(ax, B + P(-0.06, 0.05), "B", ha="right", va="bottom", fs=12)
yaz(ax, P(-0.06, -0.06), "O", ha="right", va="top", fs=12)
yaz(ax, P(1.07, 0.5), "tan α", KIRMIZI, ha="left", va="center")
yaz(ax, P(R[0] / 2, 1.06), "cot α", KIRMIZI, ha="center", va="bottom", fs=12)
yaz(ax, P(1.08, -0.78), "tanjant ekseni", MAVI, ha="left", va="center", fs=11, rotation=90)
yaz(ax, P(2.3, 1.05), "kotanjant ekseni", YESIL, ha="right", va="bottom", fs=11)
kaydet(fig, __file__)
