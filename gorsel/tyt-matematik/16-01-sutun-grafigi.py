import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: 20 öğrencinin kardeş sayısı. 0:3, 1:8, 2:6, 3:2, 4:1.
x = [0, 1, 2, 3, 4]; f = [3, 8, 6, 2, 1]
fig, ax = sekil(5.4, 3.6)
ax.bar(x, f, width=0.6, color=[MAVI if v == 8 else MAVI_ACIK for v in f], edgecolor=MAVI, lw=1.4, zorder=3)
for xi, fi in zip(x, f):
    ax.text(xi, fi + 0.2, str(fi), ha="center", va="bottom", fontsize=13, color=YAZI)
ax.set_xticks(x); ax.set_yticks(range(0, 10, 2)); ax.set_ylim(0, 9.5)
ax.set_xlabel("Kardeş sayısı"); ax.set_ylabel("Öğrenci sayısı")
for k in ("top", "right"): ax.spines[k].set_visible(False)
ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
kaydet(fig, __file__)
