import sys; sys.path.insert(0, "tools")
from cizim import *

# ∀x ∈ ℝ, x² + 1 > 2x önermesinin değili: parça parça ne değişir?
fig, ax = sekil(6, 3.1)
ax.axis("off")
ust = [(0.6, "∀x", KIRMIZI), (1.95, "∈ ℝ,", SOLUK), (3.55, "x² + 1", SOLUK), (4.7, ">", KIRMIZI), (5.55, "2x", SOLUK)]
alt = [(0.6, "∃x", KIRMIZI), (1.95, "∈ ℝ,", SOLUK), (3.55, "x² + 1", SOLUK), (4.7, "≤", KIRMIZI), (5.55, "2x", SOLUK)]
for (x, s, r), (_, s2, r2) in zip(ust, alt):
    ax.text(x, 2.2, s, ha="center", va="center", fontsize=19, color=YAZI if r == SOLUK else r, fontweight="bold" if r != SOLUK else "normal")
    ax.text(x, 0.2, s2, ha="center", va="center", fontsize=19, color=YAZI if r2 == SOLUK else r2, fontweight="bold" if r2 != SOLUK else "normal")
for x in (0.6, 4.7):
    ax.annotate("", xy=(x, 0.6), xytext=(x, 1.8), arrowprops=dict(arrowstyle="->", color=KIRMIZI, lw=1.8))
for x in (1.95, 3.55):
    ax.annotate("", xy=(x, 0.6), xytext=(x, 1.8), arrowprops=dict(arrowstyle="->", color=CIZGI, lw=1.4, ls="--"))
ax.text(0.78, 1.2, "değişir", ha="left", va="center", fontsize=11, color=KIRMIZI)
ax.text(2.75, 1.2, "aynı kalır", ha="center", va="center", fontsize=11, color=SOLUK)
ax.text(4.88, 1.2, "değillenir", ha="left", va="center", fontsize=11, color=KIRMIZI)
ax.text(3.1, -0.65, "1. satır: 0  (x = 1 için 2 > 2 yanlış)     2. satır: 1", ha="center", va="center", fontsize=12, color=MAVI)
ax.set_xlim(0, 6.3); ax.set_ylim(-0.95, 2.6)
kaydet(fig, __file__)
