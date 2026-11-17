import sys; sys.path.insert(0, "tools")
from cizim import *

# Kenarı √5 + √3 olan kare: alanı 5 + 3 + 2√15 = 8 + 2√15.
a, b = 5 ** 0.5, 3 ** 0.5
fig, ax = sekil(4.6, 4.4)
ax.axis("off"); ax.set_aspect("equal")
parcalar = ((0, b, a, a, MAVI_ACIK, MAVI, "5"),            # sol üst: √5 × √5
            (a, 0, b, b, YESIL_ACIK, YESIL, "3"),          # sağ alt: √3 × √3
            (a, b, b, a, SARI_ACIK, SARI, "√15"),          # sağ üst
            (0, 0, a, b, SARI_ACIK, SARI, "√15"))          # sol alt
for x0, y0, w, h, dolgu, renk, yazi in parcalar:
    ax.add_patch(patches.Rectangle((x0, y0), w, h, facecolor=dolgu, edgecolor=renk, lw=1.8))
    ax.text(x0 + w / 2, y0 + h / 2, yazi, ha="center", va="center", color=renk, fontsize=15)
# kenar etiketleri
ax.text(a / 2, a + b + 0.15, "√5", ha="center", va="bottom", fontsize=13)
ax.text(a + b / 2, a + b + 0.15, "√3", ha="center", va="bottom", fontsize=13)
ax.text(-0.15, b + a / 2, "√5", ha="right", va="center", fontsize=13)
ax.text(-0.15, b / 2, "√3", ha="right", va="center", fontsize=13)
ax.set_xlim(-0.8, a + b + 0.2); ax.set_ylim(-0.2, a + b + 0.6)
kaydet(fig, __file__)
