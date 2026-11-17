import sys; sys.path.insert(0, "tools")
from cizim import *

# f: A -> R, A = {1, 2, 3, 4}: f(1) = 3, f(2) = 5, f(3) = 0, f(4) = 2
# g: B -> R, B = {2, 3, 4, 5}: g(2) = 4, g(3) = 2, g(4) = 0, g(5) = 6
# A ∩ B = {2, 3, 4}. f/g için 4 atılır (g(4) = 0), g/f için 3 atılır (f(3) = 0).
fig, ax = sekil(6, 3.6)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.4, 8.4); ax.set_ylim(-1.3, 3.9)

ax.add_patch(patches.Ellipse((2.8, 1.5), 4.4, 3.0, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.8, alpha=0.9))
ax.add_patch(patches.Ellipse((5.2, 1.5), 4.4, 3.0, facecolor="none", edgecolor=YESIL, lw=1.8))
# kesişim bölgesini vurgula: B'nin dolgusu A'nın içine kırpılır
alan = patches.Ellipse((5.2, 1.5), 4.4, 3.0, facecolor=YESIL_ACIK, edgecolor="none")
ax.add_patch(alan); alan.set_clip_path(patches.Ellipse((2.8, 1.5), 4.4, 3.0, transform=ax.transData))
ax.add_patch(patches.Ellipse((2.8, 1.5), 4.4, 3.0, facecolor="none", edgecolor=MAVI, lw=1.8))
ax.add_patch(patches.Ellipse((5.2, 1.5), 4.4, 3.0, facecolor="none", edgecolor=YESIL, lw=1.8))

ax.text(1.0, 3.25, "A", fontsize=16, color=MAVI, fontweight="bold")
ax.text(6.9, 3.25, "B", fontsize=16, color=YESIL, fontweight="bold")
ax.text(1.75, 1.5, "1", ha="center", va="center", fontsize=16)
ax.text(6.25, 1.5, "5", ha="center", va="center", fontsize=16)
for e, y in (("2", 2.35), ("3", 1.5), ("4", 0.65)):
    ax.text(4.0, y, e, ha="center", va="center", fontsize=16, fontweight="bold")
ax.add_patch(patches.Circle((4.0, 0.65), 0.28, facecolor="none", edgecolor=KIRMIZI, lw=1.8))
ax.text(4.0, -0.55, "A ∩ B = {2, 3, 4}", ha="center", fontsize=13, color=YESIL)
ax.text(4.0, -1.1, "f/g için 4 atılır, çünkü g(4) = 0", ha="center", fontsize=12, color=KIRMIZI)
kaydet(fig, __file__)
