import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 5: A = {1, 3, 4}, B = {2, 3}; A×B grafiği (6 nokta). A∪B = {1, 2, 3, 4}, s = 4.
fig, ax = sekil(4.6, 3.4)
eksenler(ax, x=(-0.3, 5.2), y=(-0.3, 4.2), izgara=True)
ax.set_xticks([1, 2, 3, 4, 5]); ax.set_yticks([1, 2, 3, 4])
for a in (1, 3, 4):
    for b in (2, 3):
        nokta(ax, a, b, renk=KIRMIZI)
kaydet(fig, __file__)
