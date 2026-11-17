import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders: {a, b, c} kümesinin alt kümeleri. Her eleman için iki seçenek (al / alma): 2 · 2 · 2 = 8.
fig, ax = sekil(6.0, 4.6)
ax.axis("off"); ax.set_xlim(-0.3, 10.2); ax.set_ylim(-0.6, 9.2)
X = [0.3, 2.4, 4.5, 6.6]          # kök, a, b, c sütunları
yap = [7.5 - i for i in range(8)]  # yaprakların yüksekliği
def dugum_y(seviye, i):            # seviyedeki i. düğümün yüksekliği (yaprakların ortalaması)
    adim = 2 ** (3 - seviye)
    return sum(yap[i * adim:(i + 1) * adim]) / adim
for s, h in enumerate(["", "a?", "b?", "c?"]):
    if h: ax.text(X[s], 8.6, h, ha="center", fontsize=14, color=SOLUK, fontweight="bold")
ax.text(8.6, 8.6, "alt küme", ha="center", fontsize=14, color=SOLUK, fontweight="bold")
for s in range(3):
    for i in range(2 ** s):
        y0 = dugum_y(s, i)
        for k, (renk, isim) in enumerate([(YESIL, "var"), (KIRMIZI, "yok")]):
            y1 = dugum_y(s + 1, 2 * i + k)
            ax.plot([X[s], X[s + 1]], [y0, y1], color=renk, lw=1.8)
            if s == 0:
                ax.text((X[0] + X[1]) / 2 - 0.15, (y0 + y1) / 2 + (0.35 if k == 0 else -0.35), isim,
                        ha="center", va="center", fontsize=12, color=renk)
for s in range(4):
    for i in range(2 ** s):
        ax.plot(X[s], dugum_y(s, i), "o", color=SOLUK, markersize=5, zorder=5)
harfler = "abc"
for i in range(8):
    secim = [h for j, h in enumerate(harfler) if not (i >> (2 - j)) & 1]
    ax.text(7.3, yap[i], "{" + ", ".join(secim) + "}" if secim else "∅", va="center", fontsize=14,
            color=MAVI if secim else KIRMIZI)
ax.text(5.0, -0.4, "2 · 2 · 2 = 8 alt küme", ha="center", fontsize=14, color=YAZI, fontweight="bold")
kaydet(fig, __file__)
