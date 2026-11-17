import sys; sys.path.insert(0, "tools")
from cizim import *

# 48 kursiyer: kız 26, erkek 22; sabah kız 9, akşam kız 17, sabah erkek 9, akşam erkek 13.
# "Kız veya sabah grubunda" = tablodan yalnız akşam-erkek hücresi dışarıda kalır: 48 − 13 = 35.
fig, ax = sekil(5.6, 2.9)
ax.axis("off"); ax.set_xlim(0, 4); ax.set_ylim(0, 4); ax.invert_yaxis()
satirlar = ["", "Kız", "Erkek", "Toplam"]
sutunlar = ["", "Sabah", "Akşam", "Toplam"]
veri = {(1, 1): "9", (1, 2): "17", (1, 3): "26", (2, 1): "9", (2, 2): "13", (2, 3): "22",
        (3, 1): "18", (3, 2): "30", (3, 3): "48"}
for i in range(4):
    for j in range(4):
        renk = "white"
        if i == 0 or j == 0: renk = MAVI_ACIK
        if (i, j) in ((1, 1), (1, 2), (2, 1)): renk = YESIL_ACIK
        if (i, j) == (2, 2): renk = KIRMIZI_ACIK
        if i == 0 and j == 0: renk = "white"
        ax.add_patch(patches.Rectangle((j, i), 1, 1, facecolor=renk, edgecolor=CIZGI, lw=1.2))
        yazi = satirlar[i] if j == 0 else sutunlar[j] if i == 0 else veri[(i, j)]
        kalin = "bold" if (i == 0 or j == 0 or i == 3 or j == 3) else "normal"
        rk = KIRMIZI if (i, j) == (2, 2) else YAZI
        ax.text(j + 0.5, i + 0.5, yazi, ha="center", va="center", fontsize=14, fontweight=kalin, color=rk)
ax.plot([3, 3], [0, 4], color=SOLUK, lw=1.6); ax.plot([0, 4], [3, 3], color=SOLUK, lw=1.6)
kaydet(fig, __file__)
