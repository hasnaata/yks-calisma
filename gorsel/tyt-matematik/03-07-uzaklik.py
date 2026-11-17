import sys; sys.path.insert(0, "tools")
from cizim import *

# Üst: |−5| = 5 ve |2| = 2 (sıfıra uzaklık). Alt: −2 ile 4 arası |−2 − 4| = 6 birim.
LO, HI = -6, 6
fig, eks = plt.subplots(2, 1, figsize=(6, 3.4))

def kemer(ax, a, b, yazi, renk, y=0.42):
    ax.annotate("", xy=(b, y), xytext=(a, y), arrowprops=dict(arrowstyle="<->", color=renk, lw=2))
    ax.plot([a, a], [0.08, y + 0.08], color=renk, lw=1.2); ax.plot([b, b], [0.08, y + 0.08], color=renk, lw=1.2)
    ax.text((a + b) / 2, y + 0.14, yazi, ha="center", va="bottom", color=renk, fontsize=13)

ax = eks[0]
sayi_dogrusu(ax, LO, HI); ax.set_ylim(-0.9, 1.25)
kemer(ax, -5, 0, "|−5| = 5", KIRMIZI)
kemer(ax, 0, 2, "|2| = 2", MAVI)
for t, r in ((-5, KIRMIZI), (0, YAZI), (2, MAVI)): ax.plot(t, 0, "o", color=r, markersize=8, zorder=5)

ax = eks[1]
sayi_dogrusu(ax, LO, HI); ax.set_ylim(-0.9, 1.25)
kemer(ax, -2, 4, "|−2 − 4| = 6 birim", YESIL)
for t in (-2, 4): ax.plot(t, 0, "o", color=YESIL, markersize=8, zorder=5)
fig.subplots_adjust(hspace=0.15)
kaydet(fig, __file__)
