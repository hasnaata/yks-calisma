import sys; sys.path.insert(0, "tools")
from cizim import *

# Yan yana kareler: 1 kare 4, 2 kare 7, 3 kare 10 kibrit. Her yeni kare 3 kibrit ekler: 3n + 1.
fig, ax = sekil(6.2, 2.6)
ax.axis("off")

def kibrit(x1, y1, x2, y2, yeni=False):
    renk = KIRMIZI if yeni else SARI
    ax.plot([x1, x2], [y1, y2], color=renk, lw=4, solid_capstyle="round")
    ax.plot(x2, y2, "o", color=KIRMIZI, markersize=5)

bas = [0, 1.6, 4.2]
for n, x0 in zip((1, 2, 3), bas):
    for k in range(n):
        x = x0 + k
        yeni = (k == n - 1 and n > 1)
        kibrit(x, 0, x + 1, 0, yeni); kibrit(x, 1, x + 1, 1, yeni); kibrit(x + 1, 0, x + 1, 1, yeni)
        if k == 0: kibrit(x, 0, x, 1)
    ax.text(x0 + n / 2, -0.3, f"{n}. adım", ha="center", va="top", fontsize=12)
    ax.text(x0 + n / 2, -0.75, f"{3 * n + 1} kibrit", ha="center", va="top", fontsize=13, color=MAVI, fontweight="bold")
ax.text(3.6, 1.45, "Kırmızı: her adımda eklenen 3 kibrit", ha="center", va="bottom", fontsize=12, color=KIRMIZI)
ax.set_xlim(-0.2, 7.4); ax.set_ylim(-1.2, 1.85); ax.set_aspect("equal")
kaydet(fig, __file__)
