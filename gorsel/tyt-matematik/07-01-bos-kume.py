import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders: kümeyi kutu gibi düşün. ∅ boş kutu; {∅} içinde boş kutu olan kutu; {0} içinde 0 olan kutu.
fig, ax = sekil(6, 2.9)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 12); ax.set_ylim(-1.6, 3.9)
def kutu(x, y, w, h, renk, dolgu, lw=2):
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.25",
                                        linewidth=lw, edgecolor=renk, facecolor=dolgu))
kutu(0.3, 0.3, 3.2, 2.6, KIRMIZI, KIRMIZI_ACIK)
ax.text(1.9, 3.35, "∅  =  { }", ha="center", fontsize=15, color=KIRMIZI, fontweight="bold")
ax.text(1.9, -0.5, "0 eleman", ha="center", fontsize=14, color=KIRMIZI)
kutu(4.4, 0.3, 3.2, 2.6, YESIL, YESIL_ACIK)
kutu(5.3, 0.9, 1.4, 1.2, KIRMIZI, "white", lw=1.6)
ax.text(6.0, 3.35, "{∅}", ha="center", fontsize=15, color=YESIL, fontweight="bold")
ax.text(6.0, -0.5, "1 eleman", ha="center", fontsize=14, color=YESIL)
kutu(8.5, 0.3, 3.2, 2.6, YESIL, YESIL_ACIK)
ax.text(10.1, 1.6, "0", ha="center", va="center", fontsize=20, color=YAZI)
ax.text(10.1, 3.35, "{0}", ha="center", fontsize=15, color=YESIL, fontweight="bold")
ax.text(10.1, -0.5, "1 eleman", ha="center", fontsize=14, color=YESIL)
ax.text(6.0, -1.35, "Yalnızca ilki boş kümedir.", ha="center", fontsize=13, color=SOLUK)
kaydet(fig, __file__)
