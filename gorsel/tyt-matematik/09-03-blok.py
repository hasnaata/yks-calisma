import sys; sys.path.insert(0, "tools")
from cizim import *

# Yan yana olma: A ile B tek blok. Dışarıda 4 nesne (4!), blok içinde 2 sıra (2!).
fig, ax = sekil(6, 3.4)
ax.axis("off"); ax.set_aspect("equal")
def kutu(x, y, w, yazi, dolgu, kenar, fs=18):
    ax.add_patch(patches.FancyBboxPatch((x, y), w, 1.0, boxstyle="round,pad=0.02,rounding_size=0.1",
                                        facecolor=dolgu, edgecolor=kenar, lw=1.6))
    ax.text(x + w / 2, y + 0.5, yazi, ha="center", va="center", fontsize=fs, color=kenar, fontweight="bold")
# blok
ax.add_patch(patches.FancyBboxPatch((-0.15, -0.15), 2.5, 1.3, boxstyle="round,pad=0.02,rounding_size=0.15",
                                    facecolor="none", edgecolor=SARI, lw=2.2, linestyle="--"))
kutu(0, 0, 1.0, "A", SARI_ACIK, SARI); kutu(1.2, 0, 1.0, "B", SARI_ACIK, SARI)
for i, h in enumerate("CDE"):
    kutu(2.8 + i * 1.3, 0, 1.0, h, MAVI_ACIK, MAVI)
ax.text(1.1, 1.45, "1 blok", ha="center", fontsize=13, color=SARI, fontweight="bold")
ax.text(1.1, -0.45, "içi: 2! = 2", ha="center", va="top", fontsize=13, color=SARI)
ax.text(4.6, 1.45, "+ 3 kişi", ha="center", fontsize=13, color=MAVI, fontweight="bold")
ax.text(4.6, -0.45, "4 nesne: 4! = 24", ha="center", va="top", fontsize=13, color=MAVI)
ax.text(2.7, -1.35, "24 · 2 = 48", ha="center", va="top", fontsize=17, color=YESIL, fontweight="bold")
ax.set_xlim(-0.3, 6.6); ax.set_ylim(-2.1, 2.0)
kaydet(fig, __file__)
