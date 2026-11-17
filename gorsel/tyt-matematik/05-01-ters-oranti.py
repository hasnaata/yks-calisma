import sys; sys.path.insert(0, "tools")
from cizim import *

# Ters orantı: işçi sayısı x, gün y, x · y = 60. Dikdörtgenlerin alanı hep 60.
fig, ax = sekil(6, 4.2)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.set_xlim(0, 12.5); ax.set_ylim(0, 32)
xs = np.linspace(1.9, 12.3, 300); ax.plot(xs, 60 / xs, color=KIRMIZI)
ax.add_patch(patches.Rectangle((0, 0), 4, 15, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4, alpha=0.8))
ax.add_patch(patches.Rectangle((0, 0), 6, 10, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.4, alpha=0.8))
nokta(ax, 4, 15, renk=MAVI); nokta(ax, 6, 10, renk=YESIL)
ax.text(4.3, 16.2, "4 · 15 = 60", color=MAVI, fontsize=12)
ax.text(6.3, 11.2, "6 · 10 = 60", color=YESIL, fontsize=12)
ax.set_xticks([0, 2, 4, 6, 8, 10, 12]); ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
ax.set_xlabel("işçi sayısı"); ax.set_ylabel("gün")
kaydet(fig, __file__)
