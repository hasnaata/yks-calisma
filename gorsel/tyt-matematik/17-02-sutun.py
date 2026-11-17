import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: kütüphaneden ödünç alınan kitaplar. Roman 40, 35, 50, 45; bilim 20, 30, 25, 35.
aylar = ["Ekim", "Kasım", "Aralık", "Ocak"]; roman = [40, 35, 50, 45]; bilim = [20, 30, 25, 35]
x = np.arange(4); w = 0.36
fig, ax = sekil(5.8, 3.8)
ax.bar(x - w / 2, roman, w, color=MAVI, edgecolor=MAVI, label="Roman", zorder=3)
ax.bar(x + w / 2, bilim, w, color=YESIL_ACIK, edgecolor=YESIL, lw=1.4, label="Bilim", zorder=3)
ax.set_xticks(x); ax.set_xticklabels(aylar); ax.set_yticks(range(0, 61, 10)); ax.set_ylim(0, 60)
ax.set_ylabel("Kitap sayısı")
ax.legend(loc="upper left", frameon=False, ncol=2, fontsize=12)
for k in ("top", "right"): ax.spines[k].set_visible(False)
ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
kaydet(fig, __file__)
