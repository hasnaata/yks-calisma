import sys; sys.path.insert(0, "tools")
from cizim import *

# Sol: f(x) = 2x - 1, y = 3 doğrusu grafiği bir kez keser (x = 2).
# Sağ: g(x) = x^2, y = 4 doğrusu iki kez keser (x = -2, 2); y = -2 hiç kesmez.
fig, eks = plt.subplots(1, 2, figsize=(6.5, 3.8))
x = np.linspace(-4, 4, 200)

ax = eks[0]; eksenler(ax, (-3.5, 3.5), (-4.5, 5.5))
ax.set_xticks([-2, 2]); ax.set_yticks([2, 4])
ax.set_xticklabels(["−2", "2"]); ax.set_yticklabels(["2", "4"])
ax.plot(x, 2 * x - 1, color=MAVI)
ax.axhline(3, color=YESIL, lw=1.6, ls="--")
nokta(ax, 2, 3, renk=YESIL)
ax.text(-3.3, 3.3, "y = 3", color=YESIL, fontsize=12)
ax.text(0.5, -4.3, "f(x) = 2x − 1", color=MAVI, fontsize=12)
ax.text(0.5, -0.08, "Bire bir", transform=ax.transAxes, ha="center", va="top", color=YESIL, fontsize=13, fontweight="bold")

ax = eks[1]; eksenler(ax, (-3.5, 3.5), (-4.5, 5.5))
ax.set_xticks([-2, 2]); ax.set_yticks([2, 4])
ax.set_xticklabels(["−2", "2"]); ax.set_yticklabels(["2", "4"])
ax.plot(x, x ** 2, color=MAVI)
ax.axhline(4, color=KIRMIZI, lw=1.6, ls="--")
nokta(ax, -2, 4, renk=KIRMIZI); nokta(ax, 2, 4, renk=KIRMIZI)
ax.axhline(-2, color=SARI, lw=1.6, ls="--")
ax.text(0.25, 4.35, "y = 4", color=KIRMIZI, fontsize=12)
ax.text(0.25, -1.65, "y = −2", color=SARI, fontsize=12)
ax.text(-3.4, -3.6, "g(x) = x²", color=MAVI, fontsize=12)
ax.text(0.5, -0.08, "Bire bir değil", transform=ax.transAxes, ha="center", va="top", color=KIRMIZI, fontsize=13, fontweight="bold")
fig.subplots_adjust(wspace=0.25)
kaydet(fig, __file__)
