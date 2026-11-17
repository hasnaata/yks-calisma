import sys; sys.path.insert(0, "tools")
from cizim import *

# Üç ok şeması. A = {1, 2, 3, 4}, B = {0, 1, 2}.
# 1) Her sayıyı 3'e bölümünden kalana eşleyen kural: fonksiyon.
# 2) Aynı eşlemenin tersi (B'den A'ya): 1'den iki ok çıkar, fonksiyon değil.
# 3) A'dan B'ye, 4'ten ok çıkmıyor: fonksiyon değil.
fig, eks = plt.subplots(1, 3, figsize=(6.5, 3.5))

def panel(ax, sol, sag, oklar, baslik, renk, sol_ad, sag_ad, kirmizi=()):
    ax.axis("off"); ax.set_xlim(-0.2, 3.2); ax.set_ylim(-1.3, 5.0)
    for x, el, ad in ((0.6, sol, sol_ad), (2.4, sag, sag_ad)):
        ax.add_patch(patches.Ellipse((x, 2.2), 1.1, 3.9, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
        ax.text(x, 4.35, ad, ha="center", fontsize=15, color=MAVI, fontweight="bold")
    def y(el, i): return 2.2 + (len(el) - 1) / 2 * 0.8 - i * 0.8
    for i, e in enumerate(sol): ax.text(0.6, y(sol, i), e, ha="center", va="center", fontsize=14)
    for i, e in enumerate(sag): ax.text(2.4, y(sag, i), e, ha="center", va="center", fontsize=14)
    for s, t in oklar:
        r = KIRMIZI if s in kirmizi else SOLUK
        ax.annotate("", xy=(2.13, y(sag, sag.index(t))), xytext=(0.87, y(sol, sol.index(s))),
                    arrowprops=dict(arrowstyle="->", color=r, lw=1.6, shrinkA=0, shrinkB=0))
    ax.text(1.5, -0.1, baslik, ha="center", va="top", fontsize=13, color=renk, fontweight="bold")

A, B = ["1", "2", "3", "4"], ["0", "1", "2"]
panel(eks[0], A, B, [("1", "1"), ("2", "2"), ("3", "0"), ("4", "1")], "Fonksiyon", YESIL, "A", "B")
panel(eks[1], B, A, [("1", "1"), ("1", "4"), ("2", "2"), ("0", "3")], "Değil\n(1'den 2 ok)", KIRMIZI, "B", "A", kirmizi=("1",))
panel(eks[2], A, B, [("1", "1"), ("2", "2"), ("3", "0")], "Değil\n(4 boşta)", KIRMIZI, "A", "B")
eks[2].add_patch(patches.Circle((0.6, 2.2 - 1.2), 0.28, fill=False, edgecolor=KIRMIZI, lw=1.8))
fig.subplots_adjust(wspace=0.05)
kaydet(fig, __file__)
