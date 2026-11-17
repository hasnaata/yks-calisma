import sys; sys.path.insert(0, "tools")
from cizim import *

# 72 = 2^3·3^2 ve 120 = 2^3·3·5 asal çarpanları Venn şemasında. Kesişim EBOB, hepsi EKOK.
fig, ax = sekil(6, 3.9)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Circle((-1.1, 0), 2.0, fc=MAVI_ACIK, ec=MAVI, lw=2, alpha=0.7))
ax.add_patch(patches.Circle((1.1, 0), 2.0, fc=SARI_ACIK, ec=SARI, lw=2, alpha=0.7))
ax.text(-1.9, 2.25, "72", ha="center", fontsize=16, color=MAVI, fontweight="bold")
ax.text(1.9, 2.25, "120", ha="center", fontsize=16, color=SARI, fontweight="bold")
ax.text(-2.1, 0, "3", ha="center", va="center", fontsize=18)
ax.text(2.1, 0, "5", ha="center", va="center", fontsize=18)
for y, t in ((0.75, "2"), (0.25, "2"), (-0.25, "2"), (-0.75, "3")):
    ax.text(0, y, t, ha="center", va="center", fontsize=18, color=YESIL, fontweight="bold")
ax.text(0, -2.55, "Kesişim: EBOB = 2·2·2·3 = 24", ha="center", fontsize=13, color=YESIL)
ax.text(0, -3.15, "Hepsi: EKOK = 3·2·2·2·3·5 = 360", ha="center", fontsize=13, color=KIRMIZI)
ax.set_xlim(-3.4, 3.4); ax.set_ylim(-3.5, 2.7)
kaydet(fig, __file__)
