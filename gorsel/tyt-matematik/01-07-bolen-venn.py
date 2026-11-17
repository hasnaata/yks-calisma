import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders: 8 ile 15'in bölenleri (ortak yalnız 1) ve 12 ile 18'in bölenleri (ortak 1, 2, 3, 6).
fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.1))
def venn(ax, a, b, sol, orta, sag, baslik, renk):
    ax.axis("off"); ax.set_aspect("equal")
    ax.add_patch(patches.Circle((-0.65, 0), 1.25, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6, alpha=0.6))
    ax.add_patch(patches.Circle((0.65, 0), 1.25, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.6, alpha=0.6))
    ax.text(-0.9, 1.45, a, ha="center", fontsize=15, color=MAVI, fontweight="bold")
    ax.text(0.9, 1.45, b, ha="center", fontsize=15, color=SARI, fontweight="bold")
    def yaz(x, satirlar, k):
        n = len(satirlar)
        for t, s in enumerate(satirlar):
            ax.text(x, (n - 1) * 0.27 - t * 0.54, s, ha="center", va="center", fontsize=14,
                    fontweight="bold" if k else "normal", color=renk if k else YAZI)
    yaz(-1.25, sol, False); yaz(0, orta, True); yaz(1.25, sag, False)
    ax.text(0, -1.75, baslik, ha="center", fontsize=12, color=renk, fontweight="bold")
    ax.set_xlim(-2.0, 2.0); ax.set_ylim(-2.0, 1.85)
venn(axs[0], "8", "15", ["2", "4", "8"], ["1"], ["3", "5", "15"], "Ortak bölen yalnız 1", YESIL)
venn(axs[1], "12", "18", ["4", "12"], ["1  2", "3  6"], ["9", "18"], "Ortak bölen 1, 2, 3, 6", KIRMIZI)
fig.subplots_adjust(wspace=0.12)
kaydet(fig, __file__)
