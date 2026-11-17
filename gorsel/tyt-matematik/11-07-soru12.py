import sys; sys.path.insert(0, "tools")
from cizim import *

# Aylık üretim (bin adet). f: 2, 4, 7, 5, 6, 1. g: 3, 5, 2, 4, 5, 8.
# f + g: 5, 9, 9, 9, 11, 9 -> en büyük 5. ayda. f en büyük 3. ayda, g en büyük 6. ayda.
ay = np.arange(1, 7)
f = [2, 4, 7, 5, 6, 1]; g = [3, 5, 2, 4, 5, 8]
fig, ax = sekil(5.8, 4)
ax.set_xlim(0.5, 6.5); ax.set_ylim(0, 9)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.grid(True, color=CIZGI, linewidth=0.6, alpha=0.7); ax.set_axisbelow(True)
ax.set_xticks(ay); ax.set_yticks(range(0, 10))
ax.plot(ay, f, "-o", color=MAVI, markersize=6, label="A fabrikası: f")
ax.plot(ay, g, "--s", color=SARI, markersize=6, label="B fabrikası: g")
ax.set_xlabel("Ay"); ax.set_ylabel("Üretim (bin adet)")
ax.legend(loc="upper left", frameon=False, fontsize=11)
kaydet(fig, __file__)
