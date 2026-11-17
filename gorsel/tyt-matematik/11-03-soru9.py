import sys; sys.path.insert(0, "tools")
from cizim import *

# Üç fonksiyon grafiği (R -> R). I: y = -x + 1 (bire bir), II: y = x^2 - 2x (bire bir değil),
# III: y = x^3 / 6 + x / 2 (bire bir).
fig, eks = plt.subplots(1, 3, figsize=(6.5, 2.9))
x = np.linspace(-4, 4, 300)
for ax, yv, ad in ((eks[0], -x + 1, "I"), (eks[1], x ** 2 - 2 * x, "II"), (eks[2], x ** 3 / 6 + x / 2, "III")):
    eksenler(ax, (-3.2, 3.2), (-3.5, 4.2), izgara=False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.plot(x, yv, color=MAVI)
    ax.text(0.5, -0.06, ad, transform=ax.transAxes, ha="center", va="top", fontsize=14, fontweight="bold")
fig.subplots_adjust(wspace=0.3)
kaydet(fig, __file__)
