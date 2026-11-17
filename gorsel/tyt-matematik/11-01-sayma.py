import sys; sys.path.insert(0, "tools")
from cizim import *

# A = {a, b}, B = {1, 2, 3}: f(a) için 3, f(b) için 3 seçim, 3 · 3 = 9 fonksiyon.
# Yeşil satır: f(a) = 1 koşulunu sağlayan 3 fonksiyon.
fig, ax = sekil(5.4, 3.9)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-1.9, 6.2); ax.set_ylim(-0.75, 4.9)
H = 1.25
for i, fa in enumerate((1, 2, 3)):
    y = 3 - i
    for j, fb in enumerate((1, 2, 3)):
        x = j * 1.6
        renk, acik = (YESIL, YESIL_ACIK) if fa == 1 else (MAVI, MAVI_ACIK)
        ax.add_patch(patches.FancyBboxPatch((x + 0.08, y + 0.1), 1.44, 0.8, boxstyle="round,pad=0,rounding_size=0.12",
                                            facecolor=acik, edgecolor=renk, lw=1.4))
        ax.text(x + 0.8, y + 0.5, f"{fa} , {fb}", ha="center", va="center", fontsize=15)
    ax.text(-0.25, y + 0.5, f"f(a) = {fa}", ha="right", va="center", fontsize=13,
            color=YESIL if fa == 1 else YAZI)
for j, fb in enumerate((1, 2, 3)):
    ax.text(j * 1.6 + 0.8, 4.3, f"f(b) = {fb}", ha="center", va="center", fontsize=13)
ax.text(2.4, 0.4, "her kutu bir fonksiyon:  (f(a) , f(b))", ha="center", va="center", fontsize=12, color=SOLUK)
ax.text(2.4, -0.35, "3 · 3 = 9 fonksiyon", ha="center", va="center", fontsize=15, color=MAVI, fontweight="bold")
kaydet(fig, __file__)
