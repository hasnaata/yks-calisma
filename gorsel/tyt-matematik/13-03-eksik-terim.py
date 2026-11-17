import sys; sys.path.insert(0, "tools")
from cizim import *

# (x⁴ − 3x² + 2x + 5) ÷ (x² + x − 1): eksik x³ terimi 0x³ olarak yazılır.
# Bölüm x² − x − 1, kalan 2x + 4.
fig, ax = sekil(6, 4.9)
ax.axis("off"); ax.set_xlim(0, 11.7); ax.set_ylim(-0.2, 7.6)
sut = {4: 1.1, 3: 2.6, 2: 4.15, 1: 5.6, 0: 6.85}
FS = 15

def satir(y, terimler, renk=YAZI):
    for d, t in terimler.items():
        ax.text(sut[d], y, t, ha="center", va="center", fontsize=FS, color=renk)

def cikar(y, terimler, x0, x1):
    ax.text(0.25, y, "−", ha="center", va="center", fontsize=FS + 2, color=KIRMIZI)
    satir(y, terimler, KIRMIZI)
    ax.plot([x0, x1], [y - 0.42, y - 0.42], color=YAZI, lw=1.3)

ys = [6.6, 5.7, 4.75, 3.85, 2.9, 2.0, 1.05]
ax.add_patch(patches.FancyBboxPatch((1.88, ys[0] - 0.33), 1.45, 0.66, boxstyle="round,pad=0.05",
             fc=SARI_ACIK, ec=SARI, lw=1.3))
satir(ys[0], {4: "$x^4$", 2: "$-3x^2$", 1: "$+2x$", 0: "$+5$"})
ax.text(sut[3], ys[0], "$+0x^3$", ha="center", va="center", fontsize=FS, color=SARI)
cikar(ys[1], {4: "$x^4$", 3: "$+x^3$", 2: "$-x^2$"}, 0.5, 5.0)
satir(ys[2], {3: "$-x^3$", 2: "$-2x^2$", 1: "$+2x$", 0: "$+5$"})
cikar(ys[3], {3: "$-x^3$", 2: "$-x^2$", 1: "$+x$"}, 1.9, 6.3)
satir(ys[4], {2: "$-x^2$", 1: "$+x$", 0: "$+5$"})
cikar(ys[5], {2: "$-x^2$", 1: "$-x$", 0: "$+1$"}, 3.4, 7.4)
ax.add_patch(patches.FancyBboxPatch((5.05, ys[6] - 0.32), 2.3, 0.64, boxstyle="round,pad=0.05",
             fc=YESIL_ACIK, ec=YESIL, lw=1.3))
satir(ys[6], {1: "$2x$", 0: "$+4$"}, YESIL)

ax.plot([7.7, 7.7], [7.15, 5.25], color=YAZI, lw=1.6)
ax.plot([7.7, 11.1], [6.15, 6.15], color=YAZI, lw=1.6)
ax.text(9.4, ys[0], "$x^2+x-1$", ha="center", va="center", fontsize=FS)
ax.add_patch(patches.FancyBboxPatch((7.95, 5.38), 2.9, 0.64, boxstyle="round,pad=0.05",
             fc=MAVI_ACIK, ec=MAVI, lw=1.3))
ax.text(9.4, 5.7, "$x^2-x-1$", ha="center", va="center", fontsize=FS, color=MAVI)
ax.text(9.4, 4.85, "Bölüm", ha="center", va="center", fontsize=12, color=MAVI)
ax.text(2.6, 7.35, "eksik terim", ha="center", va="center", fontsize=12, color=SARI)
ax.text(7.7, ys[6], "Kalan", ha="left", va="center", fontsize=12, color=YESIL)
ax.text(0.1, 0.15, "Kalanın derecesi (1), bölenin derecesinden (2) küçük: bölme biter.",
        ha="left", va="center", fontsize=11, color=SOLUK)
kaydet(fig, __file__)
