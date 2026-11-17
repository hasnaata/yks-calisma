import sys; sys.path.insert(0, "tools")
from cizim import *

# Terazi modeli: 3x + 2 = x + 8. Her iki kefeden 1 kutu ve 2 kg çıkarılınca 2x = 6 kalır, x = 3.

def kutu(ax, x, y, s=0.62):
    ax.add_patch(patches.FancyBboxPatch((x, y), s, s, boxstyle="round,pad=0,rounding_size=0.06",
                                        fc=MAVI_ACIK, ec=MAVI, lw=1.8, zorder=4))
    ax.text(x + s / 2, y + s / 2, "x", ha="center", va="center", color=MAVI, fontsize=15, fontweight="bold", zorder=5)

def agirlik(ax, x, y, kg, en=1.2):
    ax.add_patch(patches.Polygon([(x, y), (x + en, y), (x + en - 0.12, y + 0.55), (x + 0.12, y + 0.55)],
                                 closed=True, fc=SARI_ACIK, ec=SARI, lw=1.8, zorder=4))
    ax.text(x + en / 2, y + 0.26, f"{kg} kg", ha="center", va="center", color=SARI, fontsize=11, fontweight="bold", zorder=5)

def terazi(ax, sol, sag, baslik):
    """sol, sag: ('kutu' | sayı) listeleri. Kefelere yan yana dizilir."""
    ax.set_xlim(-5.2, 5.2); ax.set_ylim(-0.6, 3.6); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(patches.Polygon([(-0.5, -0.4), (0.5, -0.4), (0, 1.9)], closed=True, fc=CIZGI, ec=SOLUK, lw=1.4))
    ax.plot([-3.4, 3.4], [1.9, 1.9], color=SOLUK, lw=3, solid_capstyle="round")
    for cx, yuk in ((-3.4, sol), (3.4, sag)):
        ax.plot([cx, cx - 1.5], [1.9, 0.55], color=SOLUK, lw=1)
        ax.plot([cx, cx + 1.5], [1.9, 0.55], color=SOLUK, lw=1)
        ax.add_patch(patches.Polygon([(cx - 1.85, 0.55), (cx + 1.85, 0.55), (cx + 1.55, 0.3), (cx - 1.55, 0.3)],
                                     closed=True, fc="white", ec=SOLUK, lw=1.6, zorder=3))
        enler = [0.62 if o == "kutu" else 1.2 for o in yuk]
        toplam = sum(enler) + 0.06 * (len(yuk) - 1)
        px = cx - toplam / 2
        for o, e in zip(yuk, enler):
            kutu(ax, px, 0.56) if o == "kutu" else agirlik(ax, px, 0.56, o)
            px += e + 0.06
    ax.text(0, 3.25, baslik, ha="center", va="center", fontsize=15, color=YAZI)

fig, eks = plt.subplots(2, 1, figsize=(5.6, 5.2))
terazi(eks[0], ["kutu", "kutu", "kutu", 2], ["kutu", 8], "3x + 2 = x + 8")
terazi(eks[1], ["kutu", "kutu"], [6], "2x = 6")
fig.text(0.5, 0.5, "iki kefeden de 1 kutu ve 2 kg çıkar", ha="center", va="center", fontsize=12, color=KIRMIZI)
fig.subplots_adjust(hspace=0.25)
kaydet(fig, __file__)
