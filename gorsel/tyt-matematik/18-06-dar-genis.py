import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders, kural 3: a = 6, c = 8. Üçgen eşitsizliği 2 < b < 14; B dik açıysa b = 10 (6² + 8² = 100).
fig, ax = sekil(6, 1.9)
sayi_dogrusu(ax, 2, 14, isaretler=[2, 6, 10, 14])
ax.set_ylim(-1, 1.3)
ax.plot([2, 10], [0, 0], color=MAVI, lw=6, solid_capstyle="butt")
ax.plot([10, 14], [0, 0], color=KIRMIZI, lw=6, solid_capstyle="butt")
for t in (2, 14): nokta(ax, t, 0, renk=SOLUK, dolu=False)
nokta(ax, 10, 0, renk=YESIL)
ax.text(6, 0.35, "B dar açı", ha="center", color=MAVI, fontsize=13, fontweight="bold")
ax.text(12, 0.35, "B geniş açı", ha="center", color=KIRMIZI, fontsize=13, fontweight="bold")
ax.text(10, 0.95, "B dik açı: b = 10", ha="center", color=YESIL, fontsize=12)
ax.plot([10, 10], [0.12, 0.8], color=YESIL, lw=1.2)
kaydet(fig, __file__)
