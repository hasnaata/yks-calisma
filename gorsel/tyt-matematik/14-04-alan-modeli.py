import sys; sys.path.insert(0, "tools")
from cizim import *

# x^2 + 5x + 6 = (x + 2)(x + 3) alan modeli. x = 3 birim, sabitler orantılı.
X = 3.0
fig, ax = sekil(5, 4.4)
ax.axis("off"); ax.set_aspect("equal")
parcalar = [  # (x0, y0, genişlik, yükseklik, dolgu, kenar, yazı)
    (0, 0, X, X, MAVI_ACIK, MAVI, r"$x^2$"),
    (X, 0, 3, X, YESIL_ACIK, YESIL, r"$3x$"),
    (0, X, X, 2, YESIL_ACIK, YESIL, r"$2x$"),
    (X, X, 3, 2, SARI_ACIK, SARI, r"$6$"),
]
for x0, y0, g, h, dolgu, kenar, yazi in parcalar:
    ax.add_patch(patches.Rectangle((x0, y0), g, h, facecolor=dolgu, edgecolor=kenar, lw=2))
    ax.text(x0 + g / 2, y0 + h / 2, yazi, ha="center", va="center", fontsize=22, color=kenar)
ax.text(X / 2, -0.25, "x", ha="center", va="top", fontsize=16)
ax.text(X + 1.5, -0.25, "3", ha="center", va="top", fontsize=16)
ax.text(-0.25, X / 2, "x", ha="right", va="center", fontsize=16)
ax.text(-0.25, X + 1, "2", ha="right", va="center", fontsize=16)
ax.annotate("", xy=(X + 3, X + 2.35), xytext=(0, X + 2.35), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.3))
ax.text((X + 3) / 2, X + 2.5, "x + 3", ha="center", va="bottom", fontsize=15)
ax.annotate("", xy=(X + 3.35, X + 2), xytext=(X + 3.35, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.3))
ax.text(X + 3.5, (X + 2) / 2, "x + 2", ha="left", va="center", fontsize=15)
ax.set_xlim(-0.8, X + 4.7); ax.set_ylim(-0.8, X + 3.2)
kaydet(fig, __file__)
