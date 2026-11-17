import sys; sys.path.insert(0, "tools")
from cizim import *

# Çarpan sadeleşir, terim sadeleşmez. x = 1 koyarak kontrol.
fig, ax = sekil(6, 3.4)
ax.axis("off")
ax.set_xlim(0, 10); ax.set_ylim(0, 5.6)
ax.add_patch(patches.FancyBboxPatch((0.2, 0.2), 4.5, 5.1, boxstyle="round,pad=0.05", facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.6))
ax.add_patch(patches.FancyBboxPatch((5.3, 0.2), 4.5, 5.1, boxstyle="round,pad=0.05", facecolor=KIRMIZI_ACIK, edgecolor=KIRMIZI, lw=1.6))
ax.text(2.45, 4.75, "Çarpan: sadeleşir", ha="center", fontsize=14, color=YESIL, weight="bold")
ax.text(7.55, 4.75, "Terim: sadeleşmez", ha="center", fontsize=14, color=KIRMIZI, weight="bold")
ax.text(2.45, 3.25, r"$\dfrac{5 \cdot x}{3 \cdot x} = \dfrac{5}{3}$", ha="center", va="center", fontsize=19)
ax.text(7.55, 3.25, r"$\dfrac{x + 5}{x + 3} \neq \dfrac{5}{3}$", ha="center", va="center", fontsize=19)
ax.text(2.45, 1.75, "x = 1:", ha="center", fontsize=13, color=SOLUK)
ax.text(2.45, 0.85, r"$\dfrac{5}{3} = \dfrac{5}{3}$", ha="center", va="center", fontsize=16, color=YESIL)
ax.text(7.55, 1.75, "x = 1:", ha="center", fontsize=13, color=SOLUK)
ax.text(7.55, 0.85, r"$\dfrac{6}{4} = \dfrac{3}{2} \neq \dfrac{5}{3}$", ha="center", va="center", fontsize=16, color=KIRMIZI)
kaydet(fig, __file__)
