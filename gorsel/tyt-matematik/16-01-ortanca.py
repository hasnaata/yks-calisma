import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: sıralanmış 7 veri (ortanca 4. terim = 9) ve 8 veri (4. ve 5. terim, 9 ile 12; ortanca 10,5).
SATIRLAR = [
    ("n = 7 (tek)", [5, 7, 9, 9, 12, 15, 20], [3], "4. terim:  ortanca = 9"),
    ("n = 8 (çift)", [5, 7, 9, 9, 12, 15, 20, 30], [3, 4], "4. ve 5. terim:  (9 + 12) / 2 = 10,5"),
]
fig, ax = sekil(6, 3.3)
ax.axis("off"); ax.set_aspect("equal")
for r, (ad, veri, orta, aciklama) in enumerate(SATIRLAR):
    y = -r * 2.8
    ax.text(0, y + 0.95, ad, fontsize=13, color=SOLUK, va="bottom")
    for i, v in enumerate(veri):
        vurgu = i in orta
        ax.add_patch(patches.FancyBboxPatch((i * 1.05, y - 0.45), 0.9, 0.9, boxstyle="round,pad=0,rounding_size=0.12",
                     facecolor=MAVI_ACIK if vurgu else "white", edgecolor=MAVI if vurgu else CIZGI, lw=2 if vurgu else 1.2))
        ax.text(i * 1.05 + 0.45, y, str(v), ha="center", va="center", fontsize=14,
                color=MAVI if vurgu else YAZI, fontweight="bold" if vurgu else "normal")
    ax.text(0, y - 0.62, aciklama, fontsize=12.5, color=MAVI, va="top")
ax.set_xlim(-0.1, 8.5); ax.set_ylim(-4.1, 1.5)
kaydet(fig, __file__)
