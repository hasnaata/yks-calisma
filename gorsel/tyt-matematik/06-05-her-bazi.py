import sys; sys.path.insert(0, "tools")
from cizim import *

# Dört kutu: her kutu evrensel küme E, boyalı bölge doğruluk kümesi D.
fig, axs = plt.subplots(2, 2, figsize=(6, 4.6))
noktalar = [(0.6, 1.45), (1.5, 1.6), (2.4, 1.4), (0.8, 0.75), (1.75, 0.85), (2.6, 0.7)]
durumlar = [
    (axs[0][0], "∀x, p(x)", "D = E", "1", set(range(6)), YESIL),
    (axs[0][1], "∀x, p(x)", "bir eleman dışarıda", "0", set(range(5)), KIRMIZI),
    (axs[1][0], "∃x, p(x)", "D boş değil", "1", {4}, YESIL),
    (axs[1][1], "∃x, p(x)", "D = ∅", "0", set(), KIRMIZI),
]
for ax, baslik, aciklama, deger, icerde, renk in durumlar:
    ax.axis("off"); ax.set_aspect("equal")
    ax.set_xlim(-0.1, 3.3); ax.set_ylim(-0.75, 2.75)
    ax.add_patch(patches.FancyBboxPatch((0.1, 0.25), 2.95, 1.75, boxstyle="round,pad=0.02,rounding_size=0.12",
                 facecolor="white", edgecolor=SOLUK, lw=1.1))
    for i, (x, y) in enumerate(noktalar):
        if i in icerde:
            ax.add_patch(patches.Circle((x, y), 0.27, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.2))
            ax.plot(x, y, "o", color=MAVI, markersize=6)
        else:
            ax.plot(x, y, "o", color=KIRMIZI if baslik.startswith("∀") else SOLUK, markerfacecolor="white", markersize=7, mew=1.6)
    ax.text(0.1, 2.4, baslik, fontsize=13, fontweight="bold", color=MAVI, va="center")
    ax.text(3.05, 2.4, deger, fontsize=17, fontweight="bold", color=renk, va="center", ha="right")
    ax.text(1.575, -0.2, aciklama, fontsize=11.5, color=renk, ha="center", va="center")
fig.subplots_adjust(wspace=0.12, hspace=0.12)
kaydet(fig, __file__)
