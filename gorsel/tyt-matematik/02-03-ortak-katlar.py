import sys; sys.path.insert(0, "tools")
from cizim import *

# 4'ün ve 6'nın katları: ortak katlar 12, 24, 36, 48; bunların yalnızca yarısı 24'ün katı.
fig, ax = sekil(6.2, 3.2)
ax.axis("off")
ax.annotate("", xy=(51, 0), xytext=(-1.5, 0), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.4))
for k in range(4, 49, 4):
    ax.plot(k, 0.55, "o", color=MAVI, markersize=7)
for k in range(6, 49, 6):
    ax.plot(k, -0.55, "s", color=SARI, markersize=7)
for k in range(0, 49, 2):
    ax.plot([k, k], [-0.08, 0.08], color=SOLUK, lw=1)
for k in (0, 12, 24, 36, 48):
    ax.text(k, -1.25, str(k), ha="center", va="top", fontsize=13, color=YAZI)
for k in (12, 24, 36, 48):
    renk = KIRMIZI if k in (24, 48) else YESIL
    ax.add_patch(patches.FancyBboxPatch((k - 1.1, -0.95), 2.2, 1.9, boxstyle="round,pad=0.1", fill=False, ec=YESIL, lw=1.8))
    if k in (24, 48):
        ax.text(k, 1.35, "24'ün katı", ha="center", va="bottom", fontsize=11, color=KIRMIZI)
ax.text(-1.5, 0.55, "4'ün katları", ha="right", va="center", fontsize=12, color=MAVI)
ax.text(-1.5, -0.55, "6'nın katları", ha="right", va="center", fontsize=12, color=SARI)
ax.set_xlim(-14, 52); ax.set_ylim(-1.9, 2.0)
kaydet(fig, __file__)
