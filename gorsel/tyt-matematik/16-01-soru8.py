import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 8: 20 öğrencinin bir ayda izlediği film sayısı. 0:2, 1:7, 2:4, 3:4, 4:3.
x = [0, 1, 2, 3, 4]; f = [2, 7, 4, 4, 3]
fig, ax = sekil(5.4, 3.6)
ax.bar(x, f, width=0.6, color=MAVI_ACIK, edgecolor=MAVI, lw=1.4, zorder=3)
ax.set_xticks(x); ax.set_yticks(range(0, 9)); ax.set_ylim(0, 8.3)
ax.set_xlabel("İzlenen film sayısı"); ax.set_ylabel("Öğrenci sayısı")
for k in ("top", "right"): ax.spines[k].set_visible(False)
ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
kaydet(fig, __file__)
