import sys; sys.path.insert(0, "tools")
from cizim import *

fig, ax = sekil(6, 2.6)
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 4)
ax.text(5, 3.35, "3x − 5 = x²   →   x² − 3x + 5 = 0", ha="center", fontsize=15, color=SOLUK)
parcalar = [(2.3, "x²", "a = 1", MAVI, MAVI_ACIK), (4.6, "− 3x", "b = −3", YESIL, YESIL_ACIK),
            (6.9, "+ 5", "c = 5", SARI, SARI_ACIK)]
for xm, terim, ad, renk, acik in parcalar:
    ax.add_patch(patches.FancyBboxPatch((xm - 0.85, 1.75), 1.7, 0.9, boxstyle="round,pad=0.05",
                                        facecolor=acik, edgecolor=renk, lw=1.4))
    ax.text(xm, 2.2, terim, ha="center", va="center", fontsize=17, color=renk)
    ax.annotate("", xy=(xm, 1.05), xytext=(xm, 1.7), arrowprops=dict(arrowstyle="->", color=renk, lw=1.4))
    ax.text(xm, 0.7, ad, ha="center", va="center", fontsize=15, color=renk)
ax.text(8.6, 2.2, "= 0", ha="center", va="center", fontsize=17)
kaydet(fig, __file__)
