import sys; sys.path.insert(0, "tools")
from cizim import *

# 2^3 · 2^2: üç tane 2 ile iki tane 2 yan yana gelir, beş tane 2 olur.
fig, ax = sekil(6, 2.3)
ax.axis("off"); ax.set_xlim(-0.6, 5.6); ax.set_ylim(-1.25, 1.0)
for i in range(5):
    mavi = i < 3
    ax.add_patch(patches.FancyBboxPatch((i * 1.05 - 0.36, -0.36), 0.72, 0.72, boxstyle="round,pad=0.02",
                 facecolor=MAVI_ACIK if mavi else YESIL_ACIK, edgecolor=MAVI if mavi else YESIL, lw=1.6))
    ax.text(i * 1.05, 0, "2", ha="center", va="center", fontsize=17, color=YAZI)
    if i < 4: ax.text(i * 1.05 + 0.525, 0, "·", ha="center", va="center", fontsize=18, color=SOLUK)
ax.annotate("", xy=(-0.36, 0.55), xytext=(2.46, 0.55), arrowprops=dict(arrowstyle="-", color=MAVI, lw=1.5))
ax.text(1.05, 0.78, "$2^{3}$", ha="center", va="center", fontsize=15, color=MAVI)
ax.annotate("", xy=(2.79, 0.55), xytext=(4.56, 0.55), arrowprops=dict(arrowstyle="-", color=YESIL, lw=1.5))
ax.text(3.675, 0.78, "$2^{2}$", ha="center", va="center", fontsize=15, color=YESIL)
ax.text(2.1, -0.85, "5 tane 2 çarpılıyor:  $2^{3} \\cdot 2^{2} = 2^{3+2} = 2^{5}$", ha="center", va="center", fontsize=14, color=YAZI)
kaydet(fig, __file__)
