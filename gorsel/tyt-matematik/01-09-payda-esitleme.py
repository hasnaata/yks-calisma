import sys; sys.path.insert(0, "tools")
from cizim import *

# 1/2 + 1/3: önce iki şerit kendi paydasıyla, sonra ikisi de altıda birlere bölünür; toplam 5/6.
fig, ax = sekil(6, 4.2)
ax.axis("off"); ax.set_aspect("equal")
G = 6.0  # bir bütünün genişliği

def serit(y, parca, dolu, renk, acik, etiket):
    for i in range(parca):
        w = G / parca
        ax.add_patch(patches.Rectangle((i * w, y), w, 0.8, facecolor=acik if i < dolu else "white",
                                       edgecolor=renk if i < dolu else SOLUK, lw=1.6))
    ax.text(-0.3, y + 0.4, etiket, ha="right", va="center", fontsize=15, color=renk)

serit(4.2, 2, 1, MAVI, MAVI_ACIK, r"$\frac{1}{2}$")
serit(3.0, 3, 1, YESIL, YESIL_ACIK, r"$\frac{1}{3}$")
serit(1.4, 6, 3, MAVI, MAVI_ACIK, r"$\frac{3}{6}$")
serit(0.2, 6, 2, YESIL, YESIL_ACIK, r"$\frac{2}{6}$")
ax.text(G / 2, 2.55, "ikisini de altıda birlere böl", ha="center", va="center", fontsize=12, color=SOLUK)
# toplam şeridi
for i in range(6):
    w = G / 6
    renk, acik = (MAVI, MAVI_ACIK) if i < 3 else ((YESIL, YESIL_ACIK) if i < 5 else (SOLUK, "white"))
    ax.add_patch(patches.Rectangle((i * w, -1.4), w, 0.8, facecolor=acik, edgecolor=renk, lw=1.6))
ax.text(-0.3, -1.0, r"$\frac{5}{6}$", ha="right", va="center", fontsize=15, color=YAZI)
ax.text(G / 2, -0.35, "topla", ha="center", va="center", fontsize=12, color=SOLUK)
ax.set_xlim(-1.3, 6.2); ax.set_ylim(-1.6, 5.2)
kaydet(fig, __file__)
