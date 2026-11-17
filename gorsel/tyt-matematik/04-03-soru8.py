import sys; sys.path.insert(0, "tools")
from cizim import *

# Alanı 48 cm² (kenar 4√3 ≈ 6,93) ve 27 cm² (kenar 3√3 ≈ 5,20) iki kare, alt kenarları aynı doğruda yan yana.
a, b = 48 ** 0.5, 27 ** 0.5
fig, ax = sekil(5, 3.2)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Rectangle((0, 0), a, a, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.add_patch(patches.Rectangle((a, 0), b, b, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2))
ax.text(a / 2, a / 2, "48 cm²", ha="center", va="center", color=MAVI, fontsize=15)
ax.text(a + b / 2, b / 2, "27 cm²", ha="center", va="center", color=YESIL, fontsize=15)
ax.set_xlim(-0.3, a + b + 0.3); ax.set_ylim(-0.3, a + 0.3)
kaydet(fig, __file__)
