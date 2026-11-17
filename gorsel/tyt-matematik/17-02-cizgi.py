import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: fidanın boyu haftalara göre. 0:4, 1:7, 2:9, 3:9, 4:14, 5:16 (cm).
x = [0, 1, 2, 3, 4, 5]; y = [4, 7, 9, 9, 14, 16]
fig, ax = sekil(5.6, 3.8)
ax.plot(x, y, color=MAVI, marker="o", markersize=7, zorder=3)
ax.plot([3, 4], [9, 14], color=KIRMIZI, lw=3, zorder=4)
ax.plot([2, 3], [9, 9], color=SARI, lw=3, zorder=4)
for xi, yi in zip(x, y):
    ax.text(xi - 0.12, yi + 0.6, str(yi), ha="center", va="bottom", fontsize=12)
ax.text(3.62, 10.6, "+5", color=KIRMIZI, fontsize=13, ha="left")
ax.text(2.5, 7.4, "değişim yok", color=SARI, fontsize=11, ha="center")
ax.set_xticks(x); ax.set_yticks(range(0, 19, 2)); ax.set_ylim(0, 18.5); ax.set_xlim(-0.4, 5.4)
ax.set_xlabel("Hafta"); ax.set_ylabel("Boy (cm)")
for k in ("top", "right"): ax.spines[k].set_visible(False)
ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
kaydet(fig, __file__)
