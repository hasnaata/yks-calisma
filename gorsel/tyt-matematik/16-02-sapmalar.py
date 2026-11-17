import sys; sys.path.insert(0, "tools")
from cizim import *

# 3, 5, 9, 10, 13 verisi; ortalama 8. Her verinin ortalamadan farkı ok ile.
VERI = [3, 5, 9, 10, 13]
ORT = 8
fig, ax = sekil(6, 3.2)
sayi_dogrusu(ax, 2, 14)
ax.set_ylim(-0.7, 2.3)
ax.vlines(ORT, -0.05, 2.0, color=SARI, lw=2, ls="--")
ax.text(ORT, 2.1, "ortalama 8", ha="center", color=SARI, fontsize=12)
# Okların yükseklikleri: kısa farklar alçakta, uzunlar yüksekte, çakışmasın.
YUK = {3: 1.55, 5: 0.95, 9: 0.95, 10: 1.35, 13: 1.75}
for x in VERI:
    renk = KIRMIZI if x < ORT else YESIL
    ax.plot(x, 0, "o", color=MAVI, markersize=10, zorder=5)
    y = YUK[x]
    ax.annotate("", xy=(x, y), xytext=(ORT, y), arrowprops=dict(arrowstyle="->", color=renk, lw=1.8))
    ax.vlines(x, 0.12, y, color=CIZGI, lw=1, ls=":")
    fark = x - ORT
    etiket = (f"+{fark}" if fark > 0 else f"−{-fark}")
    ax.text((x + ORT) / 2, y + 0.1, etiket, ha="center", va="bottom", color=renk, fontsize=13)
kaydet(fig, __file__)
