import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = 2x + 1, tanım kümesi (−1, 3]. f(−1) = −1 (dahil değil), f(3) = 7 (dahil). Görüntü kümesi (−1, 7].
fig, ax = sekil(6, 3.3)
ax.axis("off"); ax.set_xlim(-2.8, 9.0); ax.set_ylim(-1.3, 3.4)

def dogru(y, a, b, renk, ad):
    ax.annotate("", xy=(b + 0.6, y), xytext=(a - 0.6, y), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
    for t in range(a, b + 1):
        ax.plot([t, t], [y - 0.08, y + 0.08], color=SOLUK, lw=1.1)
        ax.text(t, y - 0.22, str(t).replace("-", "−"), ha="center", va="top", fontsize=11, color=YAZI)
    ax.text(a - 0.9, y, ad, ha="right", va="center", fontsize=14, color=renk, fontweight="bold")

dogru(2.4, -2, 8, MAVI, "x")
dogru(0.0, -2, 8, YESIL, "f(x)")
ax.plot([-1, 3], [2.4, 2.4], color=MAVI, lw=5, solid_capstyle="butt")
nokta(ax, -1, 2.4, renk=MAVI, dolu=False); nokta(ax, 3, 2.4, renk=MAVI)
ax.plot([-1, 7], [0, 0], color=YESIL, lw=5, solid_capstyle="butt")
nokta(ax, -1, 0, renk=YESIL, dolu=False); nokta(ax, 7, 0, renk=YESIL)
for s, h in ((-1, -1), (3, 7)):
    ax.annotate("", xy=(h, 0.25), xytext=(s, 2.15), arrowprops=dict(arrowstyle="->", color=SARI, lw=1.6))
ax.text(-1.25, 1.2, "f(−1) = −1", fontsize=11, color=SARI, ha="right", va="center")
ax.text(5.4, 1.45, "f(3) = 7", fontsize=11, color=SARI, ha="left", va="center")
ax.text(1, 2.95, "tanım kümesi (−1, 3]", fontsize=12, color=MAVI, ha="center")
ax.text(3, -0.95, "görüntü kümesi (−1, 7]", fontsize=12, color=YESIL, ha="center")
kaydet(fig, __file__)
