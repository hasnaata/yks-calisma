import sys; sys.path.insert(0, "tools")
from cizim import *

# 40 kişilik sınıf: İngilizce 22, Almanca 15, ikisi 8 -> yalnız İ 14, ikisi 8, yalnız A 7, hiçbiri 11.
fig, ax = sekil(6.0, 4.0)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.2, 10.2); ax.set_ylim(-0.3, 6.6)
ax.add_patch(patches.Rectangle((0, 0), 10, 6.2, facecolor=SARI_ACIK, edgecolor=SARI, lw=2))
ax.add_patch(patches.Ellipse((3.9, 3.1), 4.8, 4.2, facecolor="white", edgecolor="none"))
ax.add_patch(patches.Ellipse((6.4, 3.1), 4.8, 4.2, facecolor="white", edgecolor="none"))
ax.add_patch(patches.Ellipse((3.9, 3.1), 4.8, 4.2, facecolor=MAVI_ACIK, edgecolor="none", alpha=0.8))
ax.add_patch(patches.Ellipse((6.4, 3.1), 4.8, 4.2, facecolor=YESIL_ACIK, edgecolor="none", alpha=0.7))
ax.add_patch(patches.Ellipse((3.9, 3.1), 4.8, 4.2, facecolor="none", edgecolor=MAVI, lw=2))
ax.add_patch(patches.Ellipse((6.4, 3.1), 4.8, 4.2, facecolor="none", edgecolor=YESIL, lw=2))
ax.text(9.6, 5.65, "E", fontsize=16, fontweight="bold", color=SARI, ha="center")
ax.text(1.75, 4.95, "İ", fontsize=16, fontweight="bold", color=MAVI, ha="center")
ax.text(8.55, 4.95, "A", fontsize=16, fontweight="bold", color=YESIL, ha="center")
for x, sayi, ad, renk in ((2.75, "14", "İ \\ A", MAVI), (5.15, "8", "İ ∩ A", YAZI), (7.55, "7", "A \\ İ", YESIL)):
    ax.text(x, 3.35, sayi, fontsize=22, fontweight="bold", ha="center", va="center", color=renk)
    ax.text(x, 2.45, ad, fontsize=12, ha="center", va="center", color=renk)
ax.text(8.9, 0.75, "11", fontsize=22, fontweight="bold", ha="center", va="center", color=SARI)
ax.text(7.35, 0.6, "(İ ∪ A)′", fontsize=12, ha="center", va="center", color=SARI)
kaydet(fig, __file__)
