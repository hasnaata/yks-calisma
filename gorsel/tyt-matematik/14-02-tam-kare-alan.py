import sys; sys.path.insert(0, "tools")
from cizim import *

# (a + b)^2 = a^2 + 2ab + b^2 alan modeli. a = 3, b = 1,3 birim (orantılı çizim).
A, B = 3.0, 1.3
fig, ax = sekil(5, 4.6)
ax.axis("off"); ax.set_aspect("equal")
parcalar = [  # (x0, y0, genişlik, yükseklik, dolgu, kenar, yazı)
    (0, 0, A, A, MAVI_ACIK, MAVI, r"$a^2$"),
    (A, 0, B, A, YESIL_ACIK, YESIL, r"$ab$"),
    (0, A, A, B, YESIL_ACIK, YESIL, r"$ab$"),
    (A, A, B, B, SARI_ACIK, SARI, r"$b^2$"),
]
for x0, y0, g, h, dolgu, kenar, yazi in parcalar:
    ax.add_patch(patches.Rectangle((x0, y0), g, h, facecolor=dolgu, edgecolor=kenar, lw=2))
    ax.text(x0 + g / 2, y0 + h / 2, yazi, ha="center", va="center", fontsize=20, color=kenar)
# kenar uzunlukları
ax.text(A / 2, -0.25, "a", ha="center", va="top", fontsize=16)
ax.text(A + B / 2, -0.25, "b", ha="center", va="top", fontsize=16)
ax.text(-0.25, A / 2, "a", ha="right", va="center", fontsize=16)
ax.text(-0.25, A + B / 2, "b", ha="right", va="center", fontsize=16)
ax.annotate("", xy=(A + B, A + B + 0.35), xytext=(0, A + B + 0.35), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.3))
ax.text((A + B) / 2, A + B + 0.5, "a + b", ha="center", va="bottom", fontsize=15)
ax.set_xlim(-0.8, A + B + 0.3); ax.set_ylim(-0.8, A + B + 1.1)
kaydet(fig, __file__)
