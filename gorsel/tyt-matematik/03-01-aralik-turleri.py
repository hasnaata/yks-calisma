import sys; sys.path.insert(0, "tools")
from cizim import *

# Dört aralık türü: aynı uç noktalar (−2 ve 3), farklı dahil olma durumları.
SATIRLAR = [
    ("[−2, 3]", "kapalı", True, True),
    ("(−2, 3)", "açık", False, False),
    ("[−2, 3)", "yarı açık", True, False),
    ("(−2, 3]", "yarı açık", False, True),
]
fig, eks = plt.subplots(len(SATIRLAR), 1, figsize=(6, 5.2))
for ax, (gosterim, ad, sol, sag) in zip(eks, SATIRLAR):
    sayi_dogrusu(ax, -3, 4)
    ax.hlines(0, -2, 3, color=MAVI, lw=5, zorder=3)
    for x, dolu in ((-2, sol), (3, sag)):
        ax.plot(x, 0, "o", color=MAVI, markerfacecolor=MAVI if dolu else "white", markersize=11, mew=2.2, zorder=5)
    ax.text(4.9, 0.12, gosterim, va="center", fontsize=15, color=YAZI)
    ax.text(4.9, -0.42, ad, va="center", fontsize=12, color=SOLUK)
    ax.set_xlim(-3.6, 7.3)
kaydet(fig, __file__)
