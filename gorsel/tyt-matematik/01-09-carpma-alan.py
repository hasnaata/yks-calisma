import sys; sys.path.insert(0, "tools")
from cizim import *

# 2/3 · 3/4 alan modeli: birim kare 4 sütun, 3 satır; ortak bölge 6/12 = 1/2.
fig, ax = sekil(5, 4.6)
ax.axis("off"); ax.set_aspect("equal")
S = 4.0
for i in range(4):
    for j in range(3):
        x, y = i * S / 4, j * S / 3
        mavi, yesil = i < 3, j < 2
        renk = "#cfe0f7" if mavi and not yesil else (YESIL_ACIK if yesil and not mavi else ("#b9d9c4" if mavi and yesil else "white"))
        ax.add_patch(patches.Rectangle((x, y), S / 4, S / 3, facecolor=renk, edgecolor=CIZGI, lw=1))
ax.add_patch(patches.Rectangle((0, 0), S, S, fill=False, edgecolor=YAZI, lw=2))
ax.add_patch(patches.Rectangle((0, 0), 3 * S / 4, 2 * S / 3, fill=False, edgecolor=KIRMIZI, lw=2.6))
# üst ölçü: 3/4
ax.annotate("", xy=(3 * S / 4, S + 0.3), xytext=(0, S + 0.3), arrowprops=dict(arrowstyle="<->", color=MAVI, lw=1.4))
ax.text(3 * S / 8, S + 0.45, r"$\frac{3}{4}$", ha="center", va="bottom", fontsize=16, color=MAVI)
# sol ölçü: 2/3
ax.annotate("", xy=(-0.3, 2 * S / 3), xytext=(-0.3, 0), arrowprops=dict(arrowstyle="<->", color=YESIL, lw=1.4))
ax.text(-0.45, S / 3, r"$\frac{2}{3}$", ha="right", va="center", fontsize=16, color=YESIL)
ax.text(3 * S / 8, S / 3, r"$\frac{6}{12}$", ha="center", va="center", fontsize=20, color=KIRMIZI)
ax.text(S / 2, -0.35, "bütün: 3 · 4 = 12 küçük kare", ha="center", va="top", fontsize=12, color=SOLUK)
ax.set_xlim(-1.2, S + 0.2); ax.set_ylim(-1.0, S + 1.2)
kaydet(fig, __file__)
