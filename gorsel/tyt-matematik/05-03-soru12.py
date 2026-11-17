import sys; sys.path.insert(0, "tools")
from cizim import *

# 1. terazi: 2 küp = 1 top + 300 g.  2. terazi: 1 küp + 1 top = 900 g.  (küp 400 g, top 500 g)
fig, ax = sekil(6.8, 2.8)
ax.axis("off"); ax.set_aspect("equal")

def kup(x, y):
    ax.add_patch(patches.Rectangle((x - 0.25, y), 0.5, 0.5, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))

def top(x, y):
    ax.add_patch(patches.Circle((x, y + 0.27), 0.27, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.4))

def agirlik(x, y, yazi):
    ax.add_patch(patches.Polygon([(x - 0.5, y), (x + 0.5, y), (x + 0.4, y + 0.55), (x - 0.4, y + 0.55)],
                                 closed=True, facecolor="#ecebe7", edgecolor=SOLUK, lw=1.3))
    ax.text(x, y + 0.26, yazi, ha="center", va="center", fontsize=10.5, color=YAZI)

def terazi(cx, baslik):
    ax.add_patch(patches.Polygon([(cx - 0.35, 0), (cx + 0.35, 0), (cx, 0.9)], closed=True,
                                 facecolor="#ecebe7", edgecolor=SOLUK, lw=1.3))
    ax.plot([cx - 1.55, cx + 1.55], [0.9, 0.9], color=YAZI, lw=2)
    for s in (-1, 1):
        ax.plot([cx + s * 1.55, cx + s * 1.55], [0.9, 1.05], color=YAZI, lw=1.4)
        ax.plot([cx + s * 1.55 - 0.82, cx + s * 1.55 + 0.82], [1.05, 1.05], color=YAZI, lw=2.4)
    ax.text(cx, -0.3, baslik, ha="center", va="top", fontsize=12, color=SOLUK)
    return cx - 1.55, cx + 1.55, 1.07

sol, sag, y = terazi(0, "1. terazi")
kup(sol - 0.3, y); kup(sol + 0.3, y)
top(sag - 0.46, y); agirlik(sag + 0.27, y, "300 g")
sol, sag, y = terazi(5.6, "2. terazi")
kup(sol - 0.3, y); top(sol + 0.32, y)
agirlik(sag, y, "900 g")
ax.set_xlim(-2.45, 8.05); ax.set_ylim(-0.75, 1.75)
kaydet(fig, __file__)
