import sys; sys.path.insert(0, "tools")
from cizim import *

# Solda A ⊂ B (A, B'nin içinde); sağda A ile B ayrık (ortak eleman yok).
fig, axs = plt.subplots(1, 2, figsize=(6.2, 3.5))
ax = axs[0]
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 6); ax.set_ylim(-1.9, 4.6)
ax.add_patch(patches.Ellipse((3.0, 2.4), 5.2, 3.8, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2))
ax.add_patch(patches.Ellipse((2.6, 2.1), 2.4, 1.9, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.text(2.6, 2.1, "A", fontsize=17, fontweight="bold", color=MAVI, ha="center", va="center")
ax.text(4.7, 3.3, "B", fontsize=17, fontweight="bold", color=YESIL, ha="center", va="center")
ax.text(3.0, -0.35, "A ⊂ B", fontsize=15, fontweight="bold", ha="center")
ax.text(3.0, -0.95, "A ∩ B = A", fontsize=12.5, ha="center", color=SOLUK)
ax.text(3.0, -1.5, "A ∪ B = B", fontsize=12.5, ha="center", color=SOLUK)
ax = axs[1]
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 6); ax.set_ylim(-1.9, 4.6)
ax.add_patch(patches.Circle((1.6, 2.0), 1.3, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.add_patch(patches.Circle((4.4, 2.0), 1.3, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2))
ax.text(1.6, 2.0, "A", fontsize=17, fontweight="bold", color=MAVI, ha="center", va="center")
ax.text(4.4, 2.0, "B", fontsize=17, fontweight="bold", color=YESIL, ha="center", va="center")
ax.text(3.0, -0.35, "Ayrık kümeler", fontsize=15, fontweight="bold", ha="center")
ax.text(3.0, -0.95, "A ∩ B = ∅", fontsize=12.5, ha="center", color=SOLUK)
ax.text(3.0, -1.5, "s(A ∪ B) = s(A) + s(B)", fontsize=12.5, ha="center", color=SOLUK)
fig.subplots_adjust(wspace=0.12)
kaydet(fig, __file__)
