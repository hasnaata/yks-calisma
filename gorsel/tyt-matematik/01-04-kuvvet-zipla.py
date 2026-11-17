import sys; sys.path.insert(0, "tools")
from cizim import *

# (−2)^n: üs bir artınca sonuç sıfırın bir sağına bir soluna geçer.
DEGER = [(1, -2), (2, 4), (3, -8), (4, 16)]
fig, ax = sekil(6, 2.6)
ax.set_xlim(-10, 18); ax.set_ylim(-1.1, 2.2); ax.axis("off")
ax.annotate("", xy=(17.8, 0), xytext=(-9.8, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
ax.hlines(-0.06, -9.6, -0.15, color=KIRMIZI, lw=4, alpha=0.4)
ax.hlines(-0.06, 0.15, 17.6, color=YESIL, lw=4, alpha=0.4)
for t in (-8, -2, 0, 4, 16):
    ax.plot([t, t], [-0.12, 0.12], color=SOLUK, lw=1.2)
    ax.text(t, -0.35, str(t).replace("-", "−"), ha="center", va="top", fontsize=13)
onceki = 0
for n, v in DEGER:
    renk = YESIL if v > 0 else KIRMIZI
    ax.plot(v, 0, "o", color=renk, markersize=9, zorder=5)
    y = 0.42 + 0.42 * (n - 1)
    ax.annotate("", xy=(v, 0.14), xytext=(v, y - 0.08), arrowprops=dict(arrowstyle="-|>", color=renk, lw=1.4))
    ax.text(v, y + 0.1, f"$(-2)^{n}$", ha="center", va="bottom", color=renk, fontsize=13)
kaydet(fig, __file__)
