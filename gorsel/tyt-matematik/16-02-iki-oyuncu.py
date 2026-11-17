import sys; sys.path.insert(0, "tools")
from cizim import *

# İki oyuncunun 5 maçtaki sayıları: ortalamalar aynı (16), yayılım farklı.
KAAN = [14, 15, 16, 17, 18]
MERT = [4, 10, 16, 22, 28]
fig, ax = sekil(6, 3.3)
ax.set_xlim(-1, 33); ax.set_ylim(-0.9, 3.1); ax.axis("off")
for y, ad, veri, renk, acik in ((2.1, "Kaan", KAAN, MAVI, MAVI_ACIK), (0.6, "Mert", MERT, KIRMIZI, KIRMIZI_ACIK)):
    ax.hlines(y, 0, 30, color=CIZGI, lw=1.2)
    for t in range(0, 31, 2):
        ax.plot([t, t], [y - 0.06, y + 0.06], color=CIZGI, lw=1)
    ax.add_patch(patches.FancyBboxPatch((min(veri), y - 0.17), max(veri) - min(veri), 0.34,
                 boxstyle="round,pad=0.05", facecolor=acik, edgecolor="none", zorder=2))
    ax.plot(veri, [y] * len(veri), "o", color=renk, markersize=10, zorder=4)
    ax.text(-0.6, y + 0.42, ad, fontsize=14, color=renk, ha="left")
    ax.text(31, y, f"açıklık\n{max(veri) - min(veri)}", fontsize=12, color=renk, va="center", ha="left")
ax.vlines(16, 0.25, 2.55, color=SARI, lw=2, ls="--", zorder=3)
ax.text(16, 2.75, "ortalama 16", ha="center", color=SARI, fontsize=12)
for t in (0, 4, 10, 16, 22, 28):
    ax.text(t, 0.15, str(t), ha="center", va="top", color=SOLUK, fontsize=11)
kaydet(fig, __file__)
