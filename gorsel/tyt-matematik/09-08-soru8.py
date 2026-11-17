import sys; sys.path.insert(0, "tools")
from cizim import *

# 5 sıra çivi (1, 2, 3, 4, 5 çivi), altta 6 bölme. Ortadaki iki bölme renkli.
fig, ax = sekil(4.6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
d = 1.0
for n in range(1, 6):
    for k in range(n):
        ax.plot((k - (n - 1) / 2) * d, -n * d, "o", color=YAZI, markersize=8, zorder=3)
# top
ax.add_patch(patches.Circle((0, -0.35), 0.22, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.8, zorder=4))
# bölmeler
yb = -6.0 * d
for i in range(6):
    xc = (i - 2.5) * d
    renk = MAVI if i in (2, 3) else None
    if renk:
        ax.add_patch(patches.Rectangle((xc - d / 2, yb - 1.0), d, 1.0, facecolor=MAVI_ACIK, edgecolor="none", zorder=1))
    ax.text(xc, yb - 1.35, f"{i + 1}", ha="center", va="top", fontsize=12, color=renk or SOLUK,
            fontweight="bold" if renk else "normal")
for i in range(7):
    xx = (i - 3) * d
    ax.plot([xx, xx], [yb - 1.0, yb], color=SOLUK, lw=1.6)
ax.plot([-3 * d, 3 * d], [yb - 1.0, yb - 1.0], color=SOLUK, lw=1.6)
ax.set_xlim(-3.3, 3.3); ax.set_ylim(yb - 2.0, 0.2)
kaydet(fig, __file__)
