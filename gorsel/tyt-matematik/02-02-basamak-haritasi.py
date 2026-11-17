import sys; sys.path.insert(0, "tools")
from cizim import *

# Hangi bölen için sayının hangi basamaklarına bakılır?
RAKAMLAR = "573928"
fig, ax = sekil(6, 4.4)
ax.set_xlim(-0.2, 9.6); ax.set_ylim(-4.3, 2.2); ax.axis("off"); ax.set_aspect("equal")
n = len(RAKAMLAR)
for i, r in enumerate(RAKAMLAR):
    ax.add_patch(patches.FancyBboxPatch((i + 0.08, 0.08), 0.84, 0.84, boxstyle="round,pad=0.02",
                 facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))
    ax.text(i + 0.5, 0.5, r, ha="center", va="center", fontsize=20, color=YAZI)

def parantez(x0, x1, y, renk, yazi, yukari=False):
    d = 0.18 if yukari else -0.18
    ax.plot([x0, x0, x1, x1], [y - d, y, y, y - d], color=renk, lw=2)
    ax.text(x1 + 0.25, y, yazi, ha="left", va="center", color=renk, fontsize=13)

# Üstte: bütün basamaklar
parantez(0.05, n - 0.05, 1.35, YESIL, "Rakam toplamı: 3, 9", yukari=True)
ax.text(n + 0.25, 1.85, "İşaretli toplam: 11", ha="left", va="center", color=YESIL, fontsize=13)
# Altta: son basamaklar
parantez(n - 1 + 0.08, n - 0.08, -0.45, KIRMIZI, "Son 1 basamak: 2, 5, 10")
parantez(n - 2 + 0.08, n - 0.08, -1.45, SARI, "Son 2 basamak: 4")
parantez(n - 3 + 0.08, n - 0.08, -2.45, MAVI, "Son 3 basamak: 8")
kaydet(fig, __file__)
