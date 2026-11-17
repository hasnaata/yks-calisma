import sys; sys.path.insert(0, "tools")
from cizim import *

# √5'in sayı doğrusunda yeri: 2 × 1 dikdörtgenin köşegeni pergelle doğruya taşınır.
fig, ax = sekil(6, 3.4)
r = np.sqrt(5)
ax.set_aspect("equal"); ax.axis("off")
ax.annotate("", xy=(3.6, 0), xytext=(-1.6, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
for t in range(-1, 4):
    ax.plot([t, t], [-0.06, 0.06], color=SOLUK, lw=1.2)
    ax.text(t, -0.16, str(t).replace("-", "−"), ha="center", va="top", fontsize=13)
ax.add_patch(patches.Rectangle((0, 0), 2, 1, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.plot([1.85, 1.85, 2], [0, 0.15, 0.15], color=MAVI, lw=1.2)          # dik açı işareti
ax.plot([0, 2], [0, 1], color=KIRMIZI, lw=2.4)
t = np.linspace(np.arctan2(1, 2), 0, 60)
ax.plot(r * np.cos(t), r * np.sin(t), color=KIRMIZI, lw=1.6, ls="--")
nokta(ax, 0, 0, renk=YAZI)
ax.plot(r, 0, "o", color=KIRMIZI, markersize=9, zorder=6)
ax.text(1.0, -0.42, "2 birim", ha="center", va="top", color=MAVI, fontsize=13)
ax.text(1.9, 0.5, "1", ha="right", va="center", color=MAVI, fontsize=13)
ax.text(0.85, 0.62, "√5", ha="center", va="bottom", color=KIRMIZI, fontsize=14)
ax.text(r + 0.12, 0.12, "√5 ≈ 2,24", ha="left", va="bottom", color=KIRMIZI, fontsize=13)
ax.set_xlim(-1.7, 4.0); ax.set_ylim(-0.75, 1.4)
kaydet(fig, __file__)
