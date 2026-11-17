import sys; sys.path.insert(0, "tools")
from cizim import *

# P(x) = 2x³ − 5x² + x + 4 için x = 1 ve x = −1 yazınca her terimin değeri.
# Çift dereceli terimler (x², x⁰) iki satırda aynı, tek dereceliler (x³, x) işaret değiştirir.
fig, ax = sekil(6, 3.3)
ax.set_xlim(0, 10); ax.set_ylim(-0.5, 3.9); ax.axis("off")
sut = [3.3, 4.85, 6.4, 7.95]
basl = [r"$2x^{3}$", r"$-5x^{2}$", r"$x$", r"$4$"]
cift = [False, True, False, True]
x1 = ["2", "−5", "1", "4"]
xm1 = ["−2", "−5", "−1", "4"]
for xs, c in zip(sut, cift):
    ax.add_patch(patches.FancyBboxPatch((xs - 0.65, 0.35), 1.3, 2.55, boxstyle="round,pad=0.04",
                 fc=YESIL_ACIK if c else KIRMIZI_ACIK, ec="none"))
for xs, b in zip(sut, basl):
    ax.text(xs, 3.4, b, ha="center", va="center", fontsize=17)
ax.text(0.2, 2.2, "x = 1", fontsize=14, va="center", color=YAZI)
ax.text(0.2, 1.0, "x = −1", fontsize=14, va="center", color=YAZI)
for xs, v1, v2, c in zip(sut, x1, xm1, cift):
    ax.text(xs, 2.2, v1, ha="center", va="center", fontsize=16)
    ax.text(xs, 1.0, v2, ha="center", va="center", fontsize=16, color=YESIL if c else KIRMIZI)
ax.text(9.0, 2.2, "= 2", fontsize=15, va="center", color=MAVI)
ax.text(9.0, 1.0, "= −4", fontsize=15, va="center", color=MAVI)
ax.text(0.6, -0.25, "■ tek derece: işaret değişir", fontsize=12, color=KIRMIZI, ha="left", va="center")
ax.text(6.5, -0.25, "■ çift derece: aynı", fontsize=12, color=YESIL, ha="left", va="center")
kaydet(fig, __file__)
