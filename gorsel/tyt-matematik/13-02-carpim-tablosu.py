import sys; sys.path.insert(0, "tools")
from cizim import *

# (2x − 3)(x² + 4x − 1) çarpımı tablo ile: her hücre bir satır ile bir sütunun çarpımı.
# Aynı dereceli hücreler aynı renkte: 2x³ + (8x² − 3x²) + (−2x − 12x) + 3 = 2x³ + 5x² − 14x + 3
fig, ax = sekil(6, 3.4)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.1, 8.6); ax.set_ylim(-0.1, 3.9)
renk = {3: (MAVI, MAVI_ACIK), 2: (YESIL, YESIL_ACIK), 1: (SARI, SARI_ACIK), 0: (KIRMIZI, KIRMIZI_ACIK)}
ust = ["$x^2$", "$+4x$", "$-1$"]
sol = ["$2x$", "$-3$"]
hucre = [[("$2x^3$", 3), ("$8x^2$", 2), ("$-2x$", 1)],
         [("$-3x^2$", 2), ("$-12x$", 1), ("$+3$", 0)]]
g, h = 2.2, 1.5
x0, y0 = 1.8, 0.0
for j, t in enumerate(ust):
    ax.text(x0 + j * g + g / 2, y0 + 2 * h + 0.45, t.replace("-", "−"), ha="center", va="center", fontsize=15, color=YAZI)
for i, t in enumerate(sol):
    ax.text(x0 - 0.45, y0 + (1 - i) * h + h / 2, t.replace("-", "−"), ha="right", va="center", fontsize=15, color=YAZI)
for i in range(2):
    for j in range(3):
        t, d = hucre[i][j]
        kenar, dolgu = renk[d]
        ax.add_patch(patches.Rectangle((x0 + j * g, y0 + (1 - i) * h), g, h, facecolor=dolgu, edgecolor=CIZGI, lw=1.5))
        ax.text(x0 + j * g + g / 2, y0 + (1 - i) * h + h / 2, t.replace("-", "−"), ha="center", va="center", fontsize=16, color=kenar)
ax.text(0.2, y0 + 2 * h + 0.45, "×", ha="left", va="center", fontsize=16, color=SOLUK)
kaydet(fig, __file__)
