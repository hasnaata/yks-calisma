import sys; sys.path.insert(0, "tools")
from cizim import *

# Üç madenî para: her atışta 2 dal, toplam 2 · 2 · 2 = 8 çıktı.
fig, ax = sekil(6, 6)
ax.axis("off")
x = [0, 1.7, 3.4, 5.1]
yaprak = [3.5 - i for i in range(8)]          # 8 çıktı yukarıdan aşağı
def dugum(px, py, harf):
    renk = MAVI if harf == "Y" else KIRMIZI
    ax.add_patch(patches.Circle((px, py), 0.3, facecolor="white", edgecolor=renk, lw=2, zorder=3))
    ax.text(px, py, harf, ha="center", va="center", color=renk, fontsize=14, fontweight="bold", zorder=4)
nokta(ax, 0, 0)
for i, h1 in enumerate("YT"):
    y1 = 2 - 4 * i
    ax.plot([0, x[1] - 0.3], [0, y1], color=CIZGI, lw=1.8, zorder=1); dugum(x[1], y1, h1)
    for j, h2 in enumerate("YT"):
        y2 = y1 + 1 - 2 * j
        ax.plot([x[1] + 0.3, x[2] - 0.3], [y1, y2], color=CIZGI, lw=1.8, zorder=1); dugum(x[2], y2, h2)
        for k, h3 in enumerate("YT"):
            y3 = y2 + 0.5 - k
            ax.plot([x[2] + 0.3, x[3] - 0.3], [y2, y3], color=CIZGI, lw=1.8, zorder=1); dugum(x[3], y3, h3)
            ax.text(6.3, y3, h1 + h2 + h3, ha="left", va="center", color=YAZI, fontsize=14, family="DejaVu Sans Mono")
for px, ad in zip(x[1:], ("1. para", "2. para", "3. para")):
    ax.text(px, 4.45, ad, ha="center", color=SOLUK, fontsize=12)
ax.text(6.75, 4.45, "Çıktı", ha="center", color=SOLUK, fontsize=12)
ax.text(3.6, -4.55, "2 · 2 · 2 = 8 çıktı", ha="center", color=MAVI, fontsize=14, fontweight="bold")
ax.set_xlim(-0.4, 7.6); ax.set_ylim(-5.0, 4.9); ax.set_aspect("equal")
kaydet(fig, __file__)
