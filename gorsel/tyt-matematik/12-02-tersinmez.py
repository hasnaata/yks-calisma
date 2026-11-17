import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = x², A = {−2, 2, 3} -> B = {4, 9}. −2 ve 2 aynı görüntüye (4) gidiyor: f bire bir değil, tersi fonksiyon olamaz.
fig, ax = sekil(5.2, 3.2)
ax.axis("off"); ax.set_xlim(-0.3, 6.6); ax.set_ylim(-0.7, 4.6)
def kume(x, ad, el, ys):
    ax.add_patch(patches.Ellipse((x, 2.0), 1.2, 3.6, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
    ax.text(x, 4.1, ad, ha="center", fontsize=16, color=MAVI, fontweight="bold")
    for e, yy in zip(el, ys): ax.text(x, yy, e, ha="center", va="center", fontsize=14)
ya = [2.85, 2.0, 1.15]; yb = [2.45, 1.15]
kume(0.9, "A", ["−2", "2", "3"], ya); kume(5.1, "B", ["4", "9"], yb)
def ok(y1, y2, renk):
    ax.annotate("", xy=(5.1 - 0.38, y2), xytext=(0.9 + 0.38, y1),
                arrowprops=dict(arrowstyle="->", color=renk, lw=1.7, shrinkA=0, shrinkB=0))
ok(ya[0], yb[0], KIRMIZI); ok(ya[1], yb[0], KIRMIZI); ok(ya[2], yb[1], YESIL)
ax.text(3.0, 4.1, "f(x) = x²", ha="center", fontsize=14, color=YAZI)
ax.text(3.0, -0.45, "f⁻¹(4) = −2 mi, 2 mi?", ha="center", fontsize=13, color=KIRMIZI)
kaydet(fig, __file__)
