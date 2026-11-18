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

# Alıştırma 8: dönme dolap; merkez M yerden 25 m, yarıçap 20 m. Kabin S'den (merkezle aynı yükseklik, sağda)
# saat yönünün tersine 150° dönüp Q'ya geliyor: Q'nun yüksekliği 25 + 20·sin 150° = 35 m.
M = P(0, 25); r = 20; S = M + P(r, 0); Q = M + kutup(150, r); print("S", S, "Q", np.round(Q, 3), "|MQ|", round(float(np.linalg.norm(Q - M)), 3))
fig, ax = sekil(5.2, 4.6); ax.set_aspect("equal"); ax.axis("off")
t = np.linspace(0, 2 * np.pi, 400); ax.plot(M[0] + r * np.cos(t), M[1] + r * np.sin(t), color=YAZI, lw=2.2)
ax.plot([-30, 30], [0, 0], color=SOLUK, lw=2)
ax.plot(*zip(M, P(-9, 0)), color=SOLUK, lw=2); ax.plot(*zip(M, P(9, 0)), color=SOLUK, lw=2)
ax.plot([M[0] - r - 3, M[0] + r + 3], [M[1], M[1]], color=SOLUK, lw=1.1, ls=":")
ax.plot(*zip(M, S), color=MAVI, lw=2); ax.plot(*zip(M, Q), color=KIRMIZI, lw=2)
ax.add_patch(patches.Arc(M, 14, 14, theta1=0, theta2=150, color=SARI, lw=1.6))
ax.annotate("", xy=M + kutup(150, 7) + P(0.25, 0.43), xytext=M + kutup(148, 7), arrowprops=dict(arrowstyle="-|>", color=SARI, lw=1.4, mutation_scale=12))
yaz(ax, M + kutup(75, 9.5), "150°", SARI, ha="center", va="center", fs=12)
for Z, renk in ((S, MAVI), (Q, KIRMIZI)): ax.add_patch(patches.Rectangle(Z - P(1.4, 1.4), 2.8, 2.8, facecolor=renk, edgecolor=renk, zorder=5))
yaz(ax, S + P(1.6, 2.0), "S", MAVI, ha="left", va="bottom"); yaz(ax, Q + P(-1.6, 1.6), "Q", KIRMIZI, ha="right", va="bottom")
nok(ax, M); yaz(ax, M + P(1.0, 0.8), "M", ha="left", va="bottom", fs=12)
yaz(ax, (M + S) / 2 + P(0, -1.2), "20 m", MAVI, ha="center", va="top", fs=12)
ax.plot([Q[0], Q[0]], [0, Q[1] - 1.5], color=KIRMIZI, lw=1.3, ls="--"); yaz(ax, P(Q[0] - 0.8, 12), "?", KIRMIZI, ha="right", va="center", fs=14)
ok = dict(arrowstyle="<|-|>", color=YAZI, lw=1.2, mutation_scale=10)
ax.annotate("", xy=(27, 0), xytext=(27, 25), arrowprops=ok); yaz(ax, P(27.8, 12.5), "25 m", ha="left", va="center", fs=12)
ax.plot([20, 28], [25, 25], color=SOLUK, lw=0.8, ls=":")
yaz(ax, P(-29, -1.2), "yer", SOLUK, ha="left", va="top", fs=11)
ax.set_xlim(-31, 35); ax.set_ylim(-4, 47)
kaydet(fig, __file__)
