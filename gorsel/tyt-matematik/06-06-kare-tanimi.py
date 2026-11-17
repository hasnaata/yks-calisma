import sys; sys.path.insert(0, "tools")
from cizim import *

# Kare tanımı: "dört kenarı eşit" tek başına eşkenar dörtgenleri de alır; "bir açısı dik" eklenince yalnız kareler kalır.
fig, ax = sekil(6, 4.3)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.FancyBboxPatch((0, 0), 10, 7.8, boxstyle="round,pad=0,rounding_size=0.3",
             facecolor="white", edgecolor=SOLUK, lw=1.4))
ax.text(0.3, 7.35, "Dörtgenler", fontsize=13, color=SOLUK, va="center")
ax.add_patch(patches.Circle((3.75, 3.3), 2.6, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.8, alpha=0.9))
ax.add_patch(patches.Circle((6.25, 3.3), 2.6, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.8, alpha=0.75))
# kesişim vurgusu
kes = patches.Circle((3.75, 3.3), 2.6, facecolor=YESIL_ACIK, edgecolor="none")
ax.add_patch(kes); kes.set_clip_path(patches.Circle((6.25, 3.3), 2.6, transform=ax.transData))
ax.add_patch(patches.Circle((3.75, 3.3), 2.6, facecolor="none", edgecolor=MAVI, lw=1.8))
ax.add_patch(patches.Circle((6.25, 3.3), 2.6, facecolor="none", edgecolor=SARI, lw=1.8))
ax.text(2.4, 6.15, "Dört kenarı eşit", ha="center", fontsize=12, color=MAVI, fontweight="bold")
ax.text(7.6, 6.15, "Dört açısı dik", ha="center", fontsize=12, color=SARI, fontweight="bold")
# eşkenar dörtgen simgesi
ax.add_patch(patches.Polygon([(2.3, 3.6), (2.85, 4.4), (2.3, 5.2), (1.75, 4.4)], closed=True, facecolor="white", edgecolor=MAVI, lw=1.6))
ax.text(2.3, 3.1, "eşkenar\ndörtgen", ha="center", va="top", fontsize=11, color=MAVI)
# dikdörtgen simgesi
ax.add_patch(patches.Rectangle((7.0, 3.95), 1.3, 0.8, facecolor="white", edgecolor=SARI, lw=1.6))
ax.text(7.65, 3.6, "dikdörtgen", ha="center", va="top", fontsize=11, color=SARI)
# kare simgesi
ax.add_patch(patches.Rectangle((4.6, 3.6), 0.8, 0.8, facecolor="white", edgecolor=YESIL, lw=1.8))
ax.text(5.0, 3.25, "kare", ha="center", va="top", fontsize=13, color=YESIL, fontweight="bold")
# yamuk simgesi (dışarıda)
ax.add_patch(patches.Polygon([(8.75, 0.35), (9.75, 0.35), (9.5, 0.95), (9.0, 0.95)], closed=True, facecolor="white", edgecolor=SOLUK, lw=1.4))
ax.text(9.25, 1.1, "yamuk", ha="center", fontsize=10, color=SOLUK)
ax.set_xlim(-0.1, 10.1); ax.set_ylim(-0.1, 7.9)
kaydet(fig, __file__)
