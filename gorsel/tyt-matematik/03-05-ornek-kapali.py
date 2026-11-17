import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: 2x + y ≤ 4. Sınır doğrusu düz çizgi, orijinin bulunduğu taraf (alt) boyalı.
fig, ax = sekil(5.2, 5)
eksenler(ax, x=(-2, 5), y=(-2, 6))
ax.set_xticks(range(-1, 5)); ax.set_yticks(range(1, 6))
ax.set_xticklabels([str(t).replace("-", "−") if t else "" for t in range(-1, 5)])
ax.set_yticklabels([str(t).replace("-", "−") if t else "" for t in range(1, 6)])
xs = np.linspace(-2, 5, 200)
ax.fill_between(xs, -2, 4 - 2 * xs, color=MAVI_ACIK, zorder=0.2)
ax.plot(xs, 4 - 2 * xs, color=MAVI, zorder=3)
nokta(ax, 2, 0, "(2, 0)", dx=0.15, dy=0.25, renk=MAVI)
nokta(ax, 0, 4, "(0, 4)", dx=0.2, dy=0.1, renk=MAVI)
nokta(ax, 0, 0, "", renk=YESIL)
ax.text(-1.85, -1.45, "Deneme: (0, 0) → 0 ≤ 4 doğru", color=YESIL, fontsize=12)
ax.text(2.35, 2.6, "2x + y = 4\n(düz çizgi)", color=MAVI, fontsize=12)
kaydet(fig, __file__)
