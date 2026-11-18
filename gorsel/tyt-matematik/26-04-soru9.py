import sys; sys.path.insert(0, "tools")
from cizim import *

# Soru 9: kenarı 12 cm olan eşkenar üçgen karton; kenar orta noktalarını birleştiren kesikli çizgiler katlama çizgileri.
k = 12
s3 = np.sqrt(3)
P1, P2, P3 = np.array([0, 0.]), np.array([k, 0.]), np.array([k / 2, k * s3 / 2])
M1, M2, M3 = (P1 + P2) / 2, (P2 + P3) / 2, (P1 + P3) / 2
fig, ax = sekil(4.4, 4.0)
ax.add_patch(patches.Polygon((P1, P2, P3), closed=True, facecolor=SARI_ACIK, edgecolor=YAZI, lw=2.2, zorder=2))
for p, q in ((M1, M2), (M2, M3), (M3, M1)):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=SOLUK, lw=1.8, ls=(0, (5, 3)), zorder=3)
for m in (M1, M2, M3):
    ax.plot(m[0], m[1], "o", color=YAZI, markersize=5, zorder=4)
ax.text(k / 2, -0.95, "12 cm", ha="center", va="center", fontsize=13)
ax.text(k * 0.25 - 0.9, k * s3 / 4 + 0.35, "12 cm", ha="center", va="center", fontsize=13, rotation=60)
ax.text(k * 0.75 + 0.9, k * s3 / 4 + 0.35, "12 cm", ha="center", va="center", fontsize=13, rotation=-60)
ax.set_xlim(-1.6, k + 1.6); ax.set_ylim(-1.3, k * s3 / 2 + 0.6)
ax.set_aspect("equal"); ax.axis("off")
kaydet(fig, __file__)
