import sys; sys.path.insert(0, "tools")
from cizim import *

# Üç grafik: I. y = x³/4 (tek), II. y = x²/2 − 2 (çift), III. y = −x/2 (tek).
fig, eks = plt.subplots(1, 3, figsize=(6.5, 2.9))
x = np.linspace(-3.4, 3.4, 200)
egriler = (("I", x**3 / 4), ("II", x**2 / 2 - 2), ("III", -x / 2))
for ax, (ad, y) in zip(eks, egriler):
    eksenler(ax, (-3.6, 3.6), (-3.6, 3.6))
    ax.set_xticks([-2, 2]); ax.set_xticklabels(["", ""])
    ax.set_yticks([-2, 2]); ax.set_yticklabels(["", ""])
    ax.plot(x, y, color=MAVI)
    ax.text(0.5, -0.1, ad, transform=ax.transAxes, ha="center", va="top", fontsize=14, fontweight="bold")
fig.subplots_adjust(wspace=0.25)
kaydet(fig, __file__)
