import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 1: bir kırtasiyenin aylık defter satışı (yüz adet). Ocak 30, Şubat 34, Mart 38, Nisan 35, Mayıs 46, Haziran 50.
aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]; y = [30, 34, 38, 35, 46, 50]
x = range(6)
fig, ax = sekil(5.8, 3.6)
ax.plot(x, y, color=MAVI, marker="o", markersize=7, zorder=3)
ax.set_xticks(list(x)); ax.set_xticklabels(aylar, fontsize=11)
ax.set_yticks(range(28, 53, 2)); ax.set_ylim(28, 52); ax.set_xlim(-0.4, 5.4)
ax.set_ylabel("Satış (yüz adet)")
for k in ("top", "right"): ax.spines[k].set_visible(False)
ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
kaydet(fig, __file__)
