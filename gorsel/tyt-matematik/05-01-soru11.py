import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 11: A aracı 200 km'de 16 L, B aracı 150 km'de 9 L yakıt harcıyor (doğru orantı).
fig, ax = sekil(6, 4.2)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.set_xlim(0, 320); ax.set_ylim(0, 26)
xs = np.array([0, 300])
ax.plot(xs, 0.08 * xs, color=MAVI); ax.plot(xs, 0.06 * xs, color=SARI)
ax.text(302, 24, "A", color=MAVI, fontsize=15, fontweight="bold", va="center")
ax.text(302, 18, "B", color=SARI, fontsize=15, fontweight="bold", va="center")
for x, y, r in ((200, 16, MAVI), (150, 9, SARI)):
    ax.plot([x, x], [0, y], "--", color=SOLUK, lw=1); ax.plot([0, x], [y, y], "--", color=SOLUK, lw=1)
    nokta(ax, x, y, renk=r)
ax.set_xticks([0, 50, 100, 150, 200, 250, 300]); ax.set_yticks([0, 9, 16])
ax.set_yticklabels(["0", "9", "16"])
ax.set_xlabel("yol (km)"); ax.set_ylabel("yakıt (L)")
kaydet(fig, __file__)
