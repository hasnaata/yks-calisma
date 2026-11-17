import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 2: f: A -> B, A = {1, 2, 3, 4}, B = {2, 5, 7, 9, 11}.
# f(1) = 5, f(2) = 7, f(3) = 5, f(4) = 9. f(A) = {5, 7, 9}, 3 eleman.
fig, ax = sekil(4.4, 3.8)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.2, 4.8); ax.set_ylim(-0.4, 5.0)
ax.add_patch(patches.Ellipse((1, 2.1), 1.3, 4.2, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.8))
ax.add_patch(patches.Ellipse((3.6, 2.1), 1.3, 4.4, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.8))
ax.text(1, 4.45, "A", ha="center", fontsize=16, color=MAVI, fontweight="bold")
ax.text(3.6, 4.55, "B", ha="center", fontsize=16, color=MAVI, fontweight="bold")
ax.annotate("", xy=(3.2, 4.7), xytext=(1.4, 4.7),
            arrowprops=dict(arrowstyle="->", color=YAZI, lw=1.6, connectionstyle="arc3,rad=-0.25"))
ax.text(2.3, 4.5, "f", ha="center", fontsize=15, style="italic")
sol = {"1": 3.3, "2": 2.5, "3": 1.7, "4": 0.9}
sag = {"2": 3.7, "5": 2.9, "7": 2.1, "9": 1.3, "11": 0.5}
for e, y in sol.items(): ax.text(1, y, e, ha="center", va="center", fontsize=15)
for e, y in sag.items(): ax.text(3.6, y, e, ha="center", va="center", fontsize=15)
for s, t in (("1", "5"), ("2", "7"), ("3", "5"), ("4", "9")):
    ax.annotate("", xy=(3.3, sag[t]), xytext=(1.25, sol[s]),
                arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.5, shrinkA=0, shrinkB=0))
kaydet(fig, __file__)
