import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: 5 maaş (bin TL) 20, 22, 24, 25, 109. Ortanca 24, ortalama 40.
veri = [20, 22, 24, 25, 109]
fig, ax = sekil(6, 2.6)
ax.set_xlim(8, 120); ax.set_ylim(-1.5, 1.2); ax.axis("off")
ax.annotate("", xy=(118, 0), xytext=(10, 0), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.4))
for t in range(20, 111, 10):
    ax.plot([t, t], [-0.08, 0.08], color=SOLUK, lw=1.2)
    ax.text(t, -0.2, str(t), ha="center", va="top", fontsize=11, color=SOLUK)
for v in veri:
    ax.plot(v, 0.3, "o", color=YAZI if v != 109 else KIRMIZI, markerfacecolor="white" if v != 109 else KIRMIZI,
            mew=1.8, markersize=8, zorder=5)
ax.text(22.5, 0.62, "20, 22, 24, 25", ha="center", fontsize=12, color=YAZI)
ax.text(109, 0.62, "109 (uç değer)", ha="center", fontsize=12, color=KIRMIZI)
ax.plot(24, -0.75, "^", color=YESIL, markersize=12, zorder=5)
ax.text(24, -1.05, "ortanca 24", ha="center", va="top", fontsize=12.5, color=YESIL, fontweight="bold")
ax.plot(40, -0.75, "^", color=MAVI, markersize=12, zorder=5)
ax.text(43, -0.75, "ortalama 40", va="center", fontsize=12.5, color=MAVI, fontweight="bold")
kaydet(fig, __file__)
