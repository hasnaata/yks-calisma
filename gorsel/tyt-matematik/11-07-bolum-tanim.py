import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = x + 3, g(x) = x² − 4. f/g için g(x) = 0 yapan −2 ve 2 atılır.
# −3 atılmaz: (f/g)(−3) = 0 / 5 = 0, tanımlı.
fig, ax = sekil(6, 1.9)
sayi_dogrusu(ax, -4, 4)
ax.set_ylim(-0.9, 0.95)
for a, b in ((-4.45, -2), (-2, 2), (2, 4.45)):
    ax.plot([a, b], [0, 0], color=MAVI, lw=4, solid_capstyle="butt", zorder=3)
nokta(ax, -2, 0, renk=KIRMIZI, dolu=False); nokta(ax, 2, 0, renk=KIRMIZI, dolu=False)
nokta(ax, -3, 0, renk=YESIL)
ax.text(-2, 0.3, "g(−2) = 0", ha="center", color=KIRMIZI, fontsize=12)
ax.text(2, 0.3, "g(2) = 0", ha="center", color=KIRMIZI, fontsize=12)
ax.text(-3.55, 0.62, "(f/g)(−3) = 0", ha="center", color=YESIL, fontsize=12)
kaydet(fig, __file__)
