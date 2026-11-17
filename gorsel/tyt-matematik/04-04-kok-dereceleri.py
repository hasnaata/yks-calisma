import sys; sys.path.insert(0, "tools")
from cizim import *

# y = √x, ∛x, ⁴√x eğrileri x = 1'de kesişir.
# x > 1 iken derece küçüldükçe değer büyür; 0 < x < 1 iken sıra tersine döner.
fig, ax = sekil(6, 4.2)
eksenler(ax, x=(-0.15, 4.4), y=(-0.15, 2.4), izgara=False)
xs = np.linspace(0, 4.2, 600)
for k, renk, ad, yx in ((2, MAVI, "$\\sqrt{x}$", 2.05), (3, YESIL, "$\\sqrt[3]{x}$", 1.66), (4, SARI, "$\\sqrt[4]{x}$", 1.40)):
    ax.plot(xs, xs ** (1 / k), color=renk)
    ax.text(4.25, yx, ad, color=renk, fontsize=14, va="center")
ax.axvline(1, color=SOLUK, lw=1, ls=":")
ax.axvspan(0, 1, color=KIRMIZI_ACIK, alpha=0.6, zorder=0)
ax.plot(1, 1, "o", color=YAZI, markersize=7, zorder=5)
ax.text(1.08, 0.9, "(1, 1)", fontsize=12, va="top")
ax.text(0.5, 2.25, "0 < x < 1\nkök derecesi\nbüyük olan\nbüyük", ha="center", va="top", fontsize=10.5, color=KIRMIZI)
ax.text(2.6, 0.55, "x > 1: kök derecesi küçük olan büyük", ha="center", fontsize=11, color=YAZI)
ax.set_xticks([1, 2, 3, 4]); ax.set_xticklabels(["1", "2", "3", "4"])
ax.set_yticks([1, 2]); ax.set_yticklabels(["1", "2"])
kaydet(fig, __file__)
