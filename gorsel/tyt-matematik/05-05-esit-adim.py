import sys; sys.path.insert(0, "tools")
from cizim import *

# "Ben senin yaşındayken sen 6 yaşındaydın; sen benim yaşıma geldiğinde ben 33 olacağım."
# Yaş farkı d: 6, 6 + d, 6 + 2d, 6 + 3d = 33  =>  d = 9. Sen 15, ben 24.
fig, ax = sekil(6.2, 2.9)
ax.set_xlim(0, 39); ax.set_ylim(-2.6, 2.3); ax.axis("off")
ax.annotate("", xy=(38.5, 0), xytext=(0.5, 0), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.4))
noktalar = [(6, "sen", "o zaman", YESIL), (15, "sen şimdi", "ben o zaman", MAVI),
            (24, "ben şimdi", "sen sonra", MAVI), (33, "ben", "sonra", KIRMIZI)]
for x, ust1, ust2, renk in noktalar:
    ax.plot(x, 0, "o", color=renk, markersize=8, zorder=5)
    ax.text(x, -0.35, str(x), ha="center", va="top", fontsize=14, fontweight="bold", color=renk)
    ax.text(x, -1.25, f"{ust1}\n{ust2}", ha="center", va="top", fontsize=10.5, color=YAZI, linespacing=1.15)
for a in (6, 15, 24):
    ax.annotate("", xy=(a + 8.7, 0.25), xytext=(a + 0.3, 0.25),
                arrowprops=dict(arrowstyle="->", color=SARI, lw=1.6, connectionstyle="arc3,rad=-0.45"))
    ax.text(a + 4.5, 1.2, "+9", ha="center", va="bottom", fontsize=13, color=SARI, fontweight="bold")
kaydet(fig, __file__)
