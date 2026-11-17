import sys; sys.path.insert(0, "tools")
from cizim import *

# İki ardışık bölme: birincinin bölümü ikincide bölünen olur.
fig, ax = sekil(6, 3.4)
ax.axis("off"); ax.set_aspect("equal")
B = dict(fontsize=22, fontweight="bold")
def duzen(x, bolunen, bolen, bolum, kalan, renk_bolum):
    ax.text(x, 0, bolunen, ha="right", va="center", color=MAVI, **B)
    ax.plot([x + 0.3, x + 0.3], [0.45, -1.15], color=YAZI, lw=2)
    ax.plot([x + 0.3, x + 1.3], [-0.4, -0.4], color=YAZI, lw=2)
    ax.text(x + 0.55, 0, bolen, ha="left", va="center", color=SARI, **B)
    ax.text(x + 0.55, -0.8, bolum, ha="left", va="center", color=renk_bolum, **B)
    ax.text(x, -1.6, kalan, ha="right", va="center", color=KIRMIZI, **B)
duzen(0.6, "A", "5", "B", "3", YESIL)
duzen(4.6, "B", "4", "C", "2", YESIL)
ax.annotate("", xy=(3.75, 0.05), xytext=(1.9, -0.75),
            arrowprops=dict(arrowstyle="->", color=YESIL, lw=1.8, connectionstyle="arc3,rad=-0.3"))
ax.text(-0.9, -2.6, r"$A = 5B + 3$", fontsize=15, color=YAZI, va="center")
ax.text(3.3, -2.6, r"$B = 4C + 2$", fontsize=15, color=YAZI, va="center")
ax.text(2.6, -3.5, r"$A = 5(4C + 2) + 3 = 20C + 13$", fontsize=15, color=MAVI, ha="center", va="center")
ax.set_xlim(-1.2, 6.6); ax.set_ylim(-3.9, 0.7)
kaydet(fig, __file__)
