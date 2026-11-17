import sys; sys.path.insert(0, "tools")
from cizim import *

# Sol: x² + y² = 4 çemberi; x = 1 doğrusu iki noktada keser (y = ±√3) → fonksiyon değil.
# Sağ: y = x²/2 − 1; her düşey doğru bir kez keser → fonksiyon.
fig, eks = plt.subplots(1, 2, figsize=(6.5, 3.6))
ax = eks[0]; eksenler(ax, (-3.2, 3.2), (-3.2, 3.6)); ax.set_aspect("equal")
ax.set_xticks([]); ax.set_yticks([])
t = np.linspace(0, 2 * np.pi, 300); ax.plot(2 * np.cos(t), 2 * np.sin(t), color=MAVI)
ax.axvline(1, color=KIRMIZI, ls="--", lw=1.5)
nokta(ax, 1, np.sqrt(3), renk=KIRMIZI); nokta(ax, 1, -np.sqrt(3), renk=KIRMIZI)
ax.text(0.5, -0.06, "2 noktada keser:\nfonksiyon değil", transform=ax.transAxes, ha="center", va="top", color=KIRMIZI, fontsize=12, fontweight="bold")
ax = eks[1]; eksenler(ax, (-3.2, 3.2), (-3.2, 3.6)); ax.set_aspect("equal")
ax.set_xticks([]); ax.set_yticks([])
x = np.linspace(-3, 3, 200); ax.plot(x, x ** 2 / 2 - 1, color=MAVI)
for xv in (-1.5, 1):
    ax.axvline(xv, color=YESIL, ls="--", lw=1.5)
    nokta(ax, xv, xv ** 2 / 2 - 1, renk=YESIL)
ax.text(0.5, -0.06, "Hep 1 noktada keser:\nfonksiyon", transform=ax.transAxes, ha="center", va="top", color=YESIL, fontsize=12, fontweight="bold")
fig.subplots_adjust(wspace=0.2)
kaydet(fig, __file__)
