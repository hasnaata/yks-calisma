import sys; sys.path.insert(0, "tools")
from cizim import *

# 2x + y = 7 denkleminin çözümleri: her sıralı ikili bir nokta, hepsi aynı doğru üzerinde.
fig, ax = sekil(5.6, 5.4)
eksenler(ax, x=(-1.2, 5), y=(-2.4, 8.6))
ax.set_xticks(range(-1, 5)); ax.set_yticks(range(-2, 9))
ax.set_xticklabels(["−1", "", "1", "2", "3", "4"]); ax.set_yticklabels(["−2", "−1", "", "1", "2", "3", "4", "5", "6", "7", "8"])
xs = np.linspace(-0.6, 4.6, 20)
ax.plot(xs, 7 - 2 * xs, color=MAVI, lw=2.6)
ax.text(3.35, 2.4, "2x + y = 7", color=MAVI, fontsize=14, fontweight="bold")
for px, py in [(0, 7), (1, 5), (2, 3), (3, 1)]:
    nokta(ax, px, py, f"({px}, {py})", dx=0.2, dy=0.15, renk=YESIL)
nokta(ax, 2.5, 2, "(2,5; 2)", dx=-1.55, dy=-0.55, renk=SARI)
nokta(ax, 4, -1, "(4, −1)", dx=-1.1, dy=-0.7, renk=SARI)
kaydet(fig, __file__)
