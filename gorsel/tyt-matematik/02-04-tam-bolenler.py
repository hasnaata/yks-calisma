import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders: 12'nin tam sayı bölenleri sayı doğrusunda; her bölen negatifiyle eşleşir, toplam 0.
fig, ax = sekil(6.4, 2.4)
bolen = [1, 2, 3, 4, 6, 12]
ax.set_xlim(-13.2, 13.2); ax.set_ylim(-1.9, 3.4); ax.axis("off")
ax.annotate("", xy=(13.1, 0), xytext=(-13.1, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
ax.plot([0, 0], [-0.15, 0.15], color=SOLUK, lw=1.2)
for k, d in enumerate(bolen):
    for x, r in ((d, MAVI), (-d, KIRMIZI)):
        ax.plot(x, 0, "o", color=r, markersize=7, zorder=5)
        alt = -1.05 if d in (2, 4) else -0.45
        if d in (2, 4): ax.plot([x, x], [-0.12, alt + 0.05], color=CIZGI, lw=0.8)
        ax.text(x, alt, str(x).replace("-", "−"), ha="center", va="top", color=r, fontsize=11)
    yuk = 0.45 + 0.45 * k
    ax.add_patch(patches.Arc((0, 0), 2 * d, 2 * yuk, theta1=0, theta2=180, color=CIZGI, lw=1.2))
ax.text(0, 3.15, "Her bölen, negatifiyle toplanınca 0 olur", ha="center", va="center", fontsize=12, color=YAZI)
kaydet(fig, __file__)
