import sys; sys.path.insert(0, "tools")
from cizim import *

# Ayşe t = 0'da 12 km/sa ile çıkar: konum 12t. Burak t = 1'de aynı yerden 20 km/sa ile çıkar: konum 20(t - 1).
# Grafik yalnızca ilk 2 saati gösterir. 12t = 20(t - 1) -> t = 2,5; Burak yola çıktıktan 1,5 saat sonra yetişir.
fig, ax = sekil(5.6, 3.9)
eksenler(ax, x=(0, 2.6), y=(0, 30), izgara=False)
for t in list(ax.texts): t.remove()
ax.set_xticks([0, 0.5, 1, 1.5, 2]); ax.set_xticklabels(["0", "0,5", "1", "1,5", "2"])
ax.set_yticks([0, 4, 8, 12, 16, 20, 24, 28])
for y in range(4, 29, 4): ax.axhline(y, color=CIZGI, lw=0.6, zorder=0)
for x in (0.5, 1, 1.5, 2): ax.axvline(x, color=CIZGI, lw=0.6, zorder=0)
ax.plot([0, 2], [0, 24], color=MAVI)
ax.plot([1, 2], [0, 20], color=SARI)
nokta(ax, 2, 24, renk=MAVI); nokta(ax, 2, 20, renk=SARI)
ax.text(0.85, 13.2, "Ayşe", color=MAVI, fontsize=12, ha="right")
ax.text(1.62, 6.5, "Burak", color=SARI, fontsize=12)
ax.text(2.7, 0, "saat", fontsize=11, color=SOLUK, va="center")
ax.text(0.05, 29.3, "başlangıç noktasına uzaklık (km)", fontsize=11, color=SOLUK)
ax.set_ylim(0, 31)
kaydet(fig, __file__)
