import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 11: a < 0 < b ve a, 0'a b'den daha uzak.
fig, ax = sekil(6, 1.2)
ax.set_xlim(-6.6, 4.6); ax.set_ylim(-1, 0.8); ax.axis("off")
ax.annotate("", xy=(4.5, 0), xytext=(-6.5, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
for t, ad in ((-5, "a"), (0, "0"), (2, "b")):
    ax.plot([t, t], [-0.1, 0.1], color=YAZI, lw=1.5)
    ax.text(t, -0.35, ad, ha="center", va="top", fontsize=15, color=YAZI, style="italic" if ad != "0" else "normal")
kaydet(fig, __file__)
