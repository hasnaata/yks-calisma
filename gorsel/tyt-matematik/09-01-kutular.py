import sys; sys.path.insert(0, "tools")
from cizim import *

# Kutu yöntemi: 3 öğrenci, 5 kulüp. Üstte tekrar serbest, altta her kulüpte en çok bir öğrenci.
fig, ax = sekil(6, 3.6)
ax.axis("off"); ax.set_aspect("equal")
def satir(y, sayilar, baslik, sonuc, dolgu, kenar):
    ax.text(0, y + 1.45, baslik, fontsize=13, color=kenar, fontweight="bold")
    for i, s in enumerate(sayilar):
        x = i * 1.9
        ax.add_patch(patches.FancyBboxPatch((x, y), 1.2, 1.0, boxstyle="round,pad=0.02,rounding_size=0.1",
                                            facecolor=dolgu, edgecolor=kenar, lw=1.6))
        ax.text(x + 0.6, y + 0.5, str(s), ha="center", va="center", fontsize=22, color=kenar, fontweight="bold")
        if i < 2: ax.text(x + 1.55, y + 0.5, "·", ha="center", va="center", fontsize=24, color=YAZI)
    ax.text(5.15, y + 0.5, f"= {sonuc}", va="center", fontsize=18, color=YAZI)
satir(2.6, [5, 5, 5], "Aynı kulübü seçebilirler", 125, MAVI_ACIK, MAVI)
satir(0, [5, 4, 3], "Her kulüpte en çok bir öğrenci", 60, YESIL_ACIK, YESIL)
for i in range(3):
    ax.text(i * 1.9 + 0.6, -0.35, f"{i + 1}. öğrenci", ha="center", va="top", fontsize=11, color=SOLUK)
ax.set_xlim(-0.1, 7.2); ax.set_ylim(-0.9, 4.2)
kaydet(fig, __file__)
