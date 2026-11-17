import sys; sys.path.insert(0, "tools")
from cizim import *

# Soru 8: bahçe kenarı a = 9 m, havuz kenarı b = 3 m (ölçekli). a - b = 6, çimli alan 81 - 9 = 72.
A, B = 9.0, 3.0
fig, ax = sekil(4.6, 4.4)
ax.axis("off"); ax.set_aspect("equal")
ax.add_patch(patches.Rectangle((0, 0), A, A, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=2))
ax.add_patch(patches.Rectangle((A - B, A - B), B, B, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=2))
ax.text(A - B / 2, A - B / 2, "Havuz", ha="center", va="center", fontsize=13, color=MAVI)
ax.text(3.6, 3.6, r"Çim" "\n" r"72 m$^2$", ha="center", va="center", fontsize=15, color=YESIL)
# üst kenar parçaları
ax.text((A - B) / 2, A + 0.3, "6 m", ha="center", va="bottom", fontsize=14)
ax.plot([A - B, A - B], [A + 0.1, A + 0.6], color=SOLUK, lw=1.2)
ax.text(-0.3, A / 2, "?", ha="right", va="center", fontsize=14)
ax.set_xlim(-1.2, A + 0.4); ax.set_ylim(-0.4, A + 1.4)
kaydet(fig, __file__)
