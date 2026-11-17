import sys; sys.path.insert(0, "tools")
from cizim import *
from matplotlib.patches import FancyArrowPatch

# Üç ardışık dizi aynı sayı doğrusunda: ardışık tam (+1), ardışık çift (+2), ardışık tek (+2).
fig, axs = plt.subplots(3, 1, figsize=(6, 4.6))
satirlar = [
    ("Ardışık tam sayılar", list(range(-2, 5)), 1, MAVI),
    ("Ardışık çift sayılar", [-2, 0, 2, 4, 6], 2, YESIL),
    ("Ardışık tek sayılar", [-3, -1, 1, 3, 5], 2, KIRMIZI),
]
for ax, (ad, dizi, fark, renk) in zip(axs, satirlar):
    sayi_dogrusu(ax, -3, 6)
    ax.set_ylim(-0.9, 1.45)
    for t in dizi:
        ax.plot(t, 0, "o", color=renk, markersize=9, zorder=5)
    for a, b in zip(dizi[:-1], dizi[1:]):
        ax.add_patch(FancyArrowPatch((a, 0.12), (b, 0.12), connectionstyle="arc3,rad=-0.55",
                                     arrowstyle="-|>", mutation_scale=10, color=renk, lw=1.4))
        ax.text((a + b) / 2, 0.30 + 0.17 * fark, f"+{fark}", ha="center", va="bottom", fontsize=11, color=renk)
    ax.text(-3.55, 1.25, ad, ha="left", va="center", fontsize=13, color=renk, fontweight="bold")
fig.subplots_adjust(hspace=0.15)
kaydet(fig, __file__)
