import sys; sys.path.insert(0, "tools")
from cizim import *

# 4 x 3 ızgarada A'dan B'ye en kısa yollardan biri: S S Y S Y Y S (4 S, 3 Y).
fig, ax = sekil(5.4, 4.6)
ax.axis("off"); ax.set_aspect("equal")
M, N = 4, 3
for x in range(M + 1): ax.plot([x, x], [0, N], color=CIZGI, lw=1.6, zorder=1)
for y in range(N + 1): ax.plot([0, M], [y, y], color=CIZGI, lw=1.6, zorder=1)
yol = "SSYSYYS"
p = (0, 0)
for h in yol:
    q = (p[0] + 1, p[1]) if h == "S" else (p[0], p[1] + 1)
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=MAVI, lw=3, shrinkA=0, shrinkB=0), zorder=3)
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    if h == "S": ax.text(mx, my + 0.13, "S", ha="center", va="bottom", fontsize=12, color=MAVI, fontweight="bold")
    else: ax.text(mx - 0.13, my, "Y", ha="right", va="center", fontsize=12, color=MAVI, fontweight="bold")
    p = q
nokta(ax, 0, 0, "A", dx=-0.32, dy=-0.32, renk=YESIL)
nokta(ax, M, N, "B", dx=0.12, dy=0.08, renk=KIRMIZI)
ax.text(M / 2, -0.55, "S S Y S Y Y S  →  4 tane S, 3 tane Y", ha="center", va="top", fontsize=13, color=YAZI)
ax.set_xlim(-0.5, M + 0.5); ax.set_ylim(-1.1, N + 0.45)
kaydet(fig, __file__)
