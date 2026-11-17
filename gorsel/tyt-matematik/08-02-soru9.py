import sys; sys.path.insert(0, "tools")
from cizim import *

# Boyalı: A ∩ B ve (A ∪ B)′ ; boş: A \ B ve B \ A.
fig, ax = sekil(5.4, 3.4)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.2, 9.2); ax.set_ylim(-0.3, 5.6)
plt.rcParams["hatch.color"] = MAVI; plt.rcParams["hatch.linewidth"] = 0.8
ax.add_patch(patches.Rectangle((0, 0), 9, 5.2, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=1.8, hatch="/"))
sol = patches.Circle((3.5, 2.6), 1.9, facecolor="white", edgecolor="none"); ax.add_patch(sol)
sag = patches.Circle((5.5, 2.6), 1.9, facecolor="white", edgecolor="none"); ax.add_patch(sag)
kes = patches.Circle((5.5, 2.6), 1.9, facecolor=MAVI_ACIK, edgecolor="none", hatch="/"); ax.add_patch(kes)
kes.set_clip_path(patches.Circle((3.5, 2.6), 1.9, transform=ax.transData))
for m in ((3.5, 2.6), (5.5, 2.6)):
    ax.add_patch(patches.Circle(m, 1.9, facecolor="none", edgecolor=MAVI, lw=2))
ax.text(1.55, 4.15, "A", backgroundcolor="white", fontsize=16, fontweight="bold", color=MAVI, ha="center")
ax.text(7.45, 4.15, "B", backgroundcolor="white", fontsize=16, fontweight="bold", color=MAVI, ha="center")
ax.text(8.6, 4.62, "E", backgroundcolor="white", fontsize=16, fontweight="bold", color=YAZI, ha="center")
kaydet(fig, __file__)
