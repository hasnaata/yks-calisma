import sys; sys.path.insert(0, "tools")
from cizim import *

# {0,1,2,3,4,5} ile rakamları farklı üç basamaklı çift sayılar: birler 0 ise 5·4·1, birler 2 ya da 4 ise 4·4·2.
fig, ax = sekil(6, 3.9)
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
satir(3.0, [5, 4, 1], "1. durum: birler 0", 20, MAVI_ACIK, MAVI)
satir(0.4, [4, 4, 2], "2. durum: birler 2 ya da 4", 32, SARI_ACIK, SARI)
for i, ad in enumerate(["yüzler", "onlar", "birler"]):
    ax.text(i * 1.9 + 0.6, 0.05, ad, ha="center", va="top", fontsize=11, color=SOLUK)
ax.text(0, -0.85, "Toplam: 20 + 32 = 52", fontsize=15, color=YAZI, fontweight="bold")
ax.set_xlim(-0.1, 7.2); ax.set_ylim(-1.2, 4.6)
kaydet(fig, __file__)
