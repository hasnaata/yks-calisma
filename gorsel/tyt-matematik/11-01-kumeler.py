import sys; sys.path.insert(0, "tools")
from cizim import *

# f: A -> B, f(x) = x^2, A = {-1, 0, 1, 2}, B = {0, 1, 2, 3, 4}.
# Görüntüler: f(-1) = 1, f(0) = 0, f(1) = 1, f(2) = 4. f(A) = {0, 1, 4}; 2 ve 3 boşta.
fig, ax = sekil(6, 4.2)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.3, 7.4); ax.set_ylim(-0.9, 5.0)

ax.add_patch(patches.Ellipse((1, 2.1), 1.5, 4.2, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.8))
ax.add_patch(patches.Ellipse((4, 2.1), 1.7, 4.4, facecolor="white", edgecolor=SARI, lw=1.8))
ax.add_patch(patches.Ellipse((4, 2.75), 1.15, 2.6, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.8))
ax.text(1, 4.5, "A", ha="center", fontsize=16, color=MAVI, fontweight="bold")
ax.text(4, 4.6, "B", ha="center", fontsize=16, color=SARI, fontweight="bold")
ax.annotate("", xy=(3.6, 4.75), xytext=(1.4, 4.75),
            arrowprops=dict(arrowstyle="->", color=YAZI, lw=1.6, connectionstyle="arc3,rad=-0.25"))
ax.text(2.5, 4.55, "f", ha="center", fontsize=15, style="italic")

sol = {"−1": 3.3, "0": 2.5, "1": 1.7, "2": 0.9}
sag = {"0": 3.55, "1": 2.75, "4": 1.95, "2": 0.95, "3": 0.25}
for e, y in sol.items(): ax.text(1, y, e, ha="center", va="center", fontsize=15)
for e, y in sag.items(): ax.text(4, y, e, ha="center", va="center", fontsize=15,
                                 color=YAZI if e in "014" else SOLUK)
for s, t in (("−1", "1"), ("0", "0"), ("1", "1"), ("2", "4")):
    ax.annotate("", xy=(3.72, sag[t]), xytext=(1.3, sol[s]),
                arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.5, shrinkA=0, shrinkB=0))

ax.text(5.15, 3.4, "Görüntü\nkümesi\nf(A) = {0, 1, 4}", fontsize=12, color=YESIL, va="center")
ax.text(5.15, 0.6, "boşta kalan\n2 ve 3", fontsize=12, color=SOLUK, va="center")
ax.text(1, -0.55, "Tanım kümesi", ha="center", fontsize=13, color=MAVI)
ax.text(4, -0.55, "Değer kümesi", ha="center", fontsize=13, color=SARI)
kaydet(fig, __file__)
