import sys; sys.path.insert(0, "tools")
from cizim import *

# Diziyi bir de tersten yaz: alt alta gelen her çiftin toplamı aynı (ilk + son).
fig, ax = sekil(6, 2.9)
ax.axis("off"); ax.set_aspect("equal")
ileri = [7, 11, 15, 19, 23]
geri = ileri[::-1]
w = 1.0
for i, (a, b) in enumerate(zip(ileri, geri)):
    x = i * 1.15
    for y, deger, dolgu, kenar in ((1.3, a, MAVI_ACIK, MAVI), (0.2, b, SARI_ACIK, SARI)):
        ax.add_patch(patches.Rectangle((x, y), w, 0.9, facecolor=dolgu, edgecolor=kenar, lw=1.4))
        ax.text(x + w / 2, y + 0.45, str(deger), ha="center", va="center", fontsize=15, color=YAZI)
    ax.text(x + w / 2, -0.25, "30", ha="center", va="top", fontsize=15, color=YESIL, fontweight="bold")
ax.plot([-0.05, 4 * 1.15 + w + 0.05], [0.05, 0.05], color=YESIL, lw=1.6)
ax.text(5.95, 1.75, "S", ha="left", va="center", fontsize=15, color=MAVI)
ax.text(5.95, 0.65, "S", ha="left", va="center", fontsize=15, color=SARI)
ax.text(5.95, -0.55, "2S = 5 · 30", ha="left", va="center", fontsize=14, color=YESIL)
ax.set_xlim(-0.2, 8.6); ax.set_ylim(-1.0, 2.35)
kaydet(fig, __file__)
