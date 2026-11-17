import sys; sys.path.insert(0, "tools")
from cizim import *

# 120 cm tel, bir ucundan 1/5'i (24 cm) kesiliyor. Orta nokta 60'tan 72'ye kayar: 12 cm = kesilenin yarısı.
fig, ax = sekil(6.2, 2.8)
ax.axis("off")
L, k = 120, 24
y1, y2 = 1.6, 0.0
ax.plot([0, L], [y1, y1], color=MAVI, lw=5, solid_capstyle="butt")
ax.plot([0, k], [y2, y2], color=KIRMIZI, lw=5, solid_capstyle="butt", alpha=0.35)
ax.plot([k, L], [y2, y2], color=MAVI, lw=5, solid_capstyle="butt")
ax.text(-3, y1, "önce", ha="right", va="center", fontsize=12, color=YAZI)
ax.text(-3, y2, "sonra", ha="right", va="center", fontsize=12, color=YAZI)
for xm, y, ad in ((L / 2, y1, "orta"), ((k + L) / 2, y2, "yeni orta")):
    ax.plot([xm, xm], [y - 0.28, y + 0.28], color=YAZI, lw=2)
    ax.text(xm, y + 0.38, ad, ha="center", va="bottom", fontsize=11, color=YAZI)
ax.text(k / 2, y2 - 0.35, "kesilen 24 cm", ha="center", va="top", fontsize=11, color=KIRMIZI)
ax.text(0.8 * L, y1 - 0.35, "120 cm", ha="center", va="top", fontsize=11, color=MAVI)
# kayma
ax.plot([L / 2, L / 2], [y1 - 0.3, y2 - 0.75], color=SOLUK, lw=1, ls="--")
ax.plot([(k + L) / 2] * 2, [y2 - 0.3, y2 - 0.75], color=SOLUK, lw=1, ls="--")
ax.annotate("", xy=(L / 2, y2 - 0.7), xytext=((k + L) / 2, y2 - 0.7), arrowprops=dict(arrowstyle="<->", color=YESIL, lw=1.5))
ax.text((L / 2 + (k + L) / 2) / 2, y2 - 0.85, "12 cm kayma", ha="center", va="top", fontsize=11, color=YESIL, fontweight="bold")
ax.set_xlim(-22, L + 2); ax.set_ylim(-1.5, 2.4)
kaydet(fig, __file__)
