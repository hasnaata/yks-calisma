import sys; sys.path.insert(0, "tools")
from cizim import *

# Üç madenî para. A = en az bir tura (7 çıktı), A' = hiç tura yok = {YYY}.
fig, ax = sekil(6, 4)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Rectangle((0, 0), 8, 5.3, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.6))
ax.add_patch(patches.Circle((3.0, 2.3), 2.0, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.text(0.2, 5.05, "E", fontsize=15, color=SOLUK, va="top")
ax.text(3.0, 4.62, "A: en az bir tura", ha="center", fontsize=12.5, color=MAVI, fontweight="bold")
yer = [(2.0, 2.95), (3.0, 2.95), (4.0, 2.95), (2.0, 2.15), (3.0, 2.15), (4.0, 2.15), (3.0, 1.35)]
for (x, y), s in zip(yer, ["YYT", "YTY", "TYY", "YTT", "TYT", "TTY", "TTT"]):
    ax.text(x, y, s, ha="center", va="center", fontsize=14, color=YAZI, family="DejaVu Sans Mono")
ax.text(6.55, 2.75, "A′: hiç\ntura yok", ha="center", va="center", fontsize=12.5, color=SARI, fontweight="bold")
ax.text(6.55, 1.55, "YYY", ha="center", va="center", fontsize=15, color=YAZI, family="DejaVu Sans Mono")
ax.text(4, -0.45, "s(A′) = 8 − 7 = 1", ha="center", va="top", fontsize=14, color=YAZI)
ax.set_xlim(-0.1, 8.1); ax.set_ylim(-1.2, 5.4)
kaydet(fig, __file__)
