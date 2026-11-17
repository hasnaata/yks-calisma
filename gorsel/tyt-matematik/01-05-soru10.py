import sys; sys.path.insert(0, "tools")
from cizim import *

# Kule: en üst katta 1 blok, her alt kat 2 blok fazla. İlk dört kat çizilir, altı noktalarla devam eder.
fig, ax = sekil(5, 3.2)
ax.axis("off"); ax.set_aspect("equal")
for kat, adet in enumerate([1, 3, 5, 7]):
    y = 3 - kat
    for i in range(adet):
        x = -adet / 2 + i
        ax.add_patch(patches.Rectangle((x, y), 1, 1, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))
    ax.text(4.3, y + 0.5, f"{kat + 1}. kat: {adet} blok", ha="left", va="center", fontsize=13, color=YAZI)
for x in (-1, 0, 1):
    ax.plot(x, -0.45, "o", color=SOLUK, markersize=4)
ax.set_xlim(-4.2, 9.6); ax.set_ylim(-0.9, 4.2)
kaydet(fig, __file__)
