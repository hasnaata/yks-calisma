import sys; sys.path.insert(0, "tools")
from cizim import *

# p: a > 3 ile değili p': a ≤ 3. 3 noktası p'de dolu, p'de boş.
fig, axs = plt.subplots(2, 1, figsize=(6, 2.6))
for ax, ad, renk, dolu, yon in ((axs[0], "p:  a > 3", MAVI, False, 1), (axs[1], "p′:  a ≤ 3", KIRMIZI, True, -1)):
    sayi_dogrusu(ax, -1, 7)
    bas, son = (3, 7.45) if yon == 1 else (3, -1.45)
    ax.annotate("", xy=(son, 0.0), xytext=(bas, 0.0), arrowprops=dict(arrowstyle="->", color=renk, lw=3.2))
    nokta(ax, 3, 0, renk=renk, dolu=dolu)
    ax.text(-1.55, 0.55, ad, ha="left", va="center", color=renk, fontsize=13, fontweight="bold")
kaydet(fig, __file__)
