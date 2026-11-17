import sys; sys.path.insert(0, "tools")
from cizim import *

# 6 günde bir ve 10 günde bir tekrar eden iki olay; ortak günler EKOK(6, 10) = 30'un katları.
fig, ax = sekil(6.4, 2.9)
ax.axis("off")
satirlar = [(1.0, 6, "6 günde bir", MAVI), (0.0, 10, "10 günde bir", YESIL)]
for y, p, ad, renk in satirlar:
    ax.plot([0, 92], [y, y], color=CIZGI, lw=1.2)
    ax.text(-3, y, ad, ha="right", va="center", fontsize=12, color=renk)
    for g in range(0, 91, p):
        ortak = g % 30 == 0
        ax.plot(g, y, "o", ms=8 if ortak else 6, mfc=renk if ortak else "white", mec=renk, mew=1.6, zorder=5)
for k, g in enumerate(range(0, 91, 30)):
    ax.add_patch(patches.FancyBboxPatch((g - 1.6, -0.45), 3.2, 1.9, boxstyle="round,pad=0.1",
                                        fc=SARI_ACIK, ec=SARI, lw=1.2, zorder=1))
    ax.text(g, -0.7, str(g), ha="center", va="top", fontsize=12, color=YAZI)
    ax.text(g, 1.65, f"{k + 1}. kez", ha="center", va="bottom", fontsize=11.5, color=SARI)
ax.text(96, -0.7, "gün", ha="left", va="top", fontsize=11.5, color=SOLUK)
ax.set_xlim(-24, 104); ax.set_ylim(-1.4, 2.3)
kaydet(fig, __file__)
