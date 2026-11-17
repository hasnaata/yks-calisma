import sys; sys.path.insert(0, "tools")
from cizim import *

# f: A -> B, A = {1, 2, 3, 4}, B = {5, 6, 7, 8}. 1->6, 2->5, 3->8, 4->6. 7 boşta.
fig, ax = sekil(3.6, 3.9)
ax.axis("off"); ax.set_xlim(-0.2, 3.2); ax.set_ylim(-0.4, 5.0)
for x, ad in ((0.6, "A"), (2.4, "B")):
    ax.add_patch(patches.Ellipse((x, 2.2), 1.1, 3.9, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
    ax.text(x, 4.35, ad, ha="center", fontsize=15, color=MAVI, fontweight="bold")
ax.annotate("", xy=(2.0, 4.6), xytext=(1.0, 4.6),
            arrowprops=dict(arrowstyle="->", color=YAZI, lw=1.5, connectionstyle="arc3,rad=-0.3"))
ax.text(1.5, 4.5, "f", ha="center", fontsize=14, style="italic")
sol, sag = ["1", "2", "3", "4"], ["5", "6", "7", "8"]
def y(i): return 3.4 - i * 0.8
for i, e in enumerate(sol): ax.text(0.6, y(i), e, ha="center", va="center", fontsize=14)
for i, e in enumerate(sag): ax.text(2.4, y(i), e, ha="center", va="center", fontsize=14)
for s, t in (("1", "6"), ("2", "5"), ("3", "8"), ("4", "6")):
    ax.annotate("", xy=(2.13, y(sag.index(t))), xytext=(0.87, y(sol.index(s))),
                arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.6, shrinkA=0, shrinkB=0))
kaydet(fig, __file__)
