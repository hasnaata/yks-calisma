import sys; sys.path.insert(0, "tools")
from cizim import *

# 8 elemanlı kümenin 3 elemanlı alt kümeleri: x'i içerenler C(7, 2) = 21, içermeyenler C(7, 3) = 35.
fig, ax = sekil(6, 3.8)
ax.axis("off"); ax.set_aspect("equal")
def kutu(xm, y, w, h, satirlar, dolgu, kenar):
    ax.add_patch(patches.FancyBboxPatch((xm - w / 2, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                        facecolor=dolgu, edgecolor=kenar, lw=1.6))
    n = len(satirlar)
    for i, (s, fs) in enumerate(satirlar):
        ax.text(xm, y + h * (n - i - 0.5) / n, s, ha="center", va="center", fontsize=fs, color=kenar, fontweight="bold")
kutu(3.0, 2.2, 4.4, 1.2, [("3 elemanlı alt kümeler", 13), ("C(8, 3) = 56", 15)], MAVI_ACIK, MAVI)
kutu(1.25, 0, 2.5, 1.2, [("x var", 13), ("C(7, 2) = 21", 15)], YESIL_ACIK, YESIL)
kutu(4.75, 0, 2.5, 1.2, [("x yok", 13), ("C(7, 3) = 35", 15)], KIRMIZI_ACIK, KIRMIZI)
for xh in (1.25, 4.75):
    ax.annotate("", xy=(xh, 1.25), xytext=(3.0 + (xh - 3.0) * 0.45, 2.15), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.5))
ax.text(3.0, 0.6, "+", ha="center", va="center", fontsize=22, color=YAZI)
ax.text(3.0, -0.35, "21 + 35 = 56", ha="center", va="top", fontsize=16, color=YAZI, fontweight="bold")
ax.set_xlim(-0.2, 6.2); ax.set_ylim(-1.1, 3.6)
kaydet(fig, __file__)
