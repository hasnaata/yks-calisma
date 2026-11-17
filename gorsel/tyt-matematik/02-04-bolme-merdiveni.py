import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders: 540'ın bölme merdiveni. 540 = 2^2 · 3^3 · 5
fig, ax = sekil(6, 3.6)
ax.axis("off")
satirlar = [(540, 2), (270, 2), (135, 3), (45, 3), (15, 3), (5, 5), (1, None)]
renk = {2: MAVI, 3: YESIL, 5: SARI}
for i, (n, p) in enumerate(satirlar):
    y = -i
    ax.text(1.6, y, str(n), ha="right", va="center", fontsize=15, color=YAZI)
    if p:
        ax.text(2.0, y, str(p), ha="left", va="center", fontsize=15, color=renk[p], fontweight="bold")
        ax.plot([1.8, 2.7], [y - 0.5, y - 0.5], color=CIZGI, lw=1)
ax.plot([1.8, 1.8], [0.5, -5.5], color=SOLUK, lw=1.6)
# Sağda gruplama
gruplar = [(0, 1, "2 iki kez", MAVI), (2, 4, "3 üç kez", YESIL), (5, 5, "5 bir kez", SARI)]
for a, b, yazi, r in gruplar:
    ax.plot([2.9, 3.05, 3.05, 2.9], [-a + 0.3, -a + 0.3, -b - 0.3, -b - 0.3], color=r, lw=1.6)
    ax.text(3.25, -(a + b) / 2, yazi, ha="left", va="center", fontsize=13, color=r)
ax.text(0.2, -7.2, r"$540 = 2^2 \cdot 3^3 \cdot 5$", ha="left", va="center", fontsize=17, color=YAZI)
ax.set_xlim(0, 6); ax.set_ylim(-7.7, 0.7)
kaydet(fig, __file__)
