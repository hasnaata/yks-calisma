import sys; sys.path.insert(0, "tools")
from cizim import *

# Rasyonel ve irrasyonel sayıların sayı doğrusundaki yaklaşık yerleri.
fig, ax = sekil(6.2, 2.1)
sayi_dogrusu(ax, -3, 4)
NOKTALAR = [  # (değer, etiket, etiket yüksekliği, renk)
    (-7 / 3, "−7/3", 0.42, MAVI),
    (-np.sqrt(2), "−√2", 0.42, KIRMIZI),
    (0.75, "0,75", 0.42, MAVI),
    (np.sqrt(5), "√5", 0.42, KIRMIZI),
    (np.e, "e", 0.82, KIRMIZI),
    (np.pi, "π", 0.42, KIRMIZI),
]
for x, ad, y, renk in NOKTALAR:
    ax.plot(x, 0, "o", color=renk, markersize=8, zorder=5)
    ax.plot([x, x], [0.1, y - 0.1], color=renk, lw=1, zorder=4)
    ax.text(x, y, ad, ha="center", va="bottom", color=renk, fontsize=14)
ax.set_ylim(-0.75, 1.25)
kaydet(fig, __file__)
