import sys; sys.path.insert(0, "tools")
from cizim import *

# A = [−3, 4), B = (1, 6] ve bunlardan elde edilen kümeler aynı ölçekte alt alta.
# Her parça: (sol, sol dolu mu, sağ, sağ dolu mu)
SATIRLAR = [
    ("A", "[−3, 4)", MAVI, [(-3, True, 4, False)]),
    ("B", "(1, 6]", SARI, [(1, False, 6, True)]),
    ("A ∩ B", "(1, 4)", YESIL, [(1, False, 4, False)]),
    ("A ∪ B", "[−3, 6]", YESIL, [(-3, True, 6, True)]),
    ("A \\ B", "[−3, 1]", KIRMIZI, [(-3, True, 1, True)]),
]
fig, eks = plt.subplots(len(SATIRLAR), 1, figsize=(6, 7))
for ax, (ad, gosterim, renk, parcalar) in zip(eks, SATIRLAR):
    sayi_dogrusu(ax, -3, 6)
    for a, ad_, b, bd in parcalar:
        ax.hlines(0, a, b, color=renk, lw=5, zorder=3)
        for x, dolu in ((a, ad_), (b, bd)):
            ax.plot(x, 0, "o", color=renk, markerfacecolor=renk if dolu else "white", markersize=11, mew=2.2, zorder=5)
    ax.text(-3.55, 0.62, ad, va="center", fontsize=15, color=renk, fontweight="bold")
    ax.text(-1.75, 0.62, "= " + gosterim, va="center", fontsize=14, color=YAZI)
    ax.set_ylim(-1, 1.05)
kaydet(fig, __file__)
