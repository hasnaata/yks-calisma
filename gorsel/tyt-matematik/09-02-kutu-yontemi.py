import sys; sys.path.insert(0, "tools")
from cizim import *

# 4 farklı kitabın 4 yere dizilişi: her yer için kalan seçenek sayısı 4, 3, 2, 1.
fig, ax = sekil(6, 2.4)
ax.axis("off"); ax.set_aspect("equal")
G, H, ARA = 1.1, 1.1, 0.55
for i, v in enumerate([4, 3, 2, 1]):
    x = i * (G + ARA)
    ax.add_patch(patches.FancyBboxPatch((x, 0), G, H, boxstyle="round,pad=0,rounding_size=0.12",
                                        facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
    ax.text(x + G / 2, H / 2, str(v), ha="center", va="center", fontsize=22, color=MAVI, fontweight="bold")
    ax.text(x + G / 2, -0.25, f"{i + 1}. yer", ha="center", va="top", fontsize=12, color=SOLUK)
    if i < 3:
        ax.text(x + G + ARA / 2, H / 2, "·", ha="center", va="center", fontsize=26, color=YAZI)
son = 4 * (G + ARA) - ARA
ax.text(son + 0.25, H / 2, "= 4! = 24", ha="left", va="center", fontsize=17, color=YESIL, fontweight="bold")
ax.text(0, H + 0.3, "Her yere, öncekilerden kalan kitaplardan biri konur.", ha="left", va="bottom", fontsize=11.5, color=SOLUK)
ax.set_xlim(-0.1, son + 2.6); ax.set_ylim(-0.75, H + 0.75)
kaydet(fig, __file__)
