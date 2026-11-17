import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: en küçük veri 10, en büyük veri 30, 4 grup. 20 / 4 = 5 tam çıkıyor.
# Genişlik 5 alınırsa 30 dışarıda kalır; 6 alınınca bütün veriler gruplara girer.
fig, ax = sekil(6, 3.4)
ax.set_xlim(8.2, 35.5); ax.set_ylim(-0.7, 3.5); ax.axis("off")
satirlar = ((2.3, 5, "Genişlik 5: yanlış", KIRMIZI), (0.4, 6, "Genişlik 6: doğru", YESIL))
for y, g, baslik, renk in satirlar:
    ax.annotate("", xy=(35.2, y), xytext=(8.5, y), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.2))
    for i in range(4):
        a, b = 10 + i * g, 10 + i * g + g - 1
        ax.add_patch(patches.Rectangle((a - 0.45, y - 0.2), b - a + 0.9, 0.4, facecolor=MAVI_ACIK if i % 2 == 0 else SARI_ACIK,
                                       edgecolor=MAVI if i % 2 == 0 else SARI, lw=1.2, zorder=2))
        ax.text((a + b) / 2, y + 0.3, f"{a}–{b}", ha="center", va="bottom", fontsize=11, color=YAZI)
    ax.text(8.5, y + 0.85, baslik, ha="left", va="bottom", fontsize=13, color=renk)
    for t, ad in ((10, "en küçük"), (30, "en büyük")):
        disarida = t > 10 + 4 * g - 1
        ax.plot(t, y, "o", color=KIRMIZI if disarida else YAZI, markersize=8, zorder=5)
        ax.text(t, y - 0.3, str(t), ha="center", va="top", fontsize=12, color=KIRMIZI if disarida else YAZI)
    if 30 > 10 + 4 * g - 1:
        ax.text(31, y - 0.3, "dışarıda kaldı", ha="left", va="top", fontsize=11, color=KIRMIZI)
kaydet(fig, __file__)
