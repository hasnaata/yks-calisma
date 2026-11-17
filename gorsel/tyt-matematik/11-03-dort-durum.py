import sys; sys.path.insert(0, "tools")
from cizim import *

# Dört durum: içine-bire bir, içine-bire bir değil, örten-bire bir değil, bire bir ve örten.
fig, eks = plt.subplots(2, 2, figsize=(6.5, 6.6))

def panel(ax, sol, sag, oklar, baslik, renk, bosta=(), cift=()):
    ax.axis("off"); ax.set_xlim(-0.2, 3.2); ax.set_ylim(-1.5, 4.4)
    for x, ad in ((0.6, "A"), (2.4, "B")):
        ax.add_patch(patches.Ellipse((x, 1.9), 1.0, 3.1, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
        ax.text(x, 3.65, ad, ha="center", fontsize=15, color=MAVI, fontweight="bold")
    def y(el, i): return 1.9 + (len(el) - 1) / 2 * 0.8 - i * 0.8
    for i, e in enumerate(sol): ax.text(0.6, y(sol, i), e, ha="center", va="center", fontsize=14)
    for i, e in enumerate(sag):
        r = KIRMIZI if e in bosta else (SARI if e in cift else YAZI)
        ax.text(2.4, y(sag, i), e, ha="center", va="center", fontsize=14, color=r)
        if e in bosta or e in cift:
            ax.add_patch(patches.Circle((2.4, y(sag, i)), 0.26, fill=False, edgecolor=r, lw=1.8))
    for s, t in oklar:
        ax.annotate("", xy=(2.1, y(sag, sag.index(t))), xytext=(0.88, y(sol, sol.index(s))),
                    arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.6, shrinkA=0, shrinkB=0))
    ax.text(1.5, 0.05, baslik, ha="center", va="top", fontsize=12.5, color=renk, fontweight="bold")

abc = ["a", "b", "c"]
panel(eks[0][0], ["1", "2"], abc, [("1", "a"), ("2", "b")], "İçine\nbire bir", MAVI, bosta=("c",))
panel(eks[0][1], ["1", "2", "3"], abc, [("1", "a"), ("2", "a"), ("3", "b")],
      "İçine\nbire bir değil", KIRMIZI, bosta=("c",), cift=("a",))
panel(eks[1][0], ["1", "2", "3"], ["a", "b"], [("1", "a"), ("2", "b"), ("3", "b")],
      "Örten\nbire bir değil", SARI, cift=("b",))
panel(eks[1][1], ["1", "2", "3"], abc, [("1", "b"), ("2", "c"), ("3", "a")],
      "Bire bir\nve örten", YESIL)
fig.subplots_adjust(wspace=0.05, hspace=0.02)
kaydet(fig, __file__)
