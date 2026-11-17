import sys; sys.path.insert(0, "tools")
from cizim import *

# √(x + 7) = x − 5 denklemi. Kare alınca y = −√(x + 7) dalı da işe karışır.
# Doğru üst dalı x = 9'da (y = 4), alt dalı x = 2'de (y = −3) keser: x = 2 yabancı köktür.
fig, ax = sekil(6, 4.6)
eksenler(ax, x=(-8.5, 12.5), y=(-6, 6.5), izgara=True)
xs = np.linspace(-7, 12, 500)
ax.plot(xs, np.sqrt(xs + 7), color=MAVI)
ax.plot(xs, -np.sqrt(xs + 7), color=KIRMIZI, ls="--", lw=1.8)
xd = np.linspace(-0.5, 12, 10)
ax.plot(xd, xd - 5, color=YESIL)
ax.plot(9, 4, "o", color=MAVI, markersize=9, zorder=5)
ax.plot(2, -3, "o", color=KIRMIZI, markerfacecolor="white", mew=2.2, markersize=9, zorder=5)
ax.text(8.2, 4.5, "x = 9  geçerli", color=MAVI, fontsize=12, ha="right", va="bottom")
ax.text(2.6, -3.3, "x = 2  yabancı kök", color=KIRMIZI, fontsize=12, ha="left", va="top")
ax.text(-7.6, 3.3, "$y=\\sqrt{x+7}$", color=MAVI, fontsize=13)
ax.text(-7.6, -4.6, "$y=-\\sqrt{x+7}$", color=KIRMIZI, fontsize=13)
ax.text(10.6, 6.0, "$y=x-5$", color=YESIL, fontsize=13, ha="right")
ax.set_xticks([-5, 2, 5, 9]); ax.set_xticklabels(["−5", "2", "5", "9"])
ax.set_yticks([-3, 4]); ax.set_yticklabels(["−3", "4"])
kaydet(fig, __file__)
