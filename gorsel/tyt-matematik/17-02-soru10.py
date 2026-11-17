import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 10: iki fidanın boyu. A: 10, 13, 15, 17, 18, 19; B: 4, 8, 13, 18, 22, 26.
x = [0, 1, 2, 3, 4, 5]; A = [10, 13, 15, 17, 18, 19]; B = [4, 8, 13, 18, 22, 26]
fig, ax = sekil(5.6, 3.8)
ax.plot(x, A, color=MAVI, marker="o", markersize=6, label="A fidanı", zorder=3)
ax.plot(x, B, color=KIRMIZI, marker="s", markersize=6, ls="--", label="B fidanı", zorder=3)
ax.set_xticks(x); ax.set_yticks(range(0, 29, 2)); ax.set_ylim(0, 28); ax.set_xlim(-0.3, 5.3)
ax.tick_params(axis="y", labelsize=10)
ax.set_xlabel("Hafta"); ax.set_ylabel("Boy (cm)")
ax.legend(loc="upper left", frameon=False, fontsize=12)
for k in ("top", "right"): ax.spines[k].set_visible(False)
ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
kaydet(fig, __file__)
