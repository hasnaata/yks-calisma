import sys; sys.path.insert(0, "tools")
from cizim import *

# 3x^2 + 10x - 8 için çapraz çarpım şeması: satırlar çarpanları, çaprazlar orta terimi verir.
fig, ax = sekil(6, 3.6)
ax.axis("off")
ax.set_xlim(0, 10); ax.set_ylim(0, 6)
ax.text(0.3, 5.3, r"$3x^2 + 10x - 8$", fontsize=18, va="center")
# sol sütun (baş terimin çarpanları), sağ sütun (sabit terimin çarpanları)
ax.text(1.0, 3.8, r"$3x$", fontsize=20, ha="center", va="center", color=MAVI)
ax.text(1.0, 1.9, r"$x$", fontsize=20, ha="center", va="center", color=MAVI)
ax.text(3.6, 3.8, r"$-2$", fontsize=20, ha="center", va="center", color=SARI)
ax.text(3.6, 1.9, r"$+4$", fontsize=20, ha="center", va="center", color=SARI)
ax.plot([1.6, 3.0], [3.5, 2.2], color=YESIL, lw=2)
ax.plot([1.6, 3.0], [2.2, 3.5], color=KIRMIZI, lw=2)
ax.plot([0.3, 4.4], [1.2, 1.2], color=SOLUK, lw=1.2)
# çapraz çarpımlar
ax.text(5.0, 3.8, r"$3x \cdot (+4) = 12x$", fontsize=16, va="center", color=YESIL)
ax.text(5.0, 1.9, r"$x \cdot (-2) = -2x$", fontsize=16, va="center", color=KIRMIZI)
ax.plot([5.0, 9.6], [1.2, 1.2], color=SOLUK, lw=1.2)
ax.text(5.0, 0.55, "Toplam: 10x  (orta terim)", fontsize=15, va="center")
ax.text(0.3, 0.55, "(3x − 2)(x + 4)", fontsize=15, va="center", color=MAVI)
kaydet(fig, __file__)
