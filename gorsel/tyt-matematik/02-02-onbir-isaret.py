import sys; sys.path.insert(0, "tools")
from cizim import *

# 11 ile kalan: rakamlar SAĞDAN başlayarak +, −, +, − ile işaretlenir. Örnek: 7352
RAKAMLAR = "7352"
fig, ax = sekil(6, 3.6)
ax.set_xlim(-0.6, 6.6); ax.set_ylim(-2.9, 1.9); ax.axis("off"); ax.set_aspect("equal")
n = len(RAKAMLAR)
for i, r in enumerate(RAKAMLAR):
    sira = n - 1 - i                      # sağdan sıra: 0, 1, 2, ...
    arti = sira % 2 == 0
    renk, acik = (YESIL, YESIL_ACIK) if arti else (KIRMIZI, KIRMIZI_ACIK)
    x = 0.6 + i * 1.3
    ax.add_patch(patches.FancyBboxPatch((x, 0), 1.0, 1.0, boxstyle="round,pad=0.02", facecolor=acik, edgecolor=renk, lw=1.5))
    ax.text(x + 0.5, 0.5, r, ha="center", va="center", fontsize=22, color=YAZI)
    ax.text(x + 0.5, -0.45, "+" if arti else "−", ha="center", va="center", fontsize=22, color=renk, fontweight="bold")
# Sağdan başla oku
ax.annotate("", xy=(0.6, 1.45), xytext=(0.6 + n * 1.3 - 0.3, 1.45), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.6))
ax.text(0.6 + n * 1.3 - 0.1, 1.45, "sağdan başla", ha="left", va="center", color=SOLUK, fontsize=12)
ax.text(0.6, -1.35, "(2 + 3) − (5 + 7) = −7", ha="left", va="center", fontsize=15, color=YAZI)
ax.text(0.6, -2.2, "−7 + 11 = 4   →   kalan 4", ha="left", va="center", fontsize=15, color=MAVI)
kaydet(fig, __file__)
