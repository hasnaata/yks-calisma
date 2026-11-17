import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 9: dengedeki terazi, 3x + 5 = x + 13 (x = 4).

def kutu(ax, x, y, s=0.62):
    ax.add_patch(patches.FancyBboxPatch((x, y), s, s, boxstyle="round,pad=0,rounding_size=0.06",
                                        fc=MAVI_ACIK, ec=MAVI, lw=1.8, zorder=4))
    ax.text(x + s / 2, y + s / 2, "x", ha="center", va="center", color=MAVI, fontsize=15, fontweight="bold", zorder=5)

def agirlik(ax, x, y, kg, en=1.3):
    ax.add_patch(patches.Polygon([(x, y), (x + en, y), (x + en - 0.12, y + 0.55), (x + 0.12, y + 0.55)],
                                 closed=True, fc=SARI_ACIK, ec=SARI, lw=1.8, zorder=4))
    ax.text(x + en / 2, y + 0.26, f"{kg} kg", ha="center", va="center", color=SARI, fontsize=11, fontweight="bold", zorder=5)

fig, ax = sekil(5.6, 2.8)
ax.set_xlim(-5.2, 5.2); ax.set_ylim(-0.6, 2.3); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([(-0.5, -0.4), (0.5, -0.4), (0, 1.9)], closed=True, fc=CIZGI, ec=SOLUK, lw=1.4))
ax.plot([-3.4, 3.4], [1.9, 1.9], color=SOLUK, lw=3, solid_capstyle="round")
for cx, yuk in ((-3.4, ["kutu", "kutu", "kutu", 5]), (3.4, ["kutu", 13])):
    ax.plot([cx, cx - 1.5], [1.9, 0.55], color=SOLUK, lw=1)
    ax.plot([cx, cx + 1.5], [1.9, 0.55], color=SOLUK, lw=1)
    ax.add_patch(patches.Polygon([(cx - 1.85, 0.55), (cx + 1.85, 0.55), (cx + 1.55, 0.3), (cx - 1.55, 0.3)],
                                 closed=True, fc="white", ec=SOLUK, lw=1.6, zorder=3))
    enler = [0.62 if o == "kutu" else 1.3 for o in yuk]
    toplam = sum(enler) + 0.06 * (len(yuk) - 1)
    px = cx - toplam / 2
    for o, e in zip(yuk, enler):
        kutu(ax, px, 0.56) if o == "kutu" else agirlik(ax, px, 0.56, o)
        px += e + 0.06
kaydet(fig, __file__)
