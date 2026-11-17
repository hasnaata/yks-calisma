import sys; sys.path.insert(0, "tools")
from cizim import *

# İki tek sayının toplamı: 5 ve 7 ikişerli sütunlara dizilir; artan birer nokta toplamda yeni bir çift oluşturur.
fig, ax = sekil(6, 3.6)
ax.axis("off"); ax.set_aspect("equal")
def sutunlar(x0, y0, cift, renk, artik=None):
    for i in range(cift):
        for j in range(2):
            ax.add_patch(patches.Circle((x0 + i * 0.55, y0 + j * 0.55), 0.18, facecolor=renk, edgecolor="none"))
    if artik:
        ax.add_patch(patches.Circle((x0 + cift * 0.55, y0), 0.18, facecolor=artik, edgecolor="none"))
# üst satır: 5 ve 7
sutunlar(0.0, 3.0, 2, MAVI, KIRMIZI)
ax.text(0.55, 2.45, "5 = 2·2 + 1", ha="center", va="top", fontsize=12)
sutunlar(3.4, 3.0, 3, SARI, KIRMIZI)
ax.text(4.2, 2.45, "7 = 2·3 + 1", ha="center", va="top", fontsize=12)
ax.text(2.35, 3.25, "+", ha="center", va="center", fontsize=20, color=SOLUK)
ax.annotate("", xy=(3.2, 1.55), xytext=(3.2, 2.0), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.5))
# alt satır: 12 = 6 çift
sutunlar(0.6, 0.35, 2, MAVI); sutunlar(0.6 + 2 * 0.55, 0.35, 3, SARI)
xk = 0.6 + 5 * 0.55
for j in range(2):
    ax.add_patch(patches.Circle((xk, 0.35 + j * 0.55), 0.18, facecolor=KIRMIZI, edgecolor="none"))
ax.add_patch(patches.FancyBboxPatch((xk - 0.3, 0.05), 0.6, 1.15, boxstyle="round,pad=0,rounding_size=0.2", facecolor="none", edgecolor=KIRMIZI, lw=1.4, ls="--"))
ax.text(xk + 0.55, 0.62, "iki artık\nbir çift olur", ha="left", va="center", fontsize=11, color=KIRMIZI)
ax.text(3.2, -0.25, "5 + 7 = 2·(2 + 3 + 1) = 12", ha="center", va="top", fontsize=12)
ax.set_xlim(-0.4, 6.4); ax.set_ylim(-0.8, 3.9)
kaydet(fig, __file__)
