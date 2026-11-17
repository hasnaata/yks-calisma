import sys; sys.path.insert(0, "tools")
from cizim import *

# A = [−2, 5) ve tümleyeni ℝ \ A = (−∞, −2) ∪ [5, ∞): uçların durumu tersine döner.
LO, HI = -4, 7
OK = dict(arrowstyle="-|>,head_width=0.35,head_length=0.6", lw=3)
fig, eks = plt.subplots(2, 1, figsize=(6, 2.8))
ax = eks[0]
sayi_dogrusu(ax, LO, HI)
ax.hlines(0, -2, 5, color=MAVI, lw=5, zorder=3)
ax.plot(-2, 0, "o", color=MAVI, markerfacecolor=MAVI, markersize=11, mew=2.2, zorder=5)
ax.plot(5, 0, "o", color=MAVI, markerfacecolor="white", markersize=11, mew=2.2, zorder=5)
ax.text(-6.9, 0, "A", va="center", fontsize=15, color=MAVI, fontweight="bold")

ax = eks[1]
sayi_dogrusu(ax, LO, HI)
ax.hlines(0, LO - 0.2, -2, color=KIRMIZI, lw=5, zorder=3)
ax.hlines(0, 5, HI + 0.2, color=KIRMIZI, lw=5, zorder=3)
ax.annotate("", xy=(LO - 0.6, 0), xytext=(LO - 0.1, 0), arrowprops=dict(color=KIRMIZI, **OK), zorder=4)
ax.annotate("", xy=(HI + 0.6, 0), xytext=(HI + 0.1, 0), arrowprops=dict(color=KIRMIZI, **OK), zorder=4)
ax.plot(-2, 0, "o", color=KIRMIZI, markerfacecolor="white", markersize=11, mew=2.2, zorder=5)
ax.plot(5, 0, "o", color=KIRMIZI, markerfacecolor=KIRMIZI, markersize=11, mew=2.2, zorder=5)
ax.text(-6.9, 0, "ℝ \\ A", va="center", fontsize=15, color=KIRMIZI, fontweight="bold")
for ax in eks: ax.set_xlim(-7, 7.8)
kaydet(fig, __file__)
