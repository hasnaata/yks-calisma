import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 8: bahçe dört dikdörtgene ayrılmış; alanlar x², 5x, 2x, 10. Ölçek x = 4 için doğru (genişlikler 4 ve 5, yükseklikler 4 ve 2).
x = 4
fig, ax = sekil(5.5, 4)
ax.axis("off"); ax.set_aspect("equal")
hucreler = [(0, 2, x, x, "$x^2$"), (x, 2, 5, x, "$5x$"), (0, 0, x, 2, "$2x$"), (x, 0, 5, 2, "$10$")]
for x0, y0, g, h, alan in hucreler:
    ax.add_patch(patches.Rectangle((x0, y0), g, h, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2.2))
    ax.text(x0 + g / 2, y0 + h / 2, alan, ha="center", va="center", fontsize=19, color=YAZI)
ax.text(x / 2, 2 + x + 0.3, "$x$", ha="center", va="bottom", fontsize=15, color=MAVI)
ax.text(-0.3, 2 + x / 2, "$x$", ha="right", va="center", fontsize=15, color=MAVI)
ax.set_xlim(-1.3, x + 5.4); ax.set_ylim(-0.5, x + 3.3)
kaydet(fig, __file__)
