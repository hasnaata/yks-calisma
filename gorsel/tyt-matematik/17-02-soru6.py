import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 6: 6 denemedeki matematik neti. 15, 22, 20, 26, 26, 29.
x = [1, 2, 3, 4, 5, 6]; y = [15, 22, 20, 26, 26, 29]
fig, ax = sekil(5.6, 3.6)
ax.plot(x, y, color=MAVI, marker="o", markersize=7, zorder=3)
ax.set_xticks(x); ax.set_yticks(range(10, 33, 2)); ax.set_ylim(10, 32); ax.set_xlim(0.6, 6.4)
ax.tick_params(axis="y", labelsize=11)
ax.set_xlabel("Deneme"); ax.set_ylabel("Net")
for k in ("top", "right"): ax.spines[k].set_visible(False)
ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
kaydet(fig, __file__)
