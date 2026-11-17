import sys; sys.path.insert(0, "tools")
from cizim import *

# Musluk havuzu 6 saatte doldurur (saatte 1/6), gider 9 saatte boşaltır (saatte 1/9).
# İkisi açıkken saatte 1/6 - 1/9 = 1/18 -> 18 saat.
fig, ax = sekil(6, 3.8)
eksenler(ax, x=(0, 20), y=(0, 1.2), izgara=False)
for t in list(ax.texts): t.remove()  # x, y harflerini kaldır; eksen adları aşağıda
ax.set_xticks([0, 3, 6, 9, 12, 15, 18]); ax.set_yticks([0, 1/3, 2/3, 1])
ax.set_yticklabels(["0", "1/3", "2/3", "dolu"])
for y in (1/3, 2/3, 1): ax.axhline(y, color=CIZGI, lw=0.6, zorder=0)
ax.plot([0, 6], [0, 1], color=MAVI)
ax.plot([0, 18], [0, 1], color=KIRMIZI)
nokta(ax, 6, 1, renk=MAVI); nokta(ax, 18, 1, renk=KIRMIZI)
ax.text(6.6, 1.08, "yalnız musluk: 6 saat", color=MAVI, fontsize=11, va="bottom")
ax.text(10.5, 0.42, "musluk + gider\nsaatte 1/6 − 1/9 = 1/18", color=KIRMIZI, fontsize=11, va="top")
ax.text(18, 1.08, "18 saat", color=KIRMIZI, fontsize=11, ha="center", va="bottom")
ax.text(20.3, 0, "saat", fontsize=11, color=SOLUK, va="center")
ax.text(0.3, 1.17, "havuzdaki su", fontsize=11, color=SOLUK)
kaydet(fig, __file__)
