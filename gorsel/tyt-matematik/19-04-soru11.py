import sys; sys.path.insert(0, "tools")
from cizim import *

# Kutu: yükseklik 8 cm, genişlik 10 cm. Rampa P=(0,0), eğim 2/3.
# 1 kutuluk yığının köşesi x=12 (8 cm), 3 kutuluk x=36 (24 cm), en yüksek yığın x=72 (48 cm = 6 kutu).
h, w, m = 8, 10, 2 / 3
for x0, n in [(12, 1), (36, 3), (72, 6)]: print(n, m * x0, n * h)
fig, ax = sekil(5.4, 3.9)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-4, 88], [0, 0], color=SOLUK, lw=1.2)
for x0, n in [(12, 1), (36, 3)]:
    for i in range(n):
        ax.add_patch(patches.Rectangle((x0, i * h), w, h, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.2))
ax.add_patch(patches.Rectangle((72, 0), w, 48, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.2, hatch="..."))
ax.text(77, 24, "?", ha="center", va="center", fontsize=16, color=SARI,
        bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none"))
ax.plot([0, 80], [0, m * 80], color=MAVI, lw=3)
for x0, n in [(12, 1), (36, 3), (72, 6)]:
    nokta(ax, x0, n * h, renk=MAVI); ax.plot([x0, x0], [n * h, 60], color=SOLUK, lw=0.9, ls=":")
for xa, xb, t in [(12, 36, "24 cm"), (36, 72, "36 cm")]:
    ax.annotate("", xy=(xb, 58), xytext=(xa, 58), arrowprops=dict(arrowstyle="<->", color=YAZI, lw=1.2))
    ax.text((xa + xb) / 2, 62.5, t, ha="center", va="center", fontsize=12)
ax.set_xlim(-4, 88); ax.set_ylim(-3, 66)
kaydet(fig, __file__)
