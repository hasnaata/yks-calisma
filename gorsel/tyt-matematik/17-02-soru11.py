import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 11: kesik eksen. A 260, B 220, C 240; dikey eksen 200'den başlar.
ad = ["A", "B", "C"]; v = [260, 220, 240]; alt = 200
fig, ax = sekil(4.6, 3.6)
ax.bar(ad, [x - alt for x in v], bottom=alt, width=0.55, color=MAVI_ACIK, edgecolor=MAVI, lw=1.4, zorder=3)
ax.set_ylim(alt, 270); ax.set_yticks(range(200, 271, 10))
ax.tick_params(axis="y", labelsize=11)
ax.set_ylabel("Satış (adet)")
for k in ("top", "right"): ax.spines[k].set_visible(False)
ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
kaydet(fig, __file__)
