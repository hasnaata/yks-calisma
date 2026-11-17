import sys; sys.path.insert(0, "tools")
from cizim import *

# Denklemin iki tarafı iki doğru gibi düşünülür: kesişirlerse tek kök, paralelse ÇK = ∅, çakışıksa ÇK = ℝ.
# 1) 2x + 1 = −x + 7 (x = 2)   2) 3x − 1 = 3x + 3 (∅)   3) 2(x + 3) − x = x + 6 (ℝ)
xs = np.linspace(-1, 4, 50)
paneller = [
    ("Tek kök: x = 2", 2 * xs + 1, -xs + 7, "2x + 1", "−x + 7"),
    ("Hiç kesişmez: ÇK = ∅", 3 * xs - 1, 3 * xs + 3, "3x − 1", "3x + 3"),
    ("Her yerde eşit: ÇK = ℝ", 2 * (xs + 3) - xs, xs + 6, "2(x + 3) − x", "x + 6"),
]
fig, eks = plt.subplots(3, 1, figsize=(5.4, 7.4))
for ax, (baslik, sol, sag, sol_ad, sag_ad) in zip(eks, paneller):
    ax.set_xlim(-1, 4.6); ax.set_ylim(-4, 15)
    for k in ("top", "right"): ax.spines[k].set_visible(False)
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
    ax.set_xticks([1, 2, 3, 4]); ax.set_yticks([])
    ax.grid(True, axis="x", color=CIZGI, lw=0.6)
    ax.plot(xs, sol, color=MAVI, lw=2.6, label="sol taraf: " + sol_ad)
    if baslik.startswith("Her"):
        ax.plot(xs, sag, color=KIRMIZI, lw=2, ls=(0, (5, 4)), label="sağ taraf: " + sag_ad)
    else:
        ax.plot(xs, sag, color=KIRMIZI, lw=2.6, label="sağ taraf: " + sag_ad)
    ax.set_title(baslik, fontsize=14, loc="left", color=YAZI)
    ax.legend(loc="upper left", fontsize=11, frameon=False, bbox_to_anchor=(0.0, 1.0))
    ax.text(4.65, 0, "x", va="center")
nokta(eks[0], 2, 5, "", renk=YESIL)
eks[0].plot([2, 2], [0, 5], color=YESIL, ls=":", lw=1.6)
eks[0].text(2.15, 2.6, "x = 2", color=YESIL, fontsize=12)
fig.subplots_adjust(hspace=0.45)
kaydet(fig, __file__)
