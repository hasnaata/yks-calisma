import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 10: A = [−4, 3) ve B = (0, 6] aynı ölçekte alt alta.
SATIRLAR = [("A", MAVI, -4, True, 3, False), ("B", SARI, 0, False, 6, True)]
fig, eks = plt.subplots(2, 1, figsize=(6, 2.8))
for ax, (ad, renk, a, ad_, b, bd) in zip(eks, SATIRLAR):
    sayi_dogrusu(ax, -5, 7)
    ax.hlines(0, a, b, color=renk, lw=5, zorder=3)
    for x, dolu in ((a, ad_), (b, bd)):
        ax.plot(x, 0, "o", color=renk, markerfacecolor=renk if dolu else "white", markersize=11, mew=2.2, zorder=5)
    ax.text(-6.9, 0, ad, va="center", fontsize=15, color=renk, fontweight="bold")
    ax.set_xlim(-7.2, 7.8)
kaydet(fig, __file__)
