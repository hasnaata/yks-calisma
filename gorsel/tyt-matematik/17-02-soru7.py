import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 7: en sevilen meyve. Elma 27, Muz 36, Çilek 12, Kiraz 15 (toplam 90).
ad = ["Elma", "Muz", "Çilek", "Kiraz"]; f = [27, 36, 12, 15]
fig, ax = sekil(5.4, 3.6)
ax.bar(ad, f, width=0.55, color=YESIL_ACIK, edgecolor=YESIL, lw=1.4, zorder=3)
ax.set_yticks(range(0, 40, 3)); ax.set_ylim(0, 39)
ax.tick_params(axis="y", labelsize=11)
ax.set_ylabel("Öğrenci sayısı")
for k in ("top", "right"): ax.spines[k].set_visible(False)
ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
kaydet(fig, __file__)
