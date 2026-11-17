import sys; sys.path.insert(0, "tools")
from cizim import *

# y = |x + 2| + |x| + |x − 3| grafiği; kritik noktalar −2, 0, 3; en küçük değer 5 (x = 0).
f = lambda x: np.abs(x + 2) + np.abs(x) + np.abs(x - 3)
fig, ax = sekil(6, 4.6)
eksenler(ax, x=(-4.5, 5.2), y=(-1.2, 14))
ax.set_xticks(range(-4, 6)); ax.set_yticks(range(2, 14, 2))
ax.set_xticklabels([str(t).replace("-", "−") if t != 0 else "" for t in range(-4, 6)])
xs = np.linspace(-4, 4.8, 400)
ax.plot(xs, f(xs), color=MAVI, lw=2.6, zorder=3)
for k, d, renk in ((-2, 7, SOLUK), (0, 5, KIRMIZI), (3, 8, SOLUK)):
    ax.plot([k, k], [0, d], ls="--", color=renk, lw=1.2, zorder=2)
    ax.plot(k, d, "o", color=renk, markersize=8, zorder=5)
ax.text(-2.2, 6.2, "7", ha="right", fontsize=13, color=SOLUK)
ax.text(3.2, 7.2, "8", ha="left", fontsize=13, color=SOLUK)
ax.text(0.25, 4.0, "en küçük: 5", ha="left", va="top", fontsize=13, color=KIRMIZI, fontweight="bold")
ax.text(0.12, -0.35, "0", ha="left", va="top", fontsize=12, color=SOLUK)
kaydet(fig, __file__)
