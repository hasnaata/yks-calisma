import sys; sys.path.insert(0, "tools")
from cizim import *

# Değil işaretlerini say: çift sayıda değil sonucu değiştirmez, tek sayıda değil sonucu değiller.
fig, ax = sekil(6, 3.6)
ax.axis("off")
def kutu(x, y, yazi, renk, acik):
    ax.add_patch(patches.FancyBboxPatch((x - 0.92, y - 0.38), 1.84, 0.76, boxstyle="round,pad=0.02,rounding_size=0.15",
                 facecolor=acik, edgecolor=renk, lw=1.6))
    ax.text(x, y, yazi, ha="center", va="center", fontsize=16, color=YAZI)
# üst satır: p ⇔ q ile denk olanlar
ax.text(3.0, 3.75, "0 ya da 2 değil: değer aynı kalır", ha="center", fontsize=12, color=YESIL, fontweight="bold")
kutu(1.6, 3.0, "p ⇔ q", YESIL, YESIL_ACIK)
ax.text(3.0, 3.0, "≡", ha="center", va="center", fontsize=20, color=YESIL)
kutu(4.4, 3.0, "p′ ⇔ q′", YESIL, YESIL_ACIK)
# alt satır: değili
ax.text(3.0, 1.75, "1 değil: değer değişir", ha="center", fontsize=12, color=KIRMIZI, fontweight="bold")
kutu(0.85, 1.0, "p′ ⇔ q", KIRMIZI, KIRMIZI_ACIK)
ax.text(2.075, 1.0, "≡", ha="center", va="center", fontsize=20, color=KIRMIZI)
kutu(3.3, 1.0, "p ⇔ q′", KIRMIZI, KIRMIZI_ACIK)
ax.text(4.525, 1.0, "≡", ha="center", va="center", fontsize=20, color=KIRMIZI)
kutu(5.75, 1.0, "(p ⇔ q)′", KIRMIZI, KIRMIZI_ACIK)
ax.set_xlim(-0.2, 6.8); ax.set_ylim(0.45, 4.05)
kaydet(fig, __file__)
