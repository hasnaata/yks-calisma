import sys; sys.path.insert(0, "tools")
from cizim import *

# Tek fonksiyon: f(x) = x³ − 3x. f(2) = 2, f(−2) = −2; grafik orijine göre simetrik.
fig, ax = sekil(5, 3.8)
eksenler(ax, (-3.6, 3.6), (-3.6, 3.6))
ax.set_xticks([-2, 2]); ax.set_xticklabels(["", ""])
ax.set_yticks([-2, 2]); ax.set_yticklabels(["", ""])
x = np.linspace(-2.3, 2.3, 300)
ax.plot(x, x**3 - 3*x, color=MAVI)
ax.plot([-2, 2], [-2, 2], "--", color=YESIL, lw=1.5)
nokta(ax, 0, 0, "", renk=YESIL)
nokta(ax, 2, 2, "(2, 2)", dx=0.2, dy=-0.55, renk=MAVI)
nokta(ax, -2, -2, "(−2, −2)", dx=0.25, dy=-0.65, renk=MAVI)
ax.text(-3.4, 3.0, "y = x³ − 3x", color=MAVI, fontsize=12, ha="left")
ax.text(0.25, -0.55, "O", color=YESIL, fontsize=12)
kaydet(fig, __file__)
