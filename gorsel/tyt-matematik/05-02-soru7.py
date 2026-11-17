import sys; sys.path.insert(0, "tools")
from cizim import *

# A yazıcısı 4 dakikada 60 sayfa, B yazıcısı 6 dakikada 60 sayfa basar (doğru orantı).
fig, ax = sekil(5, 3.6)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.grid(True, color=CIZGI, linewidth=0.6, alpha=0.7); ax.set_axisbelow(True)
x = np.linspace(0, 8, 20)
ax.plot(x, 15 * x, color=MAVI); ax.plot(x, 10 * x, color=YESIL)
ax.text(6.0, 104, "A", color=MAVI, fontsize=14, fontweight="bold")
ax.text(7.4, 63, "B", color=YESIL, fontsize=14, fontweight="bold")
for px, renk in ((4, MAVI), (6, YESIL)):
    ax.plot([px, px], [0, 60], "--", color=SOLUK, lw=1)
    ax.plot(px, 60, "o", color=renk, markersize=6, zorder=5)
ax.plot([0, 6], [60, 60], "--", color=SOLUK, lw=1)
ax.set_xlim(0, 8.3); ax.set_ylim(0, 125)
ax.set_xticks(range(0, 9)); ax.set_yticks([0, 30, 60, 90, 120])
ax.tick_params(labelsize=11)
ax.set_xlabel("Süre (dakika)", fontsize=12); ax.set_ylabel("Basılan sayfa", fontsize=12)
kaydet(fig, __file__)
