import sys; sys.path.insert(0, "tools")
from cizim import *

# %35 = 100 eşit parçanın 35'i. 360 öğrencinin %35'i: her küçük kare 360/100 = 3,6 öğrenci, 35 kare 126 öğrenci.
fig, ax = sekil(5.2, 4.6)
ax.axis("off"); ax.set_aspect("equal")
for k in range(100):
    satir, sutun = divmod(k, 10)
    dolu = k < 35
    ax.add_patch(patches.Rectangle((sutun, 9 - satir), 0.92, 0.92,
                 facecolor=MAVI_ACIK if dolu else "white", edgecolor=MAVI if dolu else CIZGI, lw=1.1))
ax.text(10.4, 8.5, "35 kare\nboyalı", va="center", fontsize=12, color=MAVI)
ax.text(10.4, 4.5, "100 karenin\n35'i = %35", va="center", fontsize=12, color=YAZI)
ax.text(5, -0.5, "360 öğrenci → bir kare 3,6 öğrenci\n35 kare = 35 · 3,6 = 126 öğrenci", ha="center", va="top", fontsize=12, color=YAZI)
ax.set_xlim(-0.2, 14.2); ax.set_ylim(-2.4, 10.1)
kaydet(fig, __file__)
