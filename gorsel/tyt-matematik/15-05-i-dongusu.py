import sys; sys.path.insert(0, "tools")
from cizim import *

fig, ax = sekil(5.2, 4.6)
ax.axis("off"); ax.set_aspect("equal")
ax.set_xlim(-3.3, 3.3); ax.set_ylim(-2.9, 2.9)
R = 1.75
ax.add_patch(patches.Circle((0, 0), R, fill=False, edgecolor=CIZGI, lw=1.5, ls="--"))
# saat yönünde: üst i^0, sağ i^1, alt i^2, sol i^3
yer = [(0, R, "i⁰ = 1", "n = 4k", MAVI), (R, 0, "i¹ = i", "n = 4k + 1", YESIL),
       (0, -R, "i² = −1", "n = 4k + 2", KIRMIZI), (-R, 0, "i³ = −i", "n = 4k + 3", SARI)]
for x, y, t, alt, r in yer:
    ax.add_patch(patches.FancyBboxPatch((x - 0.95, y - 0.42), 1.9, 0.84, boxstyle="round,pad=0,rounding_size=0.18",
                                        facecolor="white", edgecolor=r, lw=2, zorder=4))
    ax.text(x, y + 0.12, t, ha="center", va="center", fontsize=14, color=r, fontweight="bold", zorder=5)
    ax.text(x, y - 0.22, alt, ha="center", va="center", fontsize=10.5, color=SOLUK, zorder=5)
# oklar (saat yönü)
import numpy as np
for a1, a2 in [(80, 10), (-10, -80), (-100, -170), (170, 100)]:
    t1, t2 = np.radians(a1), np.radians(a2)
    ax.annotate("", xy=(R * 1.33 * np.cos(t2), R * 1.33 * np.sin(t2)), xytext=(R * 1.33 * np.cos(t1), R * 1.33 * np.sin(t1)),
                arrowprops=dict(arrowstyle="->", color=MAVI, lw=1.6, connectionstyle="arc3,rad=-0.35"))
for a in (45, -45, -135, 135):
    t = np.radians(a)
    ax.text(R * 1.62 * np.cos(t), R * 1.62 * np.sin(t), "× i", ha="center", va="center", color=MAVI, fontsize=12)
ax.text(0, 0, "4 adımda\nbaşa döner", ha="center", va="center", color=SOLUK, fontsize=11)
kaydet(fig, __file__)
