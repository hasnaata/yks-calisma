import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 1. f: A -> B, A = {1, 2, 3, 4}, B = {2, 5, 6, 8}. f: 1->5, 2->8, 3->2, 4->6.
# f⁻¹(2) = 3, f(2) = 8, toplam 11.
fig, ax = sekil(4.6, 3.6)
ax.axis("off"); ax.set_xlim(-0.3, 5.3); ax.set_ylim(-0.3, 4.8)
A, B = ["1", "2", "3", "4"], ["2", "5", "6", "8"]
def yk(i): return 3.3 - i * 0.85
for x, ad, el in ((0.8, "A", A), (4.2, "B", B)):
    ax.add_patch(patches.Ellipse((x, 2.05), 1.2, 4.1, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
    ax.text(x, 4.35, ad, ha="center", fontsize=16, color=MAVI, fontweight="bold")
    for i, e in enumerate(el): ax.text(x, yk(i), e, ha="center", va="center", fontsize=14)
for a, b in (("1", "5"), ("2", "8"), ("3", "2"), ("4", "6")):
    ax.annotate("", xy=(4.2 - 0.38, yk(B.index(b))), xytext=(0.8 + 0.38, yk(A.index(a))),
                arrowprops=dict(arrowstyle="->", color=YESIL, lw=1.6, shrinkA=0, shrinkB=0))
ax.text(2.5, 4.35, "f", ha="center", fontsize=16, color=YESIL, fontweight="bold")
kaydet(fig, __file__)
