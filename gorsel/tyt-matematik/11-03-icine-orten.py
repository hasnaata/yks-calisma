import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = x^2, A = {-1, 0, 1, 2}. Görüntüler: 1, 0, 1, 4; f(A) = {0, 1, 4}.
# Sol: B = {0, 1, 2, 4}, 2 boşta -> içine.  Sağ: B = {0, 1, 4} -> örten.
fig, eks = plt.subplots(1, 2, figsize=(6.5, 3.9))

def panel(ax, sol, sag, oklar, baslik, renk, bosta=()):
    ax.axis("off"); ax.set_xlim(-0.2, 3.2); ax.set_ylim(-1.5, 5.0)
    for x, ad in ((0.6, "A"), (2.4, "B")):
        ax.add_patch(patches.Ellipse((x, 2.2), 1.1, 3.9, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
        ax.text(x, 4.35, ad, ha="center", fontsize=15, color=MAVI, fontweight="bold")
    def y(el, i): return 2.2 + (len(el) - 1) / 2 * 0.8 - i * 0.8
    for i, e in enumerate(sol): ax.text(0.6, y(sol, i), e, ha="center", va="center", fontsize=14)
    for i, e in enumerate(sag):
        ax.text(2.4, y(sag, i), e, ha="center", va="center", fontsize=14, color=KIRMIZI if e in bosta else YAZI)
        if e in bosta:
            ax.add_patch(patches.Circle((2.4, y(sag, i)), 0.27, fill=False, edgecolor=KIRMIZI, lw=1.8))
    for s, t in oklar:
        ax.annotate("", xy=(2.13, y(sag, sag.index(t))), xytext=(0.87, y(sol, sol.index(s))),
                    arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.6, shrinkA=0, shrinkB=0))
    ax.text(1.5, -0.1, baslik, ha="center", va="top", fontsize=13, color=renk, fontweight="bold")

A = ["−1", "0", "1", "2"]
oklar = [("−1", "1"), ("0", "0"), ("1", "1"), ("2", "4")]
panel(eks[0], A, ["0", "1", "2", "4"], oklar, "İçine\n(2 boşta)", KIRMIZI, bosta=("2",))
panel(eks[1], A, ["0", "1", "4"], oklar, "Örten\n(boşta yok)", YESIL)
fig.subplots_adjust(wspace=0.05)
kaydet(fig, __file__)
