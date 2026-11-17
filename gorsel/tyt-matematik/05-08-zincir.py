import sys; sys.path.insert(0, "tools")
from cizim import *

# Maliyet 100x; etiket maliyetin %40 fazlası: 140x; etikete %25 indirim: 140x * 0,75 = 105x. Kâr 5x -> %5.
fig, ax = sekil(6.2, 2.9)
ax.axis("off")
kutular = [(0, "Maliyet", "100x", MAVI, MAVI_ACIK), (4.6, "Etiket", "140x", SARI, SARI_ACIK),
           (9.2, "Satış", "105x", YESIL, YESIL_ACIK)]
for x, ad, deger, renk, acik in kutular:
    ax.add_patch(patches.FancyBboxPatch((x, 0), 2.4, 1.5, boxstyle="round,pad=0.05,rounding_size=0.2",
                                        facecolor=acik, edgecolor=renk, lw=1.6))
    ax.text(x + 1.2, 1.08, ad, ha="center", va="center", fontsize=12, color=renk)
    ax.text(x + 1.2, 0.48, deger, ha="center", va="center", fontsize=15, color=YAZI, fontweight="bold")
for x0, ust, alt in [(2.4, "+%40", "maliyetin"), (7.0, "−%25", "etiketin")]:
    ax.annotate("", xy=(x0 + 2.1, 0.75), xytext=(x0 + 0.1, 0.75), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.6))
    ax.text(x0 + 1.1, 1.0, ust, ha="center", va="bottom", fontsize=12, color=YAZI, fontweight="bold")
    ax.text(x0 + 1.1, 0.5, alt, ha="center", va="top", fontsize=10, color=SOLUK)
ax.text(5.8, -0.45, "140x · 0,75 = 105x   →   kâr 5x, yani %5 kâr", ha="center", va="top", fontsize=12, color=YAZI)
ax.set_xlim(-0.2, 11.8); ax.set_ylim(-1.2, 1.8)
kaydet(fig, __file__)
