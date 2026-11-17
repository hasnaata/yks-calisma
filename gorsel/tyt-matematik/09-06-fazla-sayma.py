import sys; sys.path.insert(0, "tools")
from cizim import *

# "Önce 1 erkek seç, sonra 8 kişiden 3" yöntemi: E1 E2 K1 K2 ekibi iki farklı yoldan bir kez daha sayılır.
fig, ax = sekil(6, 3.2)
ax.axis("off"); ax.set_aspect("equal")
satirlar = [("E$_1$", "E$_2$  K$_1$  K$_2$"), ("E$_2$", "E$_1$  K$_1$  K$_2$")]
for i, (ilk, kalan) in enumerate(satirlar):
    y = 1.2 - i * 1.5
    ax.add_patch(patches.FancyBboxPatch((0, y - 0.45), 1.3, 0.9, boxstyle="round,pad=0,rounding_size=0.12",
                                        facecolor=KIRMIZI_ACIK, edgecolor=KIRMIZI, lw=1.4))
    ax.text(0.65, y, ilk, ha="center", va="center", fontsize=15, color=KIRMIZI, fontweight="bold")
    ax.add_patch(patches.FancyBboxPatch((1.5, y - 0.45), 2.9, 0.9, boxstyle="round,pad=0,rounding_size=0.12",
                                        facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))
    ax.text(2.95, y, kalan, ha="center", va="center", fontsize=15, color=MAVI)
    ax.annotate("", xy=(5.4, 0.45), xytext=(4.55, y), arrowprops=dict(arrowstyle="-|>", color=SOLUK, lw=1.6))
ax.add_patch(patches.FancyBboxPatch((5.5, 0.0), 2.3, 0.9, boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.4))
ax.text(6.65, 0.45, "Aynı ekip", ha="center", va="center", fontsize=14, color=YESIL, fontweight="bold")
ax.text(0.65, 2.0, "Önce\nseçilen", ha="center", va="bottom", fontsize=12, color=KIRMIZI)
ax.text(2.95, 2.0, "Sonra seçilenler", ha="center", va="bottom", fontsize=12, color=MAVI)
ax.set_xlim(-0.1, 7.9); ax.set_ylim(-0.9, 2.9)
kaydet(fig, __file__)
