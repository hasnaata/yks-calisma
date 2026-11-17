import sys; sys.path.insert(0, "tools")
from cizim import *

# Su faturası: ilk 10 m³ için m³ başına 8 TL, sonrası 12 TL.
# f(x) = 8x (0 ≤ x ≤ 10), 80 + 12(x − 10) (x > 10). f(10) = 80, f(15) = 140, f(20) = 200.
fig, ax = sekil(5.6, 4.2)
eksenler(ax, x=(0, 23), y=(0, 235), izgara=True)
ax.set_xticks([5, 10, 15, 20]); ax.set_yticks([40, 80, 120, 140, 160, 200])
ax.set_xlabel(""); ax.set_ylabel("")
xs = np.array([0, 10]); ax.plot(xs, 8 * xs, color=MAVI)
xs = np.array([10, 22]); ax.plot(xs, 80 + 12 * (xs - 10), color=YESIL)
for xx, yy in ((10, 80), (15, 140)):
    ax.plot([xx, xx], [0, yy], ":", color=SOLUK, lw=1.2); ax.plot([0, xx], [yy, yy], ":", color=SOLUK, lw=1.2)
nokta(ax, 10, 80, renk=KIRMIZI); nokta(ax, 15, 140, renk=KIRMIZI)
ax.text(10.6, 66, "(10, 80)", color=KIRMIZI, fontsize=12)
ax.text(15.6, 126, "(15, 140)", color=KIRMIZI, fontsize=12)
ax.text(2.2, 64, "8 TL/m³", color=MAVI, fontsize=12, rotation=0)
ax.text(17.2, 205, "12 TL/m³", color=YESIL, fontsize=12, ha="right")
ax.text(23, 14, "m³", ha="right", fontsize=12, color=SOLUK)
ax.text(0.4, 228, "TL", fontsize=12, color=SOLUK)
kaydet(fig, __file__)
