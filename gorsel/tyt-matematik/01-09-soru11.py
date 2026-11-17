import sys; sys.path.insert(0, "tools")
from cizim import *

# 1/3 ile 3/4 arası 5 eş parça; K, L, M, N bölme noktaları (K = 5/12 ... N = 2/3). Ölçekli.
fig, ax = sekil(6, 1.9)
a, b = 1 / 3, 3 / 4
ax.set_xlim(0.26, 0.82); ax.set_ylim(-0.6, 0.5); ax.axis("off")
ax.annotate("", xy=(0.81, 0), xytext=(0.27, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
adim = (b - a) / 5
for k in range(6):
    x = a + k * adim
    ax.plot([x, x], [-0.06, 0.06], color=SOLUK, lw=1.2)
    if 1 <= k <= 4:
        nokta(ax, x, 0, renk=MAVI)
        ax.text(x, 0.14, "KLMN"[k - 1], ha="center", va="bottom", fontsize=14, color=MAVI)
ax.text(a, -0.14, r"$\dfrac{1}{3}$", ha="center", va="top", fontsize=16)
ax.text(b, -0.14, r"$\dfrac{3}{4}$", ha="center", va="top", fontsize=16)
kaydet(fig, __file__)
