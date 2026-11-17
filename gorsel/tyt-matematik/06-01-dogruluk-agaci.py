import sys; sys.path.insert(0, "tools")
from cizim import *

# p, q, r için doğruluk durumu ağacı: her önerme dalı ikiye ayırır, 2·2·2 = 8 satır.
fig, ax = sekil(6, 4.6)
ax.axis("off")
X = [0, 1.6, 3.2, 4.8]          # kök, p, q, r sütunları
SATIR_X = 6.6                    # satır yazıları
yapr = [7 - i for i in range(8)]  # 8 yaprağın y'si

def agac(sev, y_list, yol, px, py):
    if sev == 3:
        y = y_list[0]
        ax.plot([px + 0.25, SATIR_X - 0.75], [py, y], color=CIZGI, lw=0.8, ls=":")
        ax.text(SATIR_X, y, "  ".join(map(str, yol)), ha="center", va="center", fontsize=13,
                family="DejaVu Sans Mono", color=YAZI)
        return
    yarim = len(y_list) // 2
    for deger, grup in ((1, y_list[:yarim]), (0, y_list[yarim:])):
        yc = sum(grup) / len(grup)
        x = X[sev + 1]
        ax.plot([px + 0.22, x - 0.22], [py, yc], color=SOLUK, lw=1.2)
        renk = YESIL if deger == 1 else KIRMIZI
        ax.plot(x, yc, "o", markersize=19, markerfacecolor=YESIL_ACIK if deger else KIRMIZI_ACIK,
                markeredgecolor=renk, markeredgewidth=1.4, zorder=4)
        ax.text(x, yc, str(deger), ha="center", va="center", color=renk, fontsize=12, zorder=5, fontweight="bold")
        agac(sev + 1, grup, yol + [deger], x, yc)

ax.plot(X[0], 3.5, "o", color=MAVI, markersize=8)
agac(0, yapr, [], X[0], 3.5)
for x, ad in zip(X[1:], ["p", "q", "r"]):
    ax.text(x, 8.0, ad, ha="center", va="center", color=MAVI, fontsize=15, fontweight="bold")
ax.text(SATIR_X, 8.0, "p  q  r", ha="center", va="center", color=MAVI, fontsize=13,
        family="DejaVu Sans Mono", fontweight="bold")
ax.text(3.3, -0.9, "2 · 2 · 2 = 8 satır", ha="center", va="center", color=MAVI, fontsize=14)
ax.set_xlim(-0.3, 7.6); ax.set_ylim(-1.3, 8.4)
kaydet(fig, __file__)
