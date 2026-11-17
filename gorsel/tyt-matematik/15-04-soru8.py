import sys; sys.path.insert(0, "tools")
from cizim import *

# Dik kenarlar x² − 6x + 7 = 0 denkleminin kökleri: 3 + √2 ≈ 4,414 ve 3 − √2 ≈ 1,586 (ölçekli)
a, b = 3 + 2**0.5, 3 - 2**0.5
A, B, C = (0, b), (0, 0), (a, 0)
fig, ax = sekil(5, 2.6)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
s = 0.25
ax.plot([s, s, 0], [0, s, s], color=YAZI, lw=1.2)
ax.text(-0.15, b + 0.1, "A", ha="right", fontsize=13); ax.text(-0.15, -0.15, "B", ha="right", va="top", fontsize=13)
ax.text(a + 0.15, -0.15, "C", ha="left", va="top", fontsize=13)
ax.text(-0.15, b / 2, "b", ha="right", va="center", fontsize=14)
ax.text(a / 2, -0.2, "a", ha="center", va="top", fontsize=14)
ax.text(a / 2 + 0.15, b / 2 + 0.2, "?", ha="left", va="bottom", fontsize=14, color=SARI)
ax.set_xlim(-0.7, a + 0.6); ax.set_ylim(-0.7, b + 0.5)
kaydet(fig, __file__)
