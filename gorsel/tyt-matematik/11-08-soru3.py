import sys; sys.path.insert(0, "tools")
from cizim import *

# I: x = y² − 2 (yana yatık parabol) → fonksiyon değil.
# II: x < 1 için y = x + 1, (1, 2) boş; x ≥ 1 için y = 1 − x... (1, −1)? hayır: y = −1 sabit, (1, −1) dolu → fonksiyon.
# III: II ile aynı ama (1, 2) de dolu → x = 1 için iki değer → fonksiyon değil.
fig, eks = plt.subplots(1, 3, figsize=(6.5, 2.9))
lim = ((-3, 3.2), (-3, 3.4))
ax = eks[0]; eksenler(ax, *lim, izgara=False); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
y = np.linspace(-2.4, 2.4, 200); ax.plot(y ** 2 - 2, y, color=MAVI)
for i, dolu in ((1, None), (2, False), (3, True)):
    pass
for k, ax in ((2, eks[1]), (3, eks[2])):
    eksenler(ax, *lim, izgara=False); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    xs = np.linspace(-2.8, 1, 20); ax.plot(xs, xs + 1, color=MAVI)
    ax.plot([1, 3], [-1, -1], color=MAVI)
    nokta(ax, 1, 2, renk=MAVI, dolu=(k == 3))
    nokta(ax, 1, -1, renk=MAVI)
    ax.plot([1, 1], [-1, 2], color=SOLUK, ls=":", lw=1)
for ax, ad in zip(eks, ["I", "II", "III"]):
    ax.text(0.5, -0.04, ad, transform=ax.transAxes, ha="center", va="top", fontsize=14, fontweight="bold")
fig.subplots_adjust(wspace=0.15)
kaydet(fig, __file__)
