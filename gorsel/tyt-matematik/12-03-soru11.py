import sys; sys.path.insert(0, "tools")
from cizim import *

# A paketi: 300 + 20x (0 günde 300 TL, 10 günde 500 TL). B paketi: 45x (10 günde 450 TL).
# 45x < 300 + 20x ⇔ x < 12. Kesişim (12, 540) şeklin dışında kalır.
fig, ax = sekil(5.6, 4.2)
eksenler(ax, x=(0, 11.8), y=(0, 590))
ax.set_xticks(range(1, 11)); ax.set_xticklabels(["", "", "", "", "5", "", "", "", "", "10"])
ax.set_yticks([100, 200, 300, 400, 450, 500]); ax.set_yticklabels(["100", "200", "300", "400", "450", "500"])
ax.plot([0, 10], [300, 500], color=MAVI); ax.plot([0, 10], [0, 450], color=YESIL)
for yy in (450, 500): ax.plot([0, 10], [yy, yy], ":", color=SOLUK, lw=1.2)
ax.plot([10, 10], [0, 500], ":", color=SOLUK, lw=1.2)
nokta(ax, 0, 300, renk=MAVI); nokta(ax, 10, 500, renk=MAVI); nokta(ax, 0, 0, renk=YESIL); nokta(ax, 10, 450, renk=YESIL)
ax.text(3.2, 395, "A", color=MAVI, fontsize=14, fontweight="bold")
ax.text(4.6, 160, "B", color=YESIL, fontsize=14, fontweight="bold")
ax.text(11.8, 18, "gün", ha="right", fontsize=12, color=SOLUK)
ax.text(0.3, 568, "ücret (TL)", fontsize=12, color=SOLUK)
kaydet(fig, __file__)
