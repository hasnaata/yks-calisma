import sys; sys.path.insert(0, "tools")
from cizim import *

# A = 12'nin bölenleri, B = 18'in bölenleri. Solda A \ B, sağda B \ A boyalı.
fig, axs = plt.subplots(1, 2, figsize=(6.2, 3.1))
for ax, baslik, sonuc, sol_boya in ((axs[0], "A \\ B", "= {4, 12}", True), (axs[1], "B \\ A", "= {9, 18}", False)):
    ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(0, 6); ax.set_ylim(-0.7, 4.7)
    boyali = patches.Circle((2.25, 2.0) if sol_boya else (3.75, 2.0), 1.5, facecolor=MAVI_ACIK, edgecolor="none")
    ax.add_patch(boyali)
    # ortak bölgeyi beyaza boya: boyalı dairenin, diğer daireyle kesişimi
    diger = patches.Circle((3.75, 2.0) if sol_boya else (2.25, 2.0), 1.5, facecolor="white", edgecolor="none")
    ax.add_patch(diger); diger.set_clip_path(patches.Circle(boyali.center, 1.5, transform=ax.transData))
    for m in ((2.25, 2.0), (3.75, 2.0)):
        ax.add_patch(patches.Circle(m, 1.5, facecolor="none", edgecolor=MAVI, lw=2))
    ax.text(0.7, 3.55, "A", fontsize=16, fontweight="bold", color=MAVI)
    ax.text(5.05, 3.55, "B", fontsize=16, fontweight="bold", color=MAVI)
    ax.text(1.5, 2.0, "4\n12", fontsize=13, ha="center", va="center", linespacing=1.5,
            color=YAZI if sol_boya else SOLUK, fontweight="bold" if sol_boya else "normal")
    ax.text(3.0, 2.0, "1  2\n3  6", fontsize=12, ha="center", va="center", linespacing=1.5, color=SOLUK)
    ax.text(4.5, 2.0, "9\n18", fontsize=13, ha="center", va="center", linespacing=1.5,
            color=SOLUK if sol_boya else YAZI, fontweight="normal" if sol_boya else "bold")
    ax.text(3.0, 4.3, baslik, fontsize=16, fontweight="bold", ha="center", color=YAZI)
    ax.text(3.0, -0.35, sonuc, fontsize=14, ha="center", color=MAVI)
fig.subplots_adjust(wspace=0.05)
kaydet(fig, __file__)
