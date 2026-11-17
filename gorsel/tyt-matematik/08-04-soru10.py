import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 10: noktalar (1, 1), (2, 3), (4, 3), (4, 5).
# Birinci bileşenler {1, 2, 4}, ikinci bileşenler {1, 3, 5}; en küçük A×B 3 · 3 = 9 elemanlı.
fig, ax = sekil(4.6, 4.2)
eksenler(ax, x=(-0.3, 5.2), y=(-0.3, 6.2), izgara=True)
ax.set_xticks([1, 2, 3, 4, 5]); ax.set_yticks([1, 2, 3, 4, 5, 6])
for p in [(1, 1), (2, 3), (4, 3), (4, 5)]:
    nokta(ax, *p, renk=KIRMIZI)
kaydet(fig, __file__)
