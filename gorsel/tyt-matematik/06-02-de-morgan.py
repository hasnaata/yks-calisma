import sys; sys.path.insert(0, "tools")
from cizim import *

# De Morgan: boyalı bölge, değili alınan önermenin doğru olduğu durumlar.
fig, axs = plt.subplots(1, 2, figsize=(6.2, 3.3))
P, Q, R = (-0.55, 0), (0.55, 0), 1.0
BOYA = "#f4b9b2"

def panel(ax, ust, alt, tur):
    ax.add_patch(patches.Rectangle((-1.9, -1.35), 3.8, 2.7, facecolor=BOYA, edgecolor=SOLUK, lw=1.2))
    cp = patches.Circle(P, R, facecolor="none", edgecolor="none"); ax.add_patch(cp)
    if tur == "veya":
        for c in (P, Q):
            ax.add_patch(patches.Circle(c, R, facecolor="white", edgecolor="none"))
    else:
        kes = patches.Circle(Q, R, facecolor="white", edgecolor="none"); ax.add_patch(kes); kes.set_clip_path(cp)
    for c in (P, Q):
        ax.add_patch(patches.Circle(c, R, facecolor="none", edgecolor=KIRMIZI, lw=2))
    ax.text(-1.05, 0, "p", ha="center", va="center", fontsize=16, color=YAZI, fontweight="bold")
    ax.text(1.05, 0, "q", ha="center", va="center", fontsize=16, color=YAZI, fontweight="bold")
    ax.text(0, 1.6, ust, ha="center", va="bottom", fontsize=16, color=KIRMIZI, fontweight="bold")
    ax.text(0, -1.55, alt, ha="center", va="top", fontsize=16, color=MAVI, fontweight="bold")
    ax.set_xlim(-2, 2); ax.set_ylim(-2.25, 2.25); ax.set_aspect("equal"); ax.axis("off")

panel(axs[0], "(p ∨ q)′", "≡  p′ ∧ q′", "veya")
panel(axs[1], "(p ∧ q)′", "≡  p′ ∨ q′", "ve")
fig.subplots_adjust(wspace=0.1)
kaydet(fig, __file__)
