import sys; sys.path.insert(0, "tools")
from cizim import *

# √20 ≈ 4,47 (16 < 20 < 25) ve √30 ≈ 5,48 (25 < 30 < 36) sayı doğrusunda.
fig, ax = sekil(6, 2.2)
sayi_dogrusu(ax, 3, 7)
ax.set_ylim(-1, 1.25)
for t, kare in ((3, "√9"), (4, "√16"), (5, "√25"), (6, "√36"), (7, "√49")):
    ax.text(t, 0.22, kare, ha="center", va="bottom", color=SOLUK, fontsize=11)
for deger, ad, renk in ((20 ** 0.5, "√20", KIRMIZI), (30 ** 0.5, "√30", MAVI)):
    ax.plot(deger, 0, "o", color=renk, markersize=8, zorder=5)
    ax.annotate(ad, xy=(deger, 0.05), xytext=(deger, 0.8), ha="center", va="bottom", color=renk, fontsize=13,
                arrowprops=dict(arrowstyle="-", color=renk, lw=1.2))
kaydet(fig, __file__)
