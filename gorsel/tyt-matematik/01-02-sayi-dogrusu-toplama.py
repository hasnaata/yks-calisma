import sys; sys.path.insert(0, "tools")
from cizim import *

# İşaretleri farklı iki sayının toplamı sayı doğrusunda: pozitif sağa, negatif sola gider.
SATIRLAR = [
    ("−7 + 4 = −3", -7, 4, MAVI),
    ("3 + (−8) = −5", 3, -8, KIRMIZI),
]
fig, eks = plt.subplots(len(SATIRLAR), 1, figsize=(6, 3.6))
for ax, (yazi, bas, adim, renk) in zip(eks, SATIRLAR):
    sayi_dogrusu(ax, -8, 4)
    son = bas + adim
    ax.annotate("", xy=(son, 0.32), xytext=(bas, 0.32),
                arrowprops=dict(arrowstyle="-|>", color=renk, lw=2.4, mutation_scale=16))
    ax.plot(bas, 0, "o", color=YAZI, markersize=8, zorder=5)
    ax.plot(son, 0, "o", color=renk, markersize=10, zorder=5)
    ax.text((bas + son) / 2, 0.62, f"{abs(adim)} birim {'sağa' if adim > 0 else 'sola'}",
            ha="center", va="center", fontsize=12, color=renk)
    ax.text(-8.4, 0.95, yazi, ha="left", va="center", fontsize=14, color=YAZI)
    ax.set_ylim(-0.9, 1.15)
kaydet(fig, __file__)
