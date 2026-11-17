import sys; sys.path.insert(0, "tools")
from cizim import *

# Lamba 13.00.00'da yanar, sonra 50 saniyede bir. Dakika başları 60 saniyede bir.
# İkisi EKOK(50, 60) = 300 saniyede (5 dakikada) bir çakışır.
fig, ax = sekil(6.4, 2.6)
ax.axis("off")
ax.plot([0, 330], [0, 0], color=SOLUK, lw=1.4)
for t in range(0, 301, 60):
    ax.plot([t, t], [-0.25, 0], color=YAZI, lw=1.6)
    ax.text(t, -0.35, "13.%02d" % (t // 60), ha="center", va="top", fontsize=11)
for t in range(0, 301, 50):
    cak = t % 60 == 0
    ax.plot(t, 0.35, "o", color=YESIL if cak else MAVI, markersize=11 if cak else 8, zorder=4)
    ax.text(t, 0.62, str(t), ha="center", va="bottom", fontsize=10, color=YESIL if cak else MAVI)
ax.text(-12, 0.35, "yanış", ha="right", va="center", fontsize=11, color=MAVI)
ax.text(-12, 0.75, "saniye", ha="right", va="center", fontsize=10, color=SOLUK)
ax.text(-12, -0.12, "dakika", ha="right", va="center", fontsize=11, color=YAZI)
ax.text(150, -0.95, "Yeşil: tam dakika başında yanış (300 saniyede bir)", ha="center", va="top", fontsize=12, color=YESIL)
ax.set_xlim(-60, 335); ax.set_ylim(-1.35, 1.05)
kaydet(fig, __file__)
