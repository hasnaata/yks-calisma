import sys; sys.path.insert(0, "tools")
from cizim import *

# 3/4 : 1/8 = 6 — 3/4 uzunluğuna 1/8'lik kaç adım sığar?
fig, ax = sekil(6, 2.6)
ax.set_xlim(-0.06, 1.06); ax.set_ylim(-0.75, 0.75); ax.axis("off")
ax.annotate("", xy=(1.05, 0), xytext=(-0.05, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
for k in range(9):
    x = k / 8
    ax.plot([x, x], [-0.04, 0.04], color=SOLUK, lw=1.2)
etiket = {0: "0", 2: r"$\dfrac{1}{4}$", 4: r"$\dfrac{1}{2}$", 6: r"$\dfrac{3}{4}$", 8: "1"}
for k, t in etiket.items():
    ax.text(k / 8, -0.1, t, ha="center", va="top", fontsize=13, color=KIRMIZI if k == 6 else YAZI)
ax.plot([0, 0.75], [0, 0], color=KIRMIZI, lw=4, solid_capstyle="butt", zorder=3)
for k in range(6):
    a, b = k / 8, (k + 1) / 8
    ax.annotate("", xy=(b, 0.06), xytext=(a, 0.06),
                arrowprops=dict(arrowstyle="->", color=MAVI, lw=1.6, connectionstyle="arc3,rad=-0.6"))
    ax.text((a + b) / 2, 0.22, str(k + 1), ha="center", va="bottom", fontsize=13, color=MAVI)
ax.text(0.375, 0.5, r"her adım $\dfrac{1}{8}$", ha="center", va="bottom", fontsize=12, color=MAVI)
kaydet(fig, __file__)
