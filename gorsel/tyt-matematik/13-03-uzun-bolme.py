import sys; sys.path.insert(0, "tools")
from cizim import *

# (2x³ − 3x² + 4x − 1) ÷ (x − 2) uzun bölmesi: bölüm 2x² + x + 6, kalan 11.
# Terimler derecelerine göre sütunlara yazılır; kırmızı satırlar çıkarılan çarpımlardır.
fig, ax = sekil(6, 4.9)
ax.axis("off"); ax.set_xlim(0, 10.4); ax.set_ylim(-0.2, 7.6)
sut = {3: 1.3, 2: 2.75, 1: 4.2, 0: 5.5}          # x³, x², x, sabit sütunları
FS = 16

def satir(y, terimler, renk=YAZI):
    for d, t in terimler.items():
        ax.text(sut[d], y, t, ha="center", va="center", fontsize=FS, color=renk)

def cikar(y, terimler, x0, x1):
    ax.text(0.3, y, "−", ha="center", va="center", fontsize=FS + 2, color=KIRMIZI)
    satir(y, terimler, KIRMIZI)
    ax.plot([x0, x1], [y - 0.42, y - 0.42], color=YAZI, lw=1.3)

ys = [6.6, 5.7, 4.75, 3.85, 2.9, 2.0, 1.05]
satir(ys[0], {3: "$2x^3$", 2: "$-3x^2$", 1: "$+4x$", 0: "$-1$"})
cikar(ys[1], {3: "$2x^3$", 2: "$-4x^2$"}, 0.6, 3.5)
satir(ys[2], {2: "$x^2$", 1: "$+4x$", 0: "$-1$"})
cikar(ys[3], {2: "$x^2$", 1: "$-2x$"}, 2.0, 4.9)
satir(ys[4], {1: "$6x$", 0: "$-1$"})
cikar(ys[5], {1: "$6x$", 0: "$-12$"}, 3.5, 6.1)
ax.add_patch(patches.FancyBboxPatch((4.95, ys[6] - 0.32), 1.1, 0.64, boxstyle="round,pad=0.05",
             fc=YESIL_ACIK, ec=YESIL, lw=1.3))
ax.text(5.5, ys[6], "$11$", ha="center", va="center", fontsize=FS, color=YESIL)

# bölme çizgileri, bölen ve bölüm
ax.plot([6.45, 6.45], [7.15, 5.25], color=YAZI, lw=1.6)
ax.plot([6.45, 9.6], [6.15, 6.15], color=YAZI, lw=1.6)
ax.text(8.05, ys[0], "$x-2$", ha="center", va="center", fontsize=FS)
ax.add_patch(patches.FancyBboxPatch((6.6, 5.38), 2.9, 0.64, boxstyle="round,pad=0.05",
             fc=MAVI_ACIK, ec=MAVI, lw=1.3))
ax.text(8.05, 5.7, "$2x^2+x+6$", ha="center", va="center", fontsize=FS, color=MAVI)

# adlar
ax.text(3.4, 7.35, "Bölünen", ha="center", va="center", fontsize=12, color=SOLUK)
ax.text(9.75, ys[0], "Bölen", ha="left", va="center", fontsize=12, color=SOLUK)
ax.text(8.05, 4.85, "Bölüm", ha="center", va="center", fontsize=12, color=MAVI)
ax.text(6.3, ys[6], "Kalan", ha="left", va="center", fontsize=12, color=YESIL)
ax.text(0.1, 0.15, "Kalanın derecesi (0), bölenin derecesinden (1) küçük: bölme biter.",
        ha="left", va="center", fontsize=11, color=SOLUK)
kaydet(fig, __file__)
