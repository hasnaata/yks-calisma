import sys; sys.path.insert(0, "tools")
from cizim import *

# √20 ≈ 4,47 ve √90 ≈ 9,49 sayı doğrusunda; aralarındaki tam sayılar 5, 6, 7, 8, 9.
fig, ax = sekil(6, 2.3)
sayi_dogrusu(ax, 4, 10)
ax.hlines(0, np.sqrt(20), np.sqrt(90), color=MAVI_ACIK, lw=9, zorder=2)
for n in range(5, 10):
    ax.plot(n, 0, "o", color=MAVI, markersize=8, zorder=5)
for v, ad in ((np.sqrt(20), "$\\sqrt{20}$"), (np.sqrt(90), "$\\sqrt{90}$")):
    ax.plot([v, v], [-0.12, 0.12], color=KIRMIZI, lw=2.4, zorder=6)
    ax.text(v, 0.3, ad, ha="center", va="bottom", color=KIRMIZI, fontsize=14)
ax.text(4.3, 0.95, "16 < 20 < 25", ha="center", fontsize=11, color=SOLUK)
ax.text(9.6, 0.95, "81 < 90 < 100", ha="center", fontsize=11, color=SOLUK)
ax.set_ylim(-0.8, 1.3)
kaydet(fig, __file__)
