import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: x − 2y < 4  ⇔  y > x/2 − 2. Sınır kesikli, doğrunun üstü boyalı.
fig, ax = sekil(5.6, 4.6)
eksenler(ax, x=(-3, 6), y=(-4, 4))
ax.set_xticks(range(-2, 6)); ax.set_yticks(range(-3, 4))
ax.set_xticklabels([str(t).replace("-", "−") if t else "" for t in range(-2, 6)])
ax.set_yticklabels([str(t).replace("-", "−") if t else "" for t in range(-3, 4)])
xs = np.linspace(-3, 6, 200)
ax.fill_between(xs, xs / 2 - 2, 4, color=MAVI_ACIK, zorder=0.2)
ax.plot(xs, xs / 2 - 2, color=KIRMIZI, ls=(0, (6, 4)), zorder=3)
nokta(ax, 4, 0, "", renk=KIRMIZI, dolu=False)
nokta(ax, 0, -2, "", renk=KIRMIZI, dolu=False)
ax.text(3.25, 0.25, "(4, 0)", color=KIRMIZI, fontsize=12)
ax.text(0.2, -2.6, "(0, −2)", color=KIRMIZI, fontsize=12)
ax.text(1.6, -3.5, "x − 2y = 4 (kesikli)", color=KIRMIZI, fontsize=12)
ax.text(1.0, 2.3, "y > x/2 − 2\ndoğrunun üstü", color=MAVI, fontsize=12)
kaydet(fig, __file__)
