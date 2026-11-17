import sys; sys.path.insert(0, "tools")
from cizim import *

# Kutu: yükseklik 10 cm, genişlik 15 cm. Rampa P=(0,0)'dan başlar, eğim 2/3.
# Yığınlar 2, 4, 7 kutu; sol üst köşeleri x = 30, 60, 105'te: 20, 40, 70 cm yükseklikte.
# Yığın arası (köşeler arası yatay) 30 cm ve a = 45 cm.
h, w, m = 10, 15, 2 / 3
yiginlar = [(30, 2), (60, 4), (105, 7)]
for x0, n in yiginlar: print(n, "kutu, rampa yüksekliği", m * x0, "yığın", n * h)
fig, ax = sekil(5.8, 4.0)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-5, 128], [0, 0], color=SOLUK, lw=1.2)
for x0, n in yiginlar:
    for i in range(n):
        ax.add_patch(patches.Rectangle((x0, i * h), w, h, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.2))
    ax.text(x0 + w / 2, -5, f"{n} kutu", ha="center", va="center", fontsize=11, color=SARI)
ax.plot([0, 118], [0, m * 118], color=MAVI, lw=3)
for x0, n in yiginlar: nokta(ax, x0, n * h, renk=MAVI)
# yatay ölçü çizgileri: köşelerden yukarı kesikli çizgi, üstte oklu ölçü
for x0, n in yiginlar: ax.plot([x0, x0], [n * h, 90], color=SOLUK, lw=0.9, ls=":")
for xa, xb, t in [(30, 60, "30 cm"), (60, 105, "a")]:
    ax.annotate("", xy=(xb, 88), xytext=(xa, 88), arrowprops=dict(arrowstyle="<->", color=YAZI, lw=1.2))
    ax.text((xa + xb) / 2, 92.5, t, ha="center", va="center", fontsize=12)
nokta(ax, 0, 0, "P", dx=-4, dy=-7)
ax.set_xlim(-6, 128); ax.set_ylim(-10, 97)
kaydet(fig, __file__)
