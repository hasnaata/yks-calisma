import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 8: bahçe (x + 5) × (x + 2), köşede kenarı x olan kare havuz. Ölçek x = 6 (11 × 8, havuz 6 × 6).
x = 6
fig, ax = sekil(5.5, 4.2)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Rectangle((0, 0), x + 5, x + 2, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2.2))
ax.add_patch(patches.Rectangle((0, 0), x, x, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2.2))
ax.text(x / 2, x / 2, "Havuz", ha="center", va="center", fontsize=14, color=MAVI)
ax.text((x + 5 + x) / 2, (x + 2) / 2 + 1.2, "Çim", ha="center", va="center", fontsize=14, color=YESIL)
# ölçüler
ax.annotate("", xy=(x + 5, x + 2.8), xytext=(0, x + 2.8), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.3))
ax.text((x + 5) / 2, x + 3.1, "x + 5", ha="center", va="bottom", fontsize=14)
ax.annotate("", xy=(x + 5.8, x + 2), xytext=(x + 5.8, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.3))
ax.text(x + 6.1, (x + 2) / 2, "x + 2", ha="left", va="center", fontsize=14)
ax.annotate("", xy=(x, -0.8), xytext=(0, -0.8), arrowprops=dict(arrowstyle="<->", color=MAVI, lw=1.3))
ax.text(x / 2, -1.1, "x", ha="center", va="top", fontsize=14, color=MAVI)
ax.set_xlim(-0.5, x + 8.5); ax.set_ylim(-2.2, x + 4.3)
kaydet(fig, __file__)
