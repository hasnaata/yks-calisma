import sys; sys.path.insert(0, "tools")
from cizim import *

# Daire içi: o önerme doğru (1). Boyalı bölge: bileşik önermenin doğru olduğu durumlar.
fig, axs = plt.subplots(1, 3, figsize=(6.5, 2.9))
P, Q, R = (-0.55, 0), (0.55, 0), 1.0

def panel(ax, baslik, renk, acik, tur):
    ax.add_patch(patches.Rectangle((-1.9, -1.35), 3.8, 2.7, facecolor="white", edgecolor=SOLUK, lw=1.2))
    cp = patches.Circle(P, R, facecolor="none", edgecolor="none")
    cq = patches.Circle(Q, R, facecolor="none", edgecolor="none")
    ax.add_patch(cp); ax.add_patch(cq)
    if tur in ("veya", "yada"):
        for c in (P, Q):
            ax.add_patch(patches.Circle(c, R, facecolor=acik, edgecolor="none"))
    if tur in ("ve", "yada"):
        kes = patches.Circle(Q, R, facecolor=(acik if tur == "ve" else "white"), edgecolor="none")
        ax.add_patch(kes); kes.set_clip_path(cp)
    for c in (P, Q):
        ax.add_patch(patches.Circle(c, R, facecolor="none", edgecolor=renk, lw=2))
    ax.text(-1.05, 0, "p", ha="center", va="center", fontsize=16, color=YAZI, fontweight="bold")
    ax.text(1.05, 0, "q", ha="center", va="center", fontsize=16, color=YAZI, fontweight="bold")
    ax.text(0, 1.62, baslik, ha="center", va="bottom", fontsize=16, color=renk, fontweight="bold")
    ax.set_xlim(-2, 2); ax.set_ylim(-1.45, 2.25); ax.set_aspect("equal"); ax.axis("off")

panel(axs[0], "p ∧ q", MAVI, "#b9cff2", "ve")
panel(axs[1], "p ∨ q", YESIL, "#a9dcbb", "veya")
panel(axs[2], "p ⊻ q", SARI, "#f3d58c", "yada")
fig.subplots_adjust(wspace=0.08)
kaydet(fig, __file__)
