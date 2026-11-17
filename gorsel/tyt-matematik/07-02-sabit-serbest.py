import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders: {a, b, c, d, e} kümesinin a'yı içeren, b'yi içermeyen alt kümeleri. a ve b sabit, c, d, e serbest: 2^3 = 8.
fig, ax = sekil(5.6, 2.6)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 11); ax.set_ylim(-2.1, 3.2)
kutular = [("a", YESIL, YESIL_ACIK, "kesin\nvar"), ("b", KIRMIZI, KIRMIZI_ACIK, "kesin\nyok"),
           ("c", MAVI, MAVI_ACIK, ""), ("d", MAVI, MAVI_ACIK, ""), ("e", MAVI, MAVI_ACIK, "")]
for i, (h, renk, acik, alt) in enumerate(kutular):
    x = 0.4 + i * 2.1
    ax.add_patch(patches.FancyBboxPatch((x, 0.4), 1.6, 1.6, boxstyle="round,pad=0,rounding_size=0.2",
                                        facecolor=acik, edgecolor=renk, lw=2))
    ax.text(x + 0.8, 1.2, h, ha="center", va="center", fontsize=22, fontweight="bold", color=renk)
    if alt: ax.text(x + 0.8, -0.1, alt, ha="center", va="top", fontsize=12, color=renk)
    ax.text(x + 0.8, 2.35, "1" if alt else "2", ha="center", va="bottom", fontsize=15, color=renk, fontweight="bold")
ax.text(7.5, -0.1, "serbest:\nvar ya da yok", ha="center", va="top", fontsize=12, color=MAVI)
ax.text(5.5, -1.45, "1 · 1 · 2 · 2 · 2 = 8", ha="center", va="top", fontsize=15, fontweight="bold")
kaydet(fig, __file__)
