import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 10: (4, 0) ve (0, −3) noktalarından geçen düz doğru (3x − 4y = 12); orijinin bulunduğu sol üst taraf boyalı.
fig, ax = sekil(5.2, 4.4)
eksenler(ax, x=(-2, 6), y=(-5, 3))
ax.set_xticks(range(-1, 6)); ax.set_yticks(range(-4, 3))
ax.set_xticklabels([str(t).replace("-", "−") if t else "" for t in range(-1, 6)])
ax.set_yticklabels([str(t).replace("-", "−") if t else "" for t in range(-4, 3)])
xs = np.linspace(-2, 6, 200)
yl = 3 * xs / 4 - 3
ax.fill_between(xs, yl, 3, color=MAVI_ACIK, zorder=0.2)
ax.plot(xs, yl, color=MAVI, zorder=3)
nokta(ax, 4, 0, "", renk=MAVI); nokta(ax, 0, -3, "", renk=MAVI)
ax.text(-0.45, 0.25, "O", color=SOLUK, fontsize=12)
kaydet(fig, __file__)
