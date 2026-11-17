import sys; sys.path.insert(0, "tools")
from cizim import *

# Sınırsız aralıklar: sonsuz tarafta nokta yok, ok var.
# (gösterim, eşitsizlik, sol uç, sol dolu mu, sağ uç, sağ dolu mu); None = sonsuz
SATIRLAR = [
    ("(1, ∞)", "x > 1", 1, False, None, None),
    ("[1, ∞)", "x ≥ 1", 1, True, None, None),
    ("(−∞, 1]", "x ≤ 1", None, None, 1, True),
    ("(−∞, ∞)", "ℝ", None, None, None, None),
]
LO, HI = -3, 4
fig, eks = plt.subplots(len(SATIRLAR), 1, figsize=(6, 5.2))
for ax, (gosterim, esitsizlik, sol, sold, sag, sagd) in zip(eks, SATIRLAR):
    sayi_dogrusu(ax, LO, HI)
    x1 = sol if sol is not None else LO - 0.2
    x2 = sag if sag is not None else HI + 0.2
    ax.hlines(0, x1, x2, color=MAVI, lw=5, zorder=3)
    if sol is None:
        ax.annotate("", xy=(LO - 0.6, 0), xytext=(LO - 0.1, 0), arrowprops=dict(arrowstyle="-|>,head_width=0.35,head_length=0.6", color=MAVI, lw=3), zorder=4)
    else:
        ax.plot(sol, 0, "o", color=MAVI, markerfacecolor=MAVI if sold else "white", markersize=11, mew=2.2, zorder=5)
    if sag is None:
        ax.annotate("", xy=(HI + 0.6, 0), xytext=(HI + 0.1, 0), arrowprops=dict(arrowstyle="-|>,head_width=0.35,head_length=0.6", color=MAVI, lw=3), zorder=4)
    else:
        ax.plot(sag, 0, "o", color=MAVI, markerfacecolor=MAVI if sagd else "white", markersize=11, mew=2.2, zorder=5)
    ax.text(5.0, 0.12, gosterim, va="center", fontsize=15, color=YAZI)
    ax.text(5.0, -0.42, esitsizlik, va="center", fontsize=12, color=SOLUK)
    ax.set_xlim(-3.7, 7.4)
kaydet(fig, __file__)
