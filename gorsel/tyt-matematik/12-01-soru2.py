import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 2. f: 1->5, 2->4, 3->6.  g: 4->9, 5->7, 6->8.
fig, ax = sekil(6.2, 3.0)
ax.axis("off"); ax.set_xlim(-0.3, 8.3); ax.set_ylim(-0.2, 4.0)
X = {"A": 0.9, "B": 4.0, "C": 7.1}
el = {"A": ["1", "2", "3"], "B": ["4", "5", "6"], "C": ["7", "8", "9"]}
def y(k, i): return 1.7 + 0.85 - i * 0.85
for k, x in X.items():
    ax.add_patch(patches.Ellipse((x, 1.7), 1.3, 3.3, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
    ax.text(x, 3.55, k, ha="center", fontsize=16, color=MAVI, fontweight="bold")
    for i, e in enumerate(el[k]):
        ax.text(x, y(k, i), e, ha="center", va="center", fontsize=14)
def ok(k1, e1, k2, e2, renk):
    ax.annotate("", xy=(X[k2] - 0.38, y(k2, el[k2].index(e2))), xytext=(X[k1] + 0.38, y(k1, el[k1].index(e1))),
                arrowprops=dict(arrowstyle="->", color=renk, lw=1.6, shrinkA=0, shrinkB=0))
for a, b in (("1", "5"), ("2", "4"), ("3", "6")): ok("A", a, "B", b, YESIL)
for a, b in (("4", "9"), ("5", "7"), ("6", "8")): ok("B", a, "C", b, SARI)
ax.text(2.45, 3.55, "f", ha="center", fontsize=15, color=YESIL, fontweight="bold")
ax.text(5.55, 3.55, "g", ha="center", fontsize=15, color=SARI, fontweight="bold")
kaydet(fig, __file__)
