import sys; sys.path.insert(0, "tools")
from cizim import *

fig, ax = sekil(6, 4.4)
eksenler(ax, x=(-4.2, 4.2), y=(-19, 15))
yt = [-16, -8, 8]
ax.set_xticks([-3, -1, 1, 3]); ax.set_xticklabels([]); ax.set_yticks(yt)
ax.set_yticklabels([str(v).replace("-", "−") for v in yt])
xs = np.linspace(-3.45, 3.45, 400)
ax.plot(xs, xs**4 - 10 * xs**2 + 9, color=MAVI)
# kök etiketleri, eğrinin olmadığı tarafa
for k, dx in ((-3, -0.35), (-1, 0.35), (1, -0.35), (3, 0.35)):
    nokta(ax, k, 0, renk=KIRMIZI)
    ax.text(k + dx, -1.2, str(k).replace("-", "−"), ha="center", va="top", color=KIRMIZI, fontsize=13)
ax.text(0.2, 12.2, "y = x⁴ − 10x² + 9", ha="left", color=MAVI, fontsize=12)
kaydet(fig, __file__)
