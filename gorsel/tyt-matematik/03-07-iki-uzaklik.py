import sys; sys.path.insert(0, "tools")
from cizim import *

# |x + 1| + |x − 2|: x'in −1'e ve 2'ye uzaklıkları toplamı.
# Üst: x = 0,5 (arada) toplam 3. Alt: x = 3,5 (dışarıda) toplam 4,5 + 1,5 = 6.
LO, HI = -2, 4
fig, eks = plt.subplots(2, 1, figsize=(6, 4.2))

def kemer(ax, a, b, yazi, renk, y):
    ax.annotate("", xy=(b, y), xytext=(a, y), arrowprops=dict(arrowstyle="<->", color=renk, lw=2))
    ax.plot([a, a], [0.08, y + 0.06], color=renk, lw=1); ax.plot([b, b], [0.08, y + 0.06], color=renk, lw=1)
    ax.text((a + b) / 2, y + 0.1, yazi, ha="center", va="bottom", color=renk, fontsize=12)

for ax, x, baslik in ((eks[0], 0.5, "x = 0,5 (arada): toplam 1,5 + 1,5 = 3"),
                      (eks[1], 3.5, "x = 3,5 (dışarıda): toplam 4,5 + 1,5 = 6")):
    sayi_dogrusu(ax, LO, HI); ax.set_ylim(-0.9, 1.95)
    ax.hlines(0, -1, 2, color=YESIL_ACIK, lw=9, zorder=2)
    for t in (-1, 2): ax.plot(t, 0, "o", color=YESIL, markersize=8, zorder=5)
    ax.plot(x, 0, "o", color=KIRMIZI, markersize=9, zorder=6)
    ax.text(x, -0.62, "x", ha="center", va="top", color=KIRMIZI, fontsize=13, fontweight="bold")
    kemer(ax, -1, x, str(x + 1).replace(".", ","), MAVI, 0.38)
    kemer(ax, min(x, 2), max(x, 2), str(abs(x - 2)).replace(".", ","), SARI, 0.95 if x > 2 else 0.38)
    ax.text(1, 1.55, baslik, ha="center", va="bottom", fontsize=12, color=YAZI)
fig.subplots_adjust(hspace=0.25)
kaydet(fig, __file__)
