import sys; sys.path.insert(0, "tools")
from cizim import *

# P(x) = −7x⁵ + 4x² − x + 3 polinomunun parçaları: derece, baş katsayı, sabit terim, terim sayısı.
fig, ax = sekil(6, 3.4)
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
Y, B = 3, 24
ax.text(1.2, Y, r"$P(x)=$", fontsize=20, va="center", ha="center")
ax.text(2.95, Y, r"$-7$", fontsize=B, va="center", ha="center", color=MAVI)
ax.text(4.0, Y, r"$x^{5}$", fontsize=B, va="center", ha="center")
ax.text(5.65, Y, r"$+\,4x^{2}$", fontsize=B, va="center", ha="center")
ax.text(7.55, Y, r"$-\,x$", fontsize=B, va="center", ha="center")
ax.text(9.1, Y, r"$+\,3$", fontsize=B, va="center", ha="center", color=SARI)
ax.add_patch(patches.FancyBboxPatch((2.33, 2.4), 1.15, 1.2, boxstyle="round,pad=0.05", fc="none", ec=MAVI, lw=2))
ax.annotate("baş katsayı: −7", xy=(2.95, 2.3), xytext=(0.4, 0.5), fontsize=13, color=MAVI,
            arrowprops=dict(arrowstyle="->", color=MAVI, lw=1.5))
ax.annotate("derece: 5", xy=(4.25, 3.75), xytext=(3.3, 5.4), fontsize=13, color=YESIL,
            arrowprops=dict(arrowstyle="->", color=YESIL, lw=1.5))
ax.annotate("sabit terim: 3", xy=(9.3, 2.3), xytext=(6.5, 0.5), fontsize=13, color=SARI,
            arrowprops=dict(arrowstyle="->", color=SARI, lw=1.5))
ax.text(7.9, 5.4, "4 terim", fontsize=13, color=SOLUK, ha="center")
kaydet(fig, __file__)
