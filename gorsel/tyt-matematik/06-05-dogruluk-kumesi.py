import sys; sys.path.insert(0, "tools")
from cizim import *

# p(x): x² < 10. Aynı açık önerme, iki evrensel küme: Z'de 7, N'de 4 eleman.
fig, axs = plt.subplots(2, 1, figsize=(6, 2.9))
k = 10 ** 0.5
for ax, ad, evren, bas in ((axs[0], "x ∈ ℤ:  {−3, −2, −1, 0, 1, 2, 3}", range(-5, 6), -k),
                           (axs[1], "x ∈ ℕ:  {0, 1, 2, 3}", range(0, 6), 0)):
    sayi_dogrusu(ax, -5, 5)
    ax.plot([bas, k], [0, 0], color=MAVI_ACIK, lw=9, solid_capstyle="butt", zorder=1)
    for t in evren:
        icinde = t * t < 10
        ax.plot(t, 0, "o", markersize=9 if icinde else 7, zorder=5,
                color=MAVI if icinde else SOLUK, markerfacecolor=MAVI if icinde else "white")
    ax.text(-5.55, 0.62, ad, ha="left", va="center", color=MAVI, fontsize=12.5, fontweight="bold")
fig.subplots_adjust(hspace=0.35)
kaydet(fig, __file__)
