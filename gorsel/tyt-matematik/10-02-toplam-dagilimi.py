import sys; sys.path.insert(0, "tools")
from cizim import *

# İki zar: her toplamı veren çıktı sayısı. 36 çıktı eş olasıdır, 11 toplam değildir.
toplamlar = list(range(2, 13))
sayilar = [6 - abs(t - 7) for t in toplamlar]
fig, ax = sekil(6.2, 3.6)
renkler = [YESIL if t == 7 else MAVI for t in toplamlar]
ax.bar(toplamlar, sayilar, color=[YESIL_ACIK if t == 7 else MAVI_ACIK for t in toplamlar],
       edgecolor=renkler, lw=1.6, width=0.75)
for t, s in zip(toplamlar, sayilar):
    ax.text(t, s + 0.12, str(s), ha="center", va="bottom", fontsize=13,
            color=YESIL if t == 7 else YAZI, fontweight="bold" if t == 7 else "normal")
ax.set_xticks(toplamlar); ax.set_yticks([])
for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
ax.set_ylim(0, 7.2)
ax.set_xlabel("İki zarın toplamı")
ax.set_title("Toplamı veren çıktı sayısı (toplam 36)", fontsize=13, color=SOLUK)
kaydet(fig, __file__)
