import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 5: iki şubenin satışı. A: 40, 55, 30, 45; B: 35, 50, 50, 60.
aylar = ["Ocak", "Şubat", "Mart", "Nisan"]; A = [40, 55, 30, 45]; B = [35, 50, 50, 60]
x = np.arange(4); w = 0.36
fig, ax = sekil(5.8, 3.8)
ax.bar(x - w / 2, A, w, color=MAVI, edgecolor=MAVI, label="A şubesi", zorder=3)
ax.bar(x + w / 2, B, w, color=SARI_ACIK, edgecolor=SARI, lw=1.4, label="B şubesi", zorder=3)
ax.set_xticks(x); ax.set_xticklabels(aylar); ax.set_yticks(range(0, 71, 5)); ax.set_ylim(0, 70)
ax.tick_params(axis="y", labelsize=10)
ax.set_ylabel("Satış (adet)")
ax.legend(loc="upper left", frameon=False, ncol=2, fontsize=12)
for k in ("top", "right"): ax.spines[k].set_visible(False)
ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
kaydet(fig, __file__)
