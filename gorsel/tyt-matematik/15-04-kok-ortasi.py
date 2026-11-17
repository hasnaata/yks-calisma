import sys; sys.path.insert(0, "tools")
from cizim import *

# y = 2x² − 7x + 3: kökler 1/2 ve 3, köklerin ortası 7/4
fig, ax = sekil(6, 4)
ax.axis("off"); ax.set_xlim(-0.9, 4.6); ax.set_ylim(-4.6, 6.2)
ax.annotate("", xy=(4.5, 0), xytext=(-0.8, 0), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.2))
ax.text(4.5, -0.45, "x", color=SOLUK, ha="center")
xs = np.linspace(-0.25, 3.75, 200)
ax.plot(xs, 2*xs**2 - 7*xs + 3, color=MAVI)
ax.plot([1.75, 1.75], [-3.4, 5.6], color=SARI, lw=1.6, ls="--")
nokta(ax, 0.5, 0, renk=YESIL); nokta(ax, 3, 0, renk=YESIL); nokta(ax, 1.75, 0, renk=SARI)
ax.text(0.38, -0.5, "x₁ = 1/2", ha="right", va="top", color=YESIL, fontsize=12)
ax.text(3.12, -0.5, "x₂ = 3", ha="left", va="top", color=YESIL, fontsize=12)
ax.text(1.9, 4.9, "orta nokta: 7/4", ha="left", color=SARI, fontsize=12)
ax.text(1.75, -4.3, "x₁ + x₂ = 7/2 = −b/a", ha="center", color=YAZI, fontsize=13)
ax.text(-0.15, 5.1, "y = 2x² − 7x + 3", ha="left", color=MAVI, fontsize=12)
kaydet(fig, __file__)
