import sys; sys.path.insert(0, "tools")
from cizim import *

fig, ax = sekil(6, 4.6)
eksenler(ax, x=(-7, 4.5), y=(-14, 10))
xt, yt = [-6, -4, -2, 4], [-8, -4, 4, 8]
ax.set_xticks(xt); ax.set_yticks(yt)
ax.set_xticklabels([str(v).replace("-", "−") for v in xt])
ax.set_yticklabels([str(v).replace("-", "−") for v in yt])
xs = np.linspace(-6.9, 3.9, 300)
ax.plot(xs, xs**2 + 3 * xs - 10, color=MAVI)
for k in (-5, 2):
    nokta(ax, k, 0, renk=KIRMIZI)
ax.text(-5.3, -3.2, "x = −5", ha="right", color=KIRMIZI, fontsize=13)
ax.text(2.3, -3.2, "x = 2", ha="left", color=KIRMIZI, fontsize=13)
ax.text(-2.7, 8.3, "y = x² + 3x − 10", ha="center", color=MAVI, fontsize=12)
kaydet(fig, __file__)
