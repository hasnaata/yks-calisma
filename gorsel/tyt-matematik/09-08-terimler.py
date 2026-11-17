import sys; sys.path.insert(0, "tools")
from cizim import *

# (x + y)^4 açılımının 5 terimi: katsayı Pascal'ın 4. satırından, x'in üssü azalır, y'nin üssü artar.
fig, ax = sekil(6.4, 3.3)
ax.axis("off")
kats = [1, 4, 6, 4, 1]
terim = ["$x^4$", "$x^3y$", "$x^2y^2$", "$xy^3$", "$y^4$"]
w, h, ara = 1.1, 1.25, 0.18
for i in range(5):
    x0 = i * (w + ara)
    renk, acik = (YESIL, YESIL_ACIK) if i == 2 else (MAVI, MAVI_ACIK)
    ax.add_patch(patches.FancyBboxPatch((x0, 0), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                        facecolor=acik, edgecolor=renk, lw=1.6))
    ax.text(x0 + w / 2, h + 0.22, f"{i + 1}. terim", ha="center", va="bottom", fontsize=11, color=SOLUK)
    ax.text(x0 + w / 2, h - 0.33, str(kats[i]), ha="center", va="center", fontsize=17, color=renk, fontweight="bold")
    ax.text(x0 + w / 2, 0.38, terim[i], ha="center", va="center", fontsize=14, color=YAZI)
    ax.text(x0 + w / 2, -0.32, f"r = {i}", ha="center", va="center", fontsize=11.5, color=SARI)
    ax.text(x0 + w / 2, -0.78, f"{4 - i} + {i} = 4", ha="center", va="center", fontsize=11, color=SOLUK)
ax.text(-0.12, -0.32, "", ha="right")
ax.set_xlim(-0.1, 5 * w + 4 * ara + 0.1); ax.set_ylim(-1.05, h + 0.6)
kaydet(fig, __file__)
