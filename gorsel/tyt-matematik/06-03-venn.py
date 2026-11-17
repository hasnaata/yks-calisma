import sys; sys.path.insert(0, "tools")
from cizim import *
from matplotlib.path import Path

# p ⇒ q ≡ p' ∨ q: yalnızca "p var, q yok" bölgesi yanlış (0), geri kalan her yer doğru (1).
fig, ax = sekil(5.6, 3.9)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Rectangle((-3.2, -2.1), 6.4, 4.2, facecolor=YESIL_ACIK, edgecolor=SOLUK, lw=1.2))
cp, cq, r = (-0.75, 0), (0.75, 0), 1.45
# yalnız p bölgesi: p dairesi, q dairesi dışarıda kalacak şekilde kırmızıya boyanır
ax.add_patch(patches.Circle(cp, r, facecolor=KIRMIZI_ACIK, edgecolor="none"))
ax.add_patch(patches.Circle(cq, r, facecolor=YESIL_ACIK, edgecolor="none"))
ax.add_patch(patches.Circle(cp, r, facecolor="none", edgecolor=MAVI, lw=2))
ax.add_patch(patches.Circle(cq, r, facecolor="none", edgecolor=MAVI, lw=2))
ax.text(-2.05, 1.35, "p", fontsize=17, color=MAVI, fontweight="bold", ha="center")
ax.text(2.05, 1.35, "q", fontsize=17, color=MAVI, fontweight="bold", ha="center")
ax.text(-1.45, 0.05, "0", fontsize=22, color=KIRMIZI, fontweight="bold", ha="center", va="center")
ax.text(-1.45, -0.5, "p:1  q:0", fontsize=10.5, color=KIRMIZI, ha="center", va="center")
ax.text(0, 0.05, "1", fontsize=22, color=YESIL, fontweight="bold", ha="center", va="center")
ax.text(1.45, 0.05, "1", fontsize=22, color=YESIL, fontweight="bold", ha="center", va="center")
ax.text(2.75, -1.75, "1", fontsize=22, color=YESIL, fontweight="bold", ha="center", va="center")
ax.set_xlim(-3.3, 3.3); ax.set_ylim(-2.2, 2.2)
kaydet(fig, __file__)
