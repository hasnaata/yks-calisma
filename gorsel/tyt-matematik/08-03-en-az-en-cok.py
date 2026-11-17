import sys; sys.path.insert(0, "tools")
from cizim import *

# Solda "en az biri" (a + b + c), sağda "en çok biri" (a + c + d) boyalı.
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.9))
for ax, baslik, alt, renk in ((axs[0], "En az biri", "a + b + c", MAVI), (axs[1], "En çok biri", "a + c + d", KIRMIZI)):
    ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.2, 10.2); ax.set_ylim(-1.9, 7.4)
    boya = MAVI_ACIK if renk == MAVI else KIRMIZI_ACIK
    sol, sag = (3.7, 3.0), (6.3, 3.0)
    if renk == MAVI:
        ax.add_patch(patches.Rectangle((0, 0), 10, 6.0, facecolor="white", edgecolor=SOLUK, lw=1.4))
        ax.add_patch(patches.Ellipse(sol, 4.8, 4.2, facecolor=boya, edgecolor="none"))
        ax.add_patch(patches.Ellipse(sag, 4.8, 4.2, facecolor=boya, edgecolor="none"))
    else:
        ax.add_patch(patches.Rectangle((0, 0), 10, 6.0, facecolor=boya, edgecolor=SOLUK, lw=1.4))
        # ortak bölge (mercek) beyaz
        xs = np.linspace(3.7, 6.3, 400)
        ust = 3.0 + 2.1 * np.sqrt(np.clip(1 - ((xs - 3.7) / 2.4) ** 2, 0, 1))
        ust2 = 3.0 + 2.1 * np.sqrt(np.clip(1 - ((xs - 6.3) / 2.4) ** 2, 0, 1))
        y = np.minimum(ust, ust2) - 3.0
        ax.fill_between(xs, 3.0 - y, 3.0 + y, color="white", lw=0)
    ax.add_patch(patches.Ellipse(sol, 4.8, 4.2, facecolor="none", edgecolor=MAVI, lw=1.8))
    ax.add_patch(patches.Ellipse(sag, 4.8, 4.2, facecolor="none", edgecolor=YESIL, lw=1.8))
    for x0, y0, h in ((2.6, 3.0, "a"), (5.0, 3.0, "b"), (7.4, 3.0, "c"), (9.2, 0.6, "d")):
        ax.text(x0, y0, h, fontsize=19, ha="center", va="center", color=YAZI, fontweight="bold")
    ax.text(1.0, 5.15, "A", fontsize=14, fontweight="bold", color=MAVI)
    ax.text(8.5, 5.15, "B", fontsize=14, fontweight="bold", color=YESIL)
    ax.text(5.0, 6.7, baslik, fontsize=14, ha="center", fontweight="bold", color=renk)
    ax.text(5.0, -1.1, alt, fontsize=14, ha="center", color=renk)
fig.subplots_adjust(wspace=0.08)
kaydet(fig, __file__)
