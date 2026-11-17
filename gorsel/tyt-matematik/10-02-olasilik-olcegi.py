import sys; sys.path.insert(0, "tools")
from cizim import *

# Olasılık 0 ile 1 arasındadır. Bir zar ve bir madenî para örnekleri ölçek üzerinde.
fig, ax = sekil(6.4, 3.0)
ax.axis("off"); ax.set_xlim(-0.2, 1.2); ax.set_ylim(-1.45, 1.35)
ax.add_patch(patches.FancyBboxPatch((0, -0.06), 1, 0.12, boxstyle="round,pad=0,rounding_size=0.04",
                                    facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))
olaylar = [  # (değer, etiket, yazı, üstte mi, renk)
    (0, "0", "Zarda 7\n(imkânsız)", True, KIRMIZI),
    (1/6, "1/6", "Zarda 6", False, YAZI),
    (1/2, "1/2", "Parada\nyazı", True, YAZI),
    (5/6, "5/6", "Zarda 6\ngelmemesi", False, YAZI),
    (1, "1", "Zarda 7'den\nküçük (kesin)", True, YESIL),
]
for x, etiket, yazi, ust, renk in olaylar:
    ax.plot(x, 0, "o", color=renk if renk != YAZI else MAVI, markersize=10, zorder=5)
    ax.text(x, -0.2, etiket, ha="center", va="top", fontsize=14, color=YAZI)   # değer hep altta
    if ust:
        ax.text(x, 0.22, yazi, ha="center", va="bottom", fontsize=12, color=renk)
    else:
        ax.text(x, -0.62, yazi, ha="center", va="top", fontsize=12, color=renk)
kaydet(fig, __file__)
