import sys; sys.path.insert(0, "tools")
from cizim import *

# A mumu: 30 cm, 10 saatte biter (3 cm/saat). B mumu: 20 cm, 20 saatte biter (1 cm/saat).
# 30 − 3t = 20 − t ⇒ t = 5, boy 15 cm.
fig, ax = sekil(5.8, 4.2)
eksenler(ax, x=(0, 23), y=(0, 34))
ax.set_xticks([5, 10, 15, 20]); ax.set_xticklabels(["5", "10", "15", "20"])
ax.set_yticks([5, 10, 15, 20, 25, 30]); ax.set_yticklabels(["", "10", "15", "20", "", "30"])
ax.plot([0, 10], [30, 0], color=MAVI); ax.plot([0, 20], [20, 0], color=YESIL)
ax.plot([5, 5], [0, 15], ":", color=SOLUK, lw=1.2); ax.plot([0, 5], [15, 15], ":", color=SOLUK, lw=1.2)
nokta(ax, 5, 15, renk=KIRMIZI)
kutu = dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.9)
ax.text(5.6, 16.2, "(5, 15)", color=KIRMIZI, fontsize=12, bbox=kutu)
ax.text(1.6, 28.5, "A", color=MAVI, fontsize=14, fontweight="bold")
ax.text(13.2, 8.6, "B", color=YESIL, fontsize=14, fontweight="bold")
ax.text(23, 1.2, "saat", ha="right", fontsize=12, color=SOLUK)
ax.text(0.5, 32.5, "boy (cm)", fontsize=12, color=SOLUK)
kaydet(fig, __file__)
