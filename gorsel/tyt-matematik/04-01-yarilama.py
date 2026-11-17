import sys; sys.path.insert(0, "tools")
from cizim import *

# Üs 1 azaldıkça değer yarıya iner: 2^0 = 1 ve 2^−1 = 1/2 bu düzenden gelir.
fig, ax = sekil(6.2, 2.6)
ax.axis("off"); ax.set_xlim(-0.6, 5.6); ax.set_ylim(-0.7, 1.5)
usler = ["$2^{3}$", "$2^{2}$", "$2^{1}$", "$2^{0}$", "$2^{−1}$", "$2^{−2}$"]
deger = ["8", "4", "2", "1", r"$\frac{1}{2}$", r"$\frac{1}{4}$"]
for i, (u, v) in enumerate(zip(usler, deger)):
    yeni = i >= 3
    ax.add_patch(patches.FancyBboxPatch((i - 0.36, -0.55), 0.72, 1.1, boxstyle="round,pad=0.02",
                 facecolor=SARI_ACIK if yeni else MAVI_ACIK, edgecolor=SARI if yeni else MAVI, lw=1.6))
    ax.text(i, 0.22, u, ha="center", va="center", fontsize=15, color=SARI if yeni else MAVI)
    ax.text(i, -0.22, v, ha="center", va="center", fontsize=16 if i < 4 else 18, color=YAZI)
    if i < 5:
        ax.annotate("", xy=(i + 0.88, 0.62), xytext=(i + 0.12, 0.62),
                    arrowprops=dict(arrowstyle="-|>", color=SOLUK, lw=1.5, mutation_scale=14, connectionstyle="arc3,rad=-0.45"))
        ax.text(i + 0.5, 1.08, "÷2", ha="center", va="center", fontsize=13, color=SOLUK)
kaydet(fig, __file__)
