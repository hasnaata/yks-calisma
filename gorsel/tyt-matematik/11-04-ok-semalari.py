import sys; sys.path.insert(0, "tools")
from cizim import *

# Sol: birim fonksiyon I: A -> A, her eleman kendisine gider.
# Sağ: sabit fonksiyon f: A -> B, f(x) = 7; 3 ve 9 boşta (içine).
fig, eks = plt.subplots(1, 2, figsize=(6.5, 3.9))

def panel(ax, adlar, sol, sag, oklar, baslik, renk, bosta=(), hedef=()):
    ax.axis("off"); ax.set_xlim(-0.2, 3.2); ax.set_ylim(-1.5, 5.0)
    for x, ad in zip((0.6, 2.4), adlar):
        ax.add_patch(patches.Ellipse((x, 2.2), 1.1, 3.9, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
        ax.text(x, 4.35, ad, ha="center", fontsize=15, color=MAVI, fontweight="bold")
    def y(el, i): return 2.2 + (len(el) - 1) / 2 * 0.8 - i * 0.8
    for i, e in enumerate(sol): ax.text(0.6, y(sol, i), e, ha="center", va="center", fontsize=14)
    for i, e in enumerate(sag):
        r = KIRMIZI if e in bosta else (YESIL if e in hedef else YAZI)
        ax.text(2.4, y(sag, i), e, ha="center", va="center", fontsize=14, color=r,
                fontweight="bold" if e in hedef else "normal")
        if e in bosta:
            ax.add_patch(patches.Circle((2.4, y(sag, i)), 0.27, fill=False, edgecolor=KIRMIZI, lw=1.8))
    for s, t in oklar:
        ax.annotate("", xy=(2.13, y(sag, sag.index(t))), xytext=(0.87, y(sol, sol.index(s))),
                    arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.6, shrinkA=0, shrinkB=0))
    ax.text(1.5, -0.1, baslik, ha="center", va="top", fontsize=13, color=renk, fontweight="bold")

A = ["1", "2", "3", "4"]
panel(eks[0], ("A", "A"), A, A, [(e, e) for e in A], "Birim: I(x) = x", MAVI)
S = ["−1", "0", "2", "5"]
panel(eks[1], ("A", "B"), S, ["3", "7", "9"], [(e, "7") for e in S], "Sabit: f(x) = 7", YESIL,
      bosta=("3", "9"), hedef=("7",))
fig.subplots_adjust(wspace=0.05)
kaydet(fig, __file__)
