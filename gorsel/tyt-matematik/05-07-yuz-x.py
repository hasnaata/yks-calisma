import sys; sys.path.insert(0, "tools")
from cizim import *

# Para 100x. %30'u kitap -> kalan 70x. Kalanın %20'si (14x) yemek -> kalan 56x = 112 TL -> x = 2 -> para 200 TL.
fig, ax = sekil(6.2, 3.4)
ax.axis("off")
satirlar = [
    (2.2, [(100, MAVI_ACIK, MAVI, "100x")], "Başta"),
    (1.1, [(30, KIRMIZI_ACIK, KIRMIZI, "30x"), (70, MAVI_ACIK, MAVI, "70x")], "Kitap"),
    (0.0, [(30, "white", CIZGI, ""), (14, KIRMIZI_ACIK, KIRMIZI, "14x"), (56, YESIL_ACIK, YESIL, "56x")], "Yemek"),
]
for y, parcalar, ad in satirlar:
    x = 0
    for g, ic, kenar, yazi in parcalar:
        ax.add_patch(patches.Rectangle((x, y), g, 0.75, facecolor=ic, edgecolor=kenar, lw=1.4))
        if yazi: ax.text(x + g / 2, y + 0.375, yazi, ha="center", va="center", fontsize=12, color=kenar)
        x += g
    ax.text(-3, y + 0.375, ad, ha="right", va="center", fontsize=11, color=SOLUK)
ax.text(72, -0.25, "56x = 112  →  x = 2  →  para 100x = 200 TL", ha="center", va="top", fontsize=11, color=YESIL)
ax.set_xlim(-22, 101); ax.set_ylim(-0.9, 3.05)
kaydet(fig, __file__)
