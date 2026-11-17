import sys; sys.path.insert(0, "tools")
from cizim import *

# 36 382 sayısının basamakları: rakam (sayı değeri) ve basamak değeri. İki 3 mavi.
BASLIK = ["On\nbinler", "Binler", "Yüzler", "Onlar", "Birler"]
RAKAM = [3, 6, 3, 8, 2]
DEGER = ["30 000", "6 000", "300", "80", "2"]
fig, ax = sekil(6, 3.0)
ax.axis("off"); ax.set_aspect("equal")
G, Y0 = 1.5, 0  # sütun genişliği
SOL = 2.3       # satır adları için yer
satirlar = [(1.2, "Basamak", BASLIK), (1.0, "Rakam\n(sayı değeri)", RAKAM), (1.0, "Basamak\ndeğeri", DEGER)]
y = 0
for i, (h, ad, icerik) in enumerate(satirlar):
    ax.text(SOL - 0.15, y - h / 2, ad, ha="right", va="center", fontsize=11, color=SOLUK)
    for j, v in enumerate(icerik):
        x = SOL + j * G
        vurgu = RAKAM[j] == 3 and i > 0
        ax.add_patch(patches.Rectangle((x, y - h), G, h, facecolor=MAVI_ACIK if vurgu else ("#f4f2ee" if i == 0 else "white"),
                                       edgecolor=CIZGI, lw=1.2))
        ax.text(x + G / 2, y - h / 2, str(v), ha="center", va="center",
                fontsize=11 if i == 0 else (18 if i == 1 else 12),
                color=MAVI if vurgu else YAZI, fontweight="bold" if (vurgu or i == 1) else "normal")
    y -= h
ax.set_xlim(0, SOL + 5 * G + 0.05); ax.set_ylim(y - 0.05, 0.05)
kaydet(fig, __file__)
