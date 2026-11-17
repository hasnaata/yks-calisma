import sys; sys.path.insert(0, "tools")
from cizim import *
from matplotlib.path import Path

# Solda A ∩ B (yalnız ortak bölge boyalı), sağda A ∪ B (iki daire de boyalı).
fig, axs = plt.subplots(1, 2, figsize=(6.2, 2.9))
for ax, baslik, alt, birlesim in ((axs[0], "A ∩ B", "ikisinde de (ve)", False), (axs[1], "A ∪ B", "en az birinde (veya)", True)):
    ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 6); ax.set_ylim(-0.6, 4.6)
    sol = patches.Circle((2.25, 2.0), 1.5); sag = patches.Circle((3.75, 2.0), 1.5)
    if birlesim:
        for c in (sol, sag): c.set_facecolor(MAVI_ACIK); c.set_edgecolor("none"); ax.add_patch(c)
    else:
        sol_kirp = patches.Circle((2.25, 2.0), 1.5, transform=ax.transData)
        kes = patches.Circle((3.75, 2.0), 1.5, facecolor=MAVI_ACIK, edgecolor="none")
        ax.add_patch(kes); kes.set_clip_path(sol_kirp)
    for m in ((2.25, 2.0), (3.75, 2.0)):
        ax.add_patch(patches.Circle(m, 1.5, facecolor="none", edgecolor=MAVI, lw=2))
    ax.text(0.75, 3.55, "A", fontsize=16, fontweight="bold", color=MAVI)
    ax.text(5.0, 3.55, "B", fontsize=16, fontweight="bold", color=MAVI)
    ax.text(3.0, 4.35, baslik, fontsize=16, fontweight="bold", ha="center", color=YAZI)
    ax.text(3.0, -0.25, alt, fontsize=13, ha="center", color=SOLUK)
fig.subplots_adjust(wspace=0.05)
kaydet(fig, __file__)
