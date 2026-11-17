import sys; sys.path.insert(0, "tools")
from cizim import *

# A aracı: 48 L, 600 km'de biter (8 L / 100 km). B aracı: 36 L, 900 km'de biter (4 L / 100 km).
# Eşitlik: 48 − 0,08d = 36 − 0,04d ⇒ d = 300, yakıt 24 L. Kesişim noktası şekilde işaretlenmez.
fig, ax = sekil(5.8, 4.0)
eksenler(ax, x=(0, 1020), y=(0, 56))
ax.set_xticks([300, 600, 900]); ax.set_xticklabels(["300", "600", "900"])
ax.set_yticks([12, 24, 36, 48]); ax.set_yticklabels(["", "", "36", "48"])
ax.plot([0, 600], [48, 0], color=MAVI); ax.plot([0, 900], [36, 0], color=YESIL)
nokta(ax, 0, 48, renk=MAVI); nokta(ax, 600, 0, renk=MAVI); nokta(ax, 0, 36, renk=YESIL); nokta(ax, 900, 0, renk=YESIL)
ax.text(120, 44, "A", color=MAVI, fontsize=14, fontweight="bold")
ax.text(700, 12, "B", color=YESIL, fontsize=14, fontweight="bold")
ax.text(1020, 2.5, "yol (km)", ha="right", fontsize=12, color=SOLUK)
ax.text(18, 53, "yakıt (L)", fontsize=12, color=SOLUK)
kaydet(fig, __file__)
