import sys; sys.path.insert(0, "tools")
from cizim import *

# Virgül kaydırma: 34,56 · 100 = 3456 (virgül 2 basamak sağa), 34,56 : 100 = 0,3456 (2 basamak sola).
# Soluk virgül eski yer, renkli virgül yeni yer; yaylar her basamak atlamasını gösterir.
fig, ax = sekil(6, 3.4)
ax.axis("off"); ax.set_aspect("equal")
G = 0.9

def satir(y, rakamlar, eski, yeni, renk, baslik, sonuc):
    ax.text(0, y + 1.05, baslik, fontsize=13, color=renk, fontweight="bold", va="center")
    for i, r in enumerate(rakamlar):
        ax.add_patch(patches.Rectangle((i * G + 0.04, y - 0.4), G - 0.08, 0.8, facecolor="white", edgecolor=CIZGI, lw=1))
        ax.text(i * G + G / 2, y, r, ha="center", va="center", fontsize=20,
                color=SOLUK if r == "0" else YAZI)
    ax.text(eski * G, y - 0.38, ",", ha="center", fontsize=28, color=CIZGI, fontweight="bold")
    ax.text(yeni * G, y - 0.38, ",", ha="center", fontsize=28, color=renk, fontweight="bold")
    adim = 1 if yeni > eski else -1
    for k in range(eski, yeni, adim):
        ax.annotate("", xy=((k + adim) * G, y - 0.5), xytext=(k * G, y - 0.5),
                    arrowprops=dict(arrowstyle="->", color=renk, lw=1.6,
                                    connectionstyle=f"arc3,rad={0.6 * adim}"))
    ax.text(len(rakamlar) * G + 0.3, y, sonuc, fontsize=15, color=renk, va="center")

satir(2.2, ["3", "4", "5", "6"], 2, 4, KIRMIZI, "34,56 · 100  →  virgül 2 basamak sağa", "= 3456")
satir(0.0, ["0", "3", "4", "5", "6"], 3, 1, YESIL, "34,56 : 100  →  virgül 2 basamak sola", "= 0,3456")
ax.set_xlim(-0.2, 6 * G + 2.4); ax.set_ylim(-1.2, 3.5)
kaydet(fig, __file__)
