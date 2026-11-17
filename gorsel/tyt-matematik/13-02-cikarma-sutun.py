import sys; sys.path.insert(0, "tools")
from cizim import *

# P(x) − Q(x) işlemini aynı dereceli terimleri alt alta yazarak yapmak.
# P(x) = 3x³ − 2x² + 5x − 1, Q(x) = x³ + 4x² − 7  →  P − Q = 2x³ − 6x² + 5x + 6
fig, ax = sekil(6, 3.6)
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 6)
sutunlar = ["$x^3$", "$x^2$", "$x$", "sabit"]
xs = [3.6, 5.2, 6.8, 8.4]
satirlar = [
    ("P(x)", ["$3x^3$", "$-2x^2$", "$5x$", "$-1$"], YAZI, None),
    ("−Q(x)", ["$-x^3$", "$-4x^2$", "$0$", "$+7$"], KIRMIZI, KIRMIZI_ACIK),
    ("P(x) − Q(x)", ["$2x^3$", "$-6x^2$", "$5x$", "$+6$"], YESIL, YESIL_ACIK),
]
for x, s in zip(xs, sutunlar):
    ax.add_patch(patches.Rectangle((x - 0.75, 0.4), 1.5, 4.6, facecolor=MAVI_ACIK, edgecolor="none", alpha=0.6))
    ax.text(x, 5.35, s, ha="center", va="center", fontsize=13, color=MAVI)
ys = [4.3, 3.0, 1.1]
for (ad, terimler, renk, dolgu), y in zip(satirlar, ys):
    if dolgu:
        ax.add_patch(patches.FancyBboxPatch((0.15, y - 0.45), 9.6, 0.9, boxstyle="round,pad=0.02",
                                            facecolor=dolgu, edgecolor=renk, lw=1.2, alpha=0.9))
    ax.text(0.35, y, ad, ha="left", va="center", fontsize=13, color=renk)
    for x, t in zip(xs, terimler):
        ax.text(x, y, t.replace("-", "−"), ha="center", va="center", fontsize=15, color=renk)
ax.plot([0.2, 9.7], [2.1, 2.1], color=YAZI, lw=1.5)
ax.text(2.55, 3.0, "+", ha="center", va="center", fontsize=16, color=KIRMIZI)
kaydet(fig, __file__)
