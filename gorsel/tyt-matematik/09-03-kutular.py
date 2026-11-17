import sys; sys.path.insert(0, "tools")
from cizim import *

# P(7, 3): 7 koşucudan ilk üç dereceyi alanlar. Kutu sayısı = r, sayılar n'den birer azalır.
fig, ax = sekil(6, 3.2)
ax.axis("off"); ax.set_aspect("equal")
for i, (s, ad) in enumerate([(7, "1."), (6, "2."), (5, "3.")]):
    x = i * 1.9
    ax.add_patch(patches.FancyBboxPatch((x, 0), 1.2, 1.0, boxstyle="round,pad=0.02,rounding_size=0.1",
                                        facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
    ax.text(x + 0.6, 0.5, str(s), ha="center", va="center", fontsize=22, color=MAVI, fontweight="bold")
    ax.text(x + 0.6, -0.3, ad, ha="center", va="top", fontsize=12, color=SOLUK)
    if i < 2: ax.text(x + 1.55, 0.5, "·", ha="center", va="center", fontsize=24, color=YAZI)
ax.text(5.15, 0.5, "= 210", va="center", fontsize=18, color=YAZI)
ax.text(0, 1.45, "3 kutu: ilk üç derece", fontsize=13, color=MAVI, fontweight="bold")
ax.text(0, -1.25, r"$P(7,3)=\dfrac{7!}{4!}=7\cdot 6\cdot 5$", fontsize=15, color=YESIL)
ax.set_xlim(-0.1, 7.2); ax.set_ylim(-1.8, 2.0)
kaydet(fig, __file__)
