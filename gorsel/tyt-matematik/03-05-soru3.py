import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 3: (4, 0) ve (0, 2) noktalarından geçen düz doğru; orijinin bulunduğu alt taraf boyalı (x + 2y ≤ 4).
fig, ax = sekil(5.2, 4.2)
eksenler(ax, x=(-2, 6), y=(-2, 4))
ax.set_xticks(range(-1, 6)); ax.set_yticks(range(-1, 4))
ax.set_xticklabels([str(t).replace("-", "−") if t else "" for t in range(-1, 6)])
ax.set_yticklabels([str(t).replace("-", "−") if t else "" for t in range(-1, 4)])
xs = np.linspace(-2, 6, 200)
ax.fill_between(xs, -2, 2 - xs / 2, color=MAVI_ACIK, zorder=0.2)
ax.plot(xs, 2 - xs / 2, color=MAVI, zorder=3)
nokta(ax, 4, 0, "", renk=MAVI); nokta(ax, 0, 2, "", renk=MAVI)
ax.text(0.2, -0.6, "O", color=SOLUK, fontsize=12)
kaydet(fig, __file__)
