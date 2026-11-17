import sys; sys.path.insert(0, "tools")
from cizim import *

# a^2 - b^2 = (a - b)(a + b): kareden b^2 kesilir, kalan şerit döndürülüp yana eklenir. a = 3, b = 1,2.
A, B = 3.0, 1.2
fig, ax = sekil(6.5, 3.8)
ax.axis("off"); ax.set_aspect("equal")
# Sol: a x a kare, sağ üst köşeden b x b kesilmiş
ax.add_patch(patches.Rectangle((0, 0), A, A - B, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.add_patch(patches.Rectangle((0, A - B), A - B, B, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2))
ax.add_patch(patches.Rectangle((A - B, A - B), B, B, facecolor="none", edgecolor=KIRMIZI, lw=1.5, ls="--"))
ax.text(A - B / 2, A - B / 2, r"$b^2$", ha="center", va="center", fontsize=15, color=KIRMIZI)
ax.text(A / 2, -0.2, "a", ha="center", va="top", fontsize=15)
ax.text(-0.2, (A - B) / 2, "a − b", ha="right", va="center", fontsize=14)
ax.text(-0.2, A - B / 2, "b", ha="right", va="center", fontsize=14)
ax.text((A - B) / 2, A + 0.15, "a − b", ha="center", va="bottom", fontsize=14)
ax.text(A / 2, -0.75, r"$a^2 - b^2$", ha="center", va="top", fontsize=16, color=YAZI)
# Ok
ax.annotate("", xy=(A + 1.5, (A - B) / 2), xytext=(A + 0.5, (A - B) / 2), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=2))
# Sağ: (a + b) x (a - b) dikdörtgen
X = A + 2.0
ax.add_patch(patches.Rectangle((X, 0), A, A - B, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.add_patch(patches.Rectangle((X + A, 0), B, A - B, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2))
ax.text(X + A / 2, -0.2, "a", ha="center", va="top", fontsize=15)
ax.text(X + A + B / 2, -0.2, "b", ha="center", va="top", fontsize=15)
ax.text(X + A + B + 0.2, (A - B) / 2, "a − b", ha="left", va="center", fontsize=14)
ax.text(X + (A + B) / 2, -0.75, r"$(a + b)(a - b)$", ha="center", va="top", fontsize=16, color=YAZI)
ax.set_xlim(-1.4, X + A + B + 1.4); ax.set_ylim(-1.5, A + 0.7)
kaydet(fig, __file__)
