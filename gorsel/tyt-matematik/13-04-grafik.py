import sys; sys.path.insert(0, "tools")
from cizim import *

# P(x) = x³ − 4x² + x + 6 = (x + 1)(x − 2)(x − 3). Kökler −1, 2, 3 (grafik x eksenini keser).
# P(1) = 4: (x − 1) ile bölümünden kalan, grafiğin x = 1'deki yüksekliği. P(0) = 6 sabit terim.
fig, ax = sekil(5.6, 4.6)
eksenler(ax, x=(-2, 4.2), y=(-3, 7.6))
ax.set_xticks(range(-1, 5)); ax.set_xticklabels(["", "", "", "", "", ""])
ax.set_yticks(range(-2, 8)); ax.set_yticklabels([""] * 10)
xs = np.linspace(-1.42, 3.62, 300); ax.plot(xs, xs**3 - 4 * xs**2 + xs + 6, color=MAVI)
kutu = dict(facecolor="white", edgecolor="none", pad=1.5, alpha=0.9)
for r, t in ((-1, "−1"), (2, "2"), (3, "3")):
    nokta(ax, r, 0, renk=YESIL)
    ax.text(r, -0.45, t, color=YESIL, fontsize=13, ha="center", va="top", bbox=kutu)
ax.text(2.5, -1.85, "kökler: P = 0", color=YESIL, fontsize=12, ha="center", bbox=kutu)
nokta(ax, 1, 4, renk=KIRMIZI)
ax.plot([1, 1], [0, 4], color=KIRMIZI, lw=1.4, ls="--")
ax.text(1, -0.45, "1", color=KIRMIZI, fontsize=13, ha="center", va="top", bbox=kutu)
ax.text(1.2, 4.35, "P(1) = 4", color=KIRMIZI, fontsize=13, bbox=kutu)
nokta(ax, 0, 6, renk=SOLUK)
ax.text(0.2, 6.5, "P(0) = 6", color=SOLUK, fontsize=12, bbox=kutu)
kaydet(fig, __file__)
