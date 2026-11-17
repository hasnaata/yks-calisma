import sys; sys.path.insert(0, "tools")
from cizim import *

# x ≥ 0 için verilen parça: (0, 0) → (2, 3) → (4, 1). Solda çift, sağda tek tamamlanıyor.
fig, eks = plt.subplots(1, 2, figsize=(6.5, 3.6))
px, py = [0, 2, 4], [0, 3, 1]
for ax, isaret, baslik in ((eks[0], 1, "f çift ise"), (eks[1], -1, "f tek ise")):
    eksenler(ax, (-4.8, 4.8), (-3.8, 3.8))
    ax.set_xticks([-4, -2, 2, 4]); ax.set_xticklabels(["−4", "−2", "2", "4"], fontsize=11)
    ax.set_yticks([-3, -1, 1, 3]); ax.set_yticklabels(["−3", "", "", "3"], fontsize=11)
    ax.plot(px, py, color=MAVI)
    ax.plot([-v for v in px], [isaret * v for v in py], "--", color=YESIL)
    nokta(ax, 2, 3, "", renk=MAVI)
    nokta(ax, -2, isaret * 3, "", renk=YESIL)
    ax.text(0.5, -0.1, baslik, transform=ax.transAxes, ha="center", va="top", fontsize=13, fontweight="bold",
            color=YESIL)
fig.subplots_adjust(wspace=0.3)
kaydet(fig, __file__)
