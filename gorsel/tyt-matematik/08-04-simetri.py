import sys; sys.path.insert(0, "tools")
from cizim import *

# A = {1, 2, 3}, B = {2, 3, 4}. A×B mavi, B×A kırmızı; ortak 4 nokta (A∩B)×(A∩B) = {2, 3}×{2, 3} yeşil.
# A×B ile B×A, y = x doğrusuna göre simetriktir.
fig, ax = sekil(5, 4.6)
eksenler(ax, x=(-0.3, 5), y=(-0.3, 5), izgara=True)
ax.set_xticks([1, 2, 3, 4]); ax.set_yticks([1, 2, 3, 4]); ax.set_aspect("equal")
ax.plot([0, 4.7], [0, 4.7], ls="--", color=SOLUK, lw=1.2)
ax.text(4.55, 4.75, "y = x", color=SOLUK, fontsize=12, ha="right")
A, B = {1, 2, 3}, {2, 3, 4}
AB = {(a, b) for a in A for b in B}; BA = {(b, a) for b in B for a in A}
for p in AB | BA:
    if p in AB and p in BA: renk, isaret = YESIL, "o"
    elif p in AB: renk, isaret = MAVI, "o"
    else: renk, isaret = KIRMIZI, "s"
    ax.plot(*p, isaret, color=renk, markersize=11, zorder=5)
ax.add_patch(patches.Rectangle((1.6, 1.6), 1.8, 1.8, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.4, zorder=1))
ax.plot([], [], "o", color=MAVI, markersize=9, label="yalnız A×B")
ax.plot([], [], "s", color=KIRMIZI, markersize=9, label="yalnız B×A")
ax.plot([], [], "o", color=YESIL, markersize=9, label="ikisinde de")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=3, frameon=False, fontsize=11, handletextpad=0.3, columnspacing=0.9)
kaydet(fig, __file__)
