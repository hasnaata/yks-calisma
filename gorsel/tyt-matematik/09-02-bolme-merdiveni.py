import sys; sys.path.insert(0, "tools")
from cizim import *

# 40! içindeki 2 çarpanı: 40'ı bölüm 2'den küçük olana kadar 2'ye böl, bölümleri topla.
fig, ax = sekil(6, 3.6)
ax.axis("off"); ax.set_aspect("equal")
sayilar = [40, 20, 10, 5, 2, 1]
dx, dy = 1.05, -0.78
for i, s in enumerate(sayilar):
    x, y = i * dx, i * dy
    bolum = i > 0
    if bolum:
        ax.add_patch(patches.Circle((x + 0.18, y - 0.02), 0.3, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.4))
    ax.text(x + 0.18, y - 0.02, str(s), ha="center", va="center", fontsize=14,
            color=SARI if bolum else YAZI, fontweight="bold" if bolum else "normal")
    if i < len(sayilar) - 1:
        # bölme çizgisi: dikey + yatay
        ax.plot([x + 0.55, x + 0.55], [y + 0.25, y - 0.3], color=SOLUK, lw=1.3)
        ax.plot([x + 0.55, x + 1.2], [y - 0.3, y - 0.3], color=SOLUK, lw=1.3)
        ax.text(x + 0.8, y - 0.02, "2", ha="center", va="center", fontsize=13, color=MAVI)
ax.text(2.6, -4.75, "20 + 10 + 5 + 2 + 1 = 38", ha="center", va="center", fontsize=15, color=YESIL, fontweight="bold")
ax.text(5.3, -0.1, "Bölüm 2'den küçük\nolunca dur.", ha="center", va="center", fontsize=11, color=SOLUK)
ax.set_xlim(-0.4, 6.6); ax.set_ylim(-5.1, 0.45)
kaydet(fig, __file__)
