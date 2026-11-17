import sys; sys.path.insert(0, "tools")
from cizim import *

def centik(ax, P, Q, n=1, renk=SOLUK, L=0.13, ara=0.09):
    """[PQ] kenarının ortasına n çentik (eş kenar işareti)."""
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]]); M = (P + Q) / 2
    for k in range(n):
        c = M + (k - (n - 1) / 2) * ara * u
        ax.plot(*zip(c - L * v, c + L * v), color=renk, lw=1.6)

def olc(K, P, Q):
    a, b = np.asarray(P) - K, np.asarray(Q) - K
    return round(float(np.degrees(np.arccos(np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b)))), 3)

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P) - np.asarray(Q))), 3)

def dik(ax, K, P, Q, k=0.25, renk=YAZI):
    K = np.asarray(K, float)
    a = (np.asarray(P) - K) / np.linalg.norm(np.asarray(P) - K); b = (np.asarray(Q) - K) / np.linalg.norm(np.asarray(Q) - K)
    ax.plot(*zip(K + k * a, K + k * (a + b), K + k * b), color=renk, lw=1.3)

def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])

# Alıştırma soru 11: iki merdiven 17 m, ayakları aynı P noktasında, birbirine dik. Sol merdiven duvarda 15 m yükseğe ulaşıyor.
# Sol: yatay 8, yükseklik 15. Sağ (eş üçgen): yatay 15, yükseklik 8. Duvarlar arası 23.
K = np.array([0.0, 0.0]); P = np.array([8.0, 0.0]); L = np.array([0.0, 15.0]); M = np.array([23.0, 0.0]); R = np.array([23.0, 8.0])
print("PL", uz(P, L), "PR", uz(P, R), "LPR", olc(P, L, R))
fig, ax = sekil(6, 4.0)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Rectangle((-1.2, 0), 1.2, 17, facecolor=CIZGI, edgecolor="none"))
ax.add_patch(patches.Rectangle((23, 0), 1.2, 17, facecolor=CIZGI, edgecolor="none"))
ax.plot([-1.2, 24.2], [0, 0], color=SOLUK, lw=1.6)
ax.plot(*zip(P, L), color=MAVI, lw=2.6); ax.plot(*zip(P, R), color=YESIL, lw=2.6)
dik(ax, P, L, R, k=0.9); dik(ax, K, P, L, k=0.9, renk=SOLUK); dik(ax, M, P, R, k=0.9, renk=SOLUK)
nokta(ax, *P, "P", dx=-0.4, dy=-1.6)
ax.text(*((P + L) / 2 + np.array([0.6, 0.4])), "17 m", color=MAVI, ha="left", va="center", fontsize=12)
ax.text(*((P + R) / 2 + np.array([0.0, 0.9])), "17 m", color=YESIL, ha="center", va="bottom", fontsize=12)
ax.annotate("", xy=(-2.0, 0), xytext=(-2.0, 15), arrowprops=dict(arrowstyle="<->", color=YAZI, lw=1.2))
ax.plot([-2.4, 0], [15, 15], color=SOLUK, lw=0.8, ls=":")
ax.text(-2.4, 7.5, "15 m", ha="right", va="center", fontsize=12)
ax.annotate("", xy=(0, -2.4), xytext=(23, -2.4), arrowprops=dict(arrowstyle="<->", color=YAZI, lw=1.2))
ax.text(11.5, -2.8, "?", ha="center", va="top", fontsize=14)
ax.set_xlim(-6.5, 24.5); ax.set_ylim(-4.6, 17.5)
kaydet(fig, __file__)
