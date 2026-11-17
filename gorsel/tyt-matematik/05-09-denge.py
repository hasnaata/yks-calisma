import sys; sys.path.insert(0, "tools")
from cizim import *

# Karışımın yüzdesi iki yüzde arasında, miktarı çok olana yakın: 10 (200 g) ve 25 (100 g) -> 15. Uzaklıklar 5 ve 10.
fig, ax = sekil(6.0, 2.6)
sayi_dogrusu(ax, 8, 27, isaretler=[10, 15, 25])
ax.set_ylim(-1.3, 1.5)
for v, m, renk in [(10, "200 g", MAVI), (25, "100 g", MAVI)]:
    nokta(ax, v, 0, renk=renk)
    ax.text(v, 0.3, m, ha="center", va="bottom", color=renk, fontsize=12, fontweight="bold")
nokta(ax, 15, 0, renk=YESIL)
ax.text(15, 0.3, "karışım", ha="center", va="bottom", color=YESIL, fontsize=12, fontweight="bold")
for a, b, ad in [(10, 15, "5"), (15, 25, "10")]:
    ax.annotate("", xy=(b, -0.75), xytext=(a, -0.75), arrowprops=dict(arrowstyle="<->", color=SARI, lw=1.3))
    ax.text((a + b) / 2, -0.85, ad, ha="center", va="top", color=SARI, fontsize=12, fontweight="bold")
ax.text(17.5, 1.15, "uzaklıklar 1 : 2   ·   miktarlar 2 : 1", ha="center", va="center", color=YAZI, fontsize=11)
kaydet(fig, __file__)
