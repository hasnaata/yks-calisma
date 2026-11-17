import sys; sys.path.insert(0, "tools")
from cizim import *

# Tam sayılar sayı doğrusunda sırayla bir çift, bir tek gelir; 0 çifttir.
fig, ax = sekil(6, 1.9)
sayi_dogrusu(ax, -5, 6)
for t in range(-5, 7):
    renk = MAVI if t % 2 == 0 else KIRMIZI
    ax.plot(t, 0, "o", color=renk, markersize=10, zorder=5)
    ax.text(t, 0.38, "Ç" if t % 2 == 0 else "T", ha="center", va="center", fontsize=14,
            color=renk, fontweight="bold")
ax.text(-5.5, 0.95, "Ç: çift", color=MAVI, fontsize=13, ha="left", va="center")
ax.text(-2.6, 0.95, "T: tek", color=KIRMIZI, fontsize=13, ha="left", va="center")
ax.set_ylim(-0.85, 1.15)
kaydet(fig, __file__)
