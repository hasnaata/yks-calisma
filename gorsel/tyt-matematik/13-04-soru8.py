import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 8: P(x) = (x + 2)(x − 1)(x − 3) = x³ − 2x² − 5x + 6.
# Grafikte yalnızca kökler (−2, 1, 3) ve y eksenini kestiği nokta (6) verilir; P(2) = −4 okunmasın diye ızgara yok.
fig, ax = sekil(5.6, 4.6)
eksenler(ax, x=(-3, 4.2), y=(-8.5, 9.5), izgara=False)
ax.set_xticks([]); ax.set_yticks([])
xs = np.linspace(-2.38, 3.55, 300); ax.plot(xs, (xs + 2) * (xs - 1) * (xs - 3), color=MAVI)
kutu = dict(facecolor="white", edgecolor="none", pad=1.5, alpha=0.9)
for r, t in ((-2, "−2"), (1, "1"), (3, "3")):
    nokta(ax, r, 0)
for r, t, dx in ((-2, "−2", 0.35), (1, "1", -0.25), (3, "3", 0.3)):
    ax.text(r + dx, -0.6, t, fontsize=13, ha="center", va="top", bbox=kutu)
nokta(ax, 0, 6)
ax.text(-0.25, 6, "6", fontsize=13, ha="right", va="center", bbox=kutu)
ax.text(2.75, 7.6, "y = P(x)", color=MAVI, fontsize=13, ha="center", bbox=kutu)
kaydet(fig, __file__)
