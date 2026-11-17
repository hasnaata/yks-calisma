import sys; sys.path.insert(0, "tools")
from cizim import *

# f: A -> B, g: B -> C. A = {−1, 0, 2}, B = {1, 3, 4, 5}, C = {0, 2, 6}.
# f: −1->3, 0->1, 2->5.  g: 1->0, 3->6, 4->2, 5->2.  g∘f = {(−1, 6), (0, 0), (2, 2)}.
fig, ax = sekil(6.2, 3.4)
ax.axis("off"); ax.set_xlim(-0.3, 8.3); ax.set_ylim(-0.5, 4.6)
X = {"A": 0.9, "B": 4.0, "C": 7.1}
el = {"A": ["−1", "0", "2"], "B": ["1", "3", "4", "5"], "C": ["0", "2", "6"]}
def y(k, i): n = len(el[k]); return 2.0 + (n - 1) / 2 * 0.85 - i * 0.85
for k, x in X.items():
    ax.add_patch(patches.Ellipse((x, 2.0), 1.3, 4.0, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
    ax.text(x, 4.2, k, ha="center", fontsize=16, color=MAVI, fontweight="bold")
    for i, e in enumerate(el[k]):
        ax.text(x, y(k, i), e, ha="center", va="center", fontsize=14)
def ok(k1, e1, k2, e2, renk):
    ax.annotate("", xy=(X[k2] - 0.38, y(k2, el[k2].index(e2))), xytext=(X[k1] + 0.38, y(k1, el[k1].index(e1))),
                arrowprops=dict(arrowstyle="->", color=renk, lw=1.6, shrinkA=0, shrinkB=0))
for a, b in (("−1", "3"), ("0", "1"), ("2", "5")): ok("A", a, "B", b, YESIL)
for a, b in (("1", "0"), ("3", "6"), ("4", "2"), ("5", "2")): ok("B", a, "C", b, SARI)
ax.text(2.45, 4.2, "f", ha="center", fontsize=15, color=YESIL, fontweight="bold")
ax.text(5.55, 4.2, "g", ha="center", fontsize=15, color=SARI, fontweight="bold")
kaydet(fig, __file__)
