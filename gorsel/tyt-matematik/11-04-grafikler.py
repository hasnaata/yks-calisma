import sys; sys.path.insert(0, "tools")
from cizim import *

# Sol: birim fonksiyon y = x, noktalar (2, 2) ve (−3, −3).
# Sağ: sabit fonksiyon y = 3, noktalar (−3, 3) ve (2, 3).
fig, eks = plt.subplots(1, 2, figsize=(6.5, 3.8))
x = np.linspace(-4.5, 4.5, 50)
for ax in eks:
    eksenler(ax, (-4.5, 4.5), (-4.5, 4.5))
    ax.set_xticks([-3, 2]); ax.set_xticklabels(["−3", "2"])
eks[0].set_yticks([2]); eks[0].set_yticklabels(["2"])
eks[1].set_yticks([3]); eks[1].set_yticklabels([""])

ax = eks[0]
ax.plot(x, x, color=MAVI)
nokta(ax, 2, 2, "(2, 2)", dx=0.3, dy=-0.7, renk=MAVI)
nokta(ax, -3, -3, "(−3, −3)", dx=0.35, dy=-0.25, renk=MAVI)
ax.text(1.0, 3.9, "y = x", color=MAVI, fontsize=12)
ax.text(0.5, -0.08, "Birim fonksiyon", transform=ax.transAxes, ha="center", va="top", color=MAVI, fontsize=13, fontweight="bold")

ax = eks[1]
ax.plot(x, 0 * x + 3, color=YESIL)
nokta(ax, -3, 3, "(−3, 3)", dx=-0.9, dy=0.35, renk=YESIL)
nokta(ax, 2, 3, "(2, 3)", dx=-0.4, dy=0.35, renk=YESIL)
ax.text(1.6, 2.2, "y = 3", color=YESIL, fontsize=12)
ax.text(0.5, -0.08, "Sabit fonksiyon", transform=ax.transAxes, ha="center", va="top", color=YESIL, fontsize=13, fontweight="bold")
fig.subplots_adjust(wspace=0.25)
kaydet(fig, __file__)
