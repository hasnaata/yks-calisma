import sys; sys.path.insert(0, "tools")
from cizim import *

# İç içe sayı kümeleri: R = Q ∪ Q'; N ⊂ Z ⊂ Q. Her bölgede örnek sayılar.
fig, ax = sekil(6, 4.3)
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 7.2); ax.set_aspect("equal")

def kutu(x, y, w, h, renk, dolgu, ad, adx, ady):
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.25",
                                        linewidth=2, edgecolor=renk, facecolor=dolgu))
    ax.text(adx, ady, ad, color=renk, fontsize=16, fontweight="bold", va="top")

kutu(0.1, 0.1, 9.8, 6.6, SOLUK, "white", "ℝ", 0.3, 7.12)                   # gerçek sayılar
kutu(0.3, 0.3, 6.3, 6.2, MAVI, MAVI_ACIK, "ℚ", 0.5, 6.35)                  # rasyonel
kutu(6.8, 0.3, 2.9, 6.2, KIRMIZI, KIRMIZI_ACIK, "ℚ′", 7.0, 6.35)         # irrasyonel
kutu(0.6, 0.6, 4.2, 4.6, SARI, SARI_ACIK, "ℤ", 0.8, 5.05)                  # tam sayılar
kutu(0.9, 0.9, 2.5, 2.9, YESIL, YESIL_ACIK, "ℕ", 1.1, 3.65)                # doğal sayılar

ax.text(2.15, 2.0, "0   7\n\n√9", ha="center", va="center", fontsize=14)
ax.text(4.1, 2.3, "−4\n\n−√16", ha="center", va="center", fontsize=14)
ax.text(5.7, 3.0, "2\n—\n3", ha="center", va="center", fontsize=13, linespacing=0.75)
ax.text(5.7, 1.3, "0,75", ha="center", va="center", fontsize=14)
ax.text(2.9, 5.85, "−1,5", ha="center", va="center", fontsize=14)
ax.text(8.25, 3.4, "√2\n\nπ\n\n−√7", ha="center", va="center", fontsize=14)
ax.text(0.3, 7.12, "", fontsize=1)
kaydet(fig, __file__)
