import sys; sys.path.insert(0, "tools")
from cizim import *

# 1'den 30'a kadar numaralı kartlar. A: 2'ye bölünen (15), B: 3'e bölünen (10), A ∩ B: 6'ya bölünen (5).
# Yalnız A: 10, yalnız B: 5, ikisi de değil: 10.
fig, ax = sekil(6, 3.9)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.1, 6.1); ax.set_ylim(-0.75, 4.3)
ax.add_patch(patches.Rectangle((0, 0), 6, 3.9, facecolor="none", edgecolor=SOLUK, lw=1.4))
ax.text(0.15, 0.15, "E (30 kart)", fontsize=13, color=SOLUK, va="bottom")
ax.add_patch(patches.Circle((2.35, 1.8), 1.35, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2, alpha=0.75))
ax.add_patch(patches.Circle((3.75, 1.8), 1.2, facecolor=SARI_ACIK, edgecolor=SARI, lw=2, alpha=0.75))
ax.text(1.45, 3.35, "A: 2'ye bölünen", color=MAVI, fontsize=12, ha="center", fontweight="bold")
ax.text(4.55, 3.35, "B: 3'e bölünen", color=SARI, fontsize=12, ha="center", fontweight="bold")
ax.text(1.7, 1.8, "10", fontsize=18, ha="center", va="center")
ax.text(3.05, 1.8, "5", fontsize=18, ha="center", va="center", color=YESIL, fontweight="bold")
ax.text(4.35, 1.8, "5", fontsize=18, ha="center", va="center")
ax.text(5.55, 0.35, "10", fontsize=16, ha="center", va="center", color=SOLUK)
ax.text(3, -0.4, "s(A ∪ B) = 15 + 10 − 5 = 20", ha="center", fontsize=14, color=YESIL)
kaydet(fig, __file__)
