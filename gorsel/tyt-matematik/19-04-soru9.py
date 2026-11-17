import sys; sys.path.insert(0, "tools")
from cizim import *

# Lamba L yerde (0,0). Kişi x=2'de, boyu 1,8 m. Duvar x=6'da. Gölgenin duvardaki yüksekliği 1,8*6/2 = 5,4 m.
L = np.array([0.0, 0.0]); B = np.array([2.0, 0.0]); K = np.array([2.0, 1.8]); W = np.array([6.0, 0.0]); G = np.array([6.0, 5.4])
print("G", 1.8 * 6 / 2)
fig, ax = sekil(4.6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-0.5, 6.0], [0, 0], color=SOLUK, lw=1.2)
ax.add_patch(patches.Rectangle((6.0, 0), 0.3, 6.2, facecolor=CIZGI, edgecolor=SOLUK, lw=1))
ax.plot(*zip(W, G), color=YAZI, lw=6, alpha=0.75)
ax.plot(*zip(L, G), color=SARI, lw=1.8, ls="--")
ax.plot(*zip(B, K), color=MAVI, lw=4)
ax.plot(L[0], L[1] + 0.12, "o", color=SARI, markersize=14, zorder=6)
s = 0.22
ax.plot([B[0], B[0] + s, B[0] + s], [s, s, 0], color=YAZI, lw=1.1)
ax.text(-0.15, 0.45, "lamba", ha="center", va="bottom", color=SARI, fontsize=11)
ax.text(1.85, 0.9, "1,8 m", ha="right", va="center", color=MAVI, fontsize=12)
ax.text(6.45, 2.7, "?", ha="left", va="center", fontsize=14)
ax.text(6.45, 5.9, "duvar", ha="left", va="center", color=SOLUK, fontsize=11)
for xb, y, t in [(2, -0.45, "2 m"), (6, -1.15, "6 m")]:
    ax.annotate("", xy=(xb, y), xytext=(0, y), arrowprops=dict(arrowstyle="<->", color=YAZI, lw=1.2))
    ax.text(xb / 2, y - 0.32, t, ha="center", va="center", fontsize=12)
ax.set_xlim(-0.8, 7.6); ax.set_ylim(-1.7, 6.4)
kaydet(fig, __file__)
