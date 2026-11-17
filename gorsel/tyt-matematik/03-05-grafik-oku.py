import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: x eksenini −3'te, y eksenini 2'de kesen düz doğru; orijinin karşı tarafı (sol üst) boyalı.
# Doğru: 2x − 3y = −6 ; bölge 2x − 3y ≤ −6.
fig, ax = sekil(5.6, 4.6)
eksenler(ax, x=(-6, 3), y=(-2, 5))
ax.set_xticks(range(-5, 3)); ax.set_yticks(range(-1, 5))
ax.set_xticklabels([str(t).replace("-", "−") if t not in (0, -4, -5) else "" for t in range(-5, 3)])
ax.set_yticklabels([str(t).replace("-", "−") if t else "" for t in range(-1, 5)])
xs = np.linspace(-6, 3, 200)
yl = 2 * xs / 3 + 2
ax.fill_between(xs, yl, 5, color=MAVI_ACIK, zorder=0.2)
ax.plot(xs, yl, color=MAVI, zorder=3)
nokta(ax, -3, 0, "", renk=MAVI); nokta(ax, 0, 2, "", renk=MAVI)
nokta(ax, 0, 0, "", renk=YESIL)
ax.text(0.2, -0.6, "O", color=YESIL, fontsize=12)
kaydet(fig, __file__)
