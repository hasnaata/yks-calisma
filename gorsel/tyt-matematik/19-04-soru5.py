import sys; sys.path.insert(0, "tools")
from cizim import *

# Kutu: yükseklik 15 cm, genişlik 20 cm. Rampa P=(0,0), eğim 1/2.
# 2 kutuluk yığının sol üst köşesi x=60 (30 cm), 5 kutuluk yığınınki x=150 (75 cm). Aradaki yatay uzaklık 90 cm.
h, w, m = 15, 20, 0.5
yiginlar = [(60, 2), (150, 5)]
for x0, n in yiginlar: print(n, "kutu:", m * x0, n * h)
fig, ax = sekil(5.8, 3.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-6, 182], [0, 0], color=SOLUK, lw=1.2)
for x0, n in yiginlar:
    for i in range(n):
        ax.add_patch(patches.Rectangle((x0, i * h), w, h, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.2))
ax.plot([0, 172], [0, m * 172], color=MAVI, lw=3)
for x0, n in yiginlar: nokta(ax, x0, n * h, renk=MAVI); ax.plot([x0, x0], [n * h, 100], color=SOLUK, lw=0.9, ls=":")
ax.plot([0, 0], [0, 100], color=SOLUK, lw=0.9, ls=":")
for xa, xb, t in [(0, 60, "60 cm"), (60, 150, "?")]:
    ax.annotate("", xy=(xb, 97), xytext=(xa, 97), arrowprops=dict(arrowstyle="<->", color=YAZI, lw=1.2))
    ax.text((xa + xb) / 2, 104, t, ha="center", va="center", fontsize=12)
nokta(ax, 0, 0, "P", dx=-6, dy=-11)
ax.set_xlim(-8, 182); ax.set_ylim(-14, 110)
kaydet(fig, __file__)
