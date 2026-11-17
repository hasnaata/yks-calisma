import sys; sys.path.insert(0, "tools")
from cizim import *

# Doğru orantı: elmanın fiyatı y = 15x (x kg, y TL). Grafik orijinden geçen doğru.
fig, ax = sekil(6, 4.2)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.set_xlim(0, 8.5); ax.set_ylim(0, 130)
xs = np.array([0, 8.2]); ax.plot(xs, 15 * xs, color=MAVI)
for x in (3, 7):
    y = 15 * x
    ax.plot([x, x], [0, y], "--", color=SOLUK, lw=1); ax.plot([0, x], [y, y], "--", color=SOLUK, lw=1)
    nokta(ax, x, y, renk=MAVI)
    ax.text(x + 0.2, y - 9, f"{y} ÷ {x} = 15", color=MAVI, fontsize=12)
ax.set_xticks(range(0, 9)); ax.set_yticks([0, 15, 45, 75, 105])
ax.set_xlabel("elma (kg)"); ax.set_ylabel("fiyat (TL)")
ax.grid(True, color=CIZGI, linewidth=0.6, alpha=0.7); ax.set_axisbelow(True)
kaydet(fig, __file__)
