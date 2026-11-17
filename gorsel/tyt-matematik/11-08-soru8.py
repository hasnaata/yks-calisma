import sys; sys.path.insert(0, "tools")
from cizim import *

# Depodaki su (litre) - zaman (saat): (0, 10), (4, 50), (6, 50), (11, 0).
fig, ax = sekil(5.8, 3.8)
ax.set_xlim(-0.3, 12.4); ax.set_ylim(-3, 62)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
ax.grid(True, color=CIZGI, linewidth=0.6, alpha=0.7); ax.set_axisbelow(True)
ax.set_xticks(range(0, 12)); ax.set_xticklabels(["0", "", "", "", "4", "", "6", "", "", "", "", "11"])
ax.set_yticks(range(0, 61, 10)); ax.set_yticklabels(["", "10", "20", "30", "40", "50", ""])
ax.plot([0, 4, 6, 11], [10, 50, 50, 0], color=MAVI)
for xv, yv in [(0, 10), (4, 50), (6, 50), (11, 0)]: nokta(ax, xv, yv, renk=MAVI)
ax.text(12.3, 2, "Zaman\n(saat)", ha="right", va="bottom", fontsize=12, color=YAZI)
ax.text(0.3, 60, "Su miktarı (litre)", ha="left", va="center", fontsize=12, color=YAZI)
kaydet(fig, __file__)
