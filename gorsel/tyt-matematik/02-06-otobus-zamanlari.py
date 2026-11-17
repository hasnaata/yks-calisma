import sys; sys.path.insert(0, "tools")
from cizim import *

# 12, 15 ve 20 dakikada bir kalkan otobüsler; ortak kalkış EKOK = 60. dakikada.
fig, ax = sekil(6.4, 3.4)
ax.axis("off")
satirlar = [(12, MAVI, 2.0), (15, YESIL, 1.0), (20, SARI, 0.0)]
for p, renk, y in satirlar:
    ax.plot([0, 63], [y, y], color=CIZGI, lw=1.2)
    ax.text(-2.5, y, f"{p} dk", ha="right", va="center", fontsize=13, color=renk, fontweight="bold")
    for t in range(0, 61, p):
        ax.plot(t, y, "o", color=renk, markersize=9, zorder=4)
        if 0 < t < 60: ax.text(t, y + 0.22, str(t), ha="center", va="bottom", fontsize=11, color=renk)
ax.add_patch(patches.Rectangle((-2, -0.45), 4, 3.1, facecolor="none", edgecolor=KIRMIZI, lw=1.8, zorder=5))
ax.add_patch(patches.Rectangle((58, -0.45), 4, 3.1, facecolor="none", edgecolor=KIRMIZI, lw=1.8, zorder=5))
for t, s in [(0, "08.00"), (60, "09.00")]:
    ax.text(t, -0.75, s, ha="center", va="top", fontsize=13, color=KIRMIZI, fontweight="bold")
ax.text(30, -0.75, "dakika: noktaların üstünde", ha="center", va="top", fontsize=11, color=SOLUK)
ax.set_xlim(-11, 65); ax.set_ylim(-1.5, 3.2)
kaydet(fig, __file__)
