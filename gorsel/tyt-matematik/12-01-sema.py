import sys; sys.path.insert(0, "tools")
from cizim import *

# Bileşke şeması: f(x) = 2x + 1, g(x) = x². 3 -> f(3) = 7 -> g(7) = 49.
# Üstte f ve g okları, altta doğrudan A'dan C'ye giden g∘f oku.
fig, ax = sekil(6.2, 3.6)
ax.axis("off"); ax.set_xlim(-0.2, 9.2); ax.set_ylim(-1.9, 4.3)
for x, ad in ((1, "A"), (4.5, "B"), (8, "C")):
    ax.add_patch(patches.Ellipse((x, 1.6), 1.9, 3.2, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
    ax.text(x, 3.55, ad, ha="center", fontsize=16, color=MAVI, fontweight="bold")
ax.text(1, 1.6, "3", ha="center", va="center", fontsize=17)
ax.text(4.5, 1.6, "7", ha="center", va="center", fontsize=17)
ax.text(8, 1.6, "49", ha="center", va="center", fontsize=17)
ax.text(1, 0.85, "x", ha="center", va="center", fontsize=12, color=SOLUK)
ax.text(4.5, 0.85, "f(3)", ha="center", va="center", fontsize=12, color=SOLUK)
ax.text(8, 0.85, "g(7)", ha="center", va="center", fontsize=12, color=SOLUK)
ok = dict(arrowstyle="->", lw=1.8, shrinkA=0, shrinkB=0)
ax.annotate("", xy=(4.15, 1.75), xytext=(1.35, 1.75), arrowprops=dict(ok, color=YESIL, connectionstyle="arc3,rad=-0.25"))
ax.annotate("", xy=(7.6, 1.75), xytext=(4.85, 1.75), arrowprops=dict(ok, color=SARI, connectionstyle="arc3,rad=-0.25"))
ax.text(2.75, 2.75, "f: 2x + 1", ha="center", fontsize=13, color=YESIL)
ax.text(6.2, 2.75, "g: x²", ha="center", fontsize=13, color=SARI)
ax.annotate("", xy=(8, -0.05), xytext=(1, -0.05), arrowprops=dict(ok, color=KIRMIZI, connectionstyle="arc3,rad=0.28"))
ax.text(4.5, -1.75, "g∘f :  3 ⟶ 49", ha="center", fontsize=14, color=KIRMIZI, fontweight="bold")
kaydet(fig, __file__)
