import sys; sys.path.insert(0, "tools")
from cizim import *

# Denklem sisteminin üç durumu: kesişen, paralel, çakışık doğrular.
xs = np.linspace(0, 5.5, 20)
paneller = [
    ("Kesişir: tek çözüm (3, 2)", 5 - xs, xs - 1, "x + y = 5", "x − y = 1"),
    ("Paralel: ÇK = ∅", 2 - xs / 2, 3 - xs / 2, "x + 2y = 4", "2x + 4y = 12"),
    ("Çakışık: sonsuz çözüm", 2 - xs / 2, 2 - xs / 2, "x + 2y = 4", "2x + 4y = 8"),
]
fig, eks = plt.subplots(3, 1, figsize=(5.4, 8.2))
for ax, (baslik, d1, d2, ad1, ad2) in zip(eks, paneller):
    ax.set_xlim(0, 6); ax.set_ylim(-1.5, 5.5)
    for k in ("top", "right"): ax.spines[k].set_visible(False)
    ax.spines["left"].set_position(("data", 0)); ax.spines["bottom"].set_position("zero")
    ax.set_xticks([1, 2, 3, 4, 5]); ax.set_yticks([1, 2, 3, 4])
    ax.grid(True, color=CIZGI, lw=0.6, alpha=0.7); ax.set_axisbelow(True)
    ax.plot(xs, d1, color=MAVI, lw=2.6, label=ad1)
    if baslik.startswith("Çakışık"):
        ax.plot(xs, d2, color=KIRMIZI, lw=2, ls=(0, (5, 4)), label=ad2)
    else:
        ax.plot(xs, d2, color=KIRMIZI, lw=2.6, label=ad2)
    ax.set_title(baslik, fontsize=14, loc="left", color=YAZI, pad=34)
    ax.legend(loc="lower left", bbox_to_anchor=(-0.02, 0.98), ncol=2, fontsize=12, frameon=False, handlelength=1.6, columnspacing=1.2)
nokta(eks[0], 3, 2, "", renk=YESIL)
eks[0].plot(3, 2, "o", color=YESIL, markersize=10, zorder=6)
fig.subplots_adjust(hspace=0.75)
kaydet(fig, __file__)
