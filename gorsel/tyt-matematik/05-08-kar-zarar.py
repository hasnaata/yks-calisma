import sys; sys.path.insert(0, "tools")
from cizim import *

# Maliyet 80 TL. Satış 100 TL -> 20 TL kâr; satış 60 TL -> 20 TL zarar; satış 80 TL -> ne kâr ne zarar.
fig, ax = sekil(6.2, 3.6)
ax.axis("off")
durumlar = [("Kâr", 100, YESIL, YESIL_ACIK, "+20 TL kâr"), ("Zarar", 60, KIRMIZI, KIRMIZI_ACIK, "−20 TL zarar"),
            ("Ne kâr ne zarar", 80, SOLUK, "#eeeeee", "0")]
G = 0.8
for i, (ad, satis, renk, acik, fark) in enumerate(durumlar):
    x0 = i * 3.2
    ax.add_patch(patches.Rectangle((x0, 0), G, 80, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.4))
    ax.text(x0 + G / 2, -6, "maliyet", ha="center", va="top", fontsize=11, color=MAVI)
    ax.text(x0 + G / 2, 40, "80", ha="center", va="center", fontsize=12, color=MAVI)
    xs = x0 + 1.1
    ax.add_patch(patches.Rectangle((xs, 0), G, min(satis, 80), facecolor=SARI_ACIK, edgecolor=SARI, lw=1.4))
    ax.text(xs + G / 2, -6, "satış", ha="center", va="top", fontsize=11, color=SARI)
    ax.text(xs + G / 2, min(satis, 80) / 2, str(satis), ha="center", va="center", fontsize=12, color=SARI)
    ax.plot([x0 - 0.15, xs + G + 0.15], [80, 80], ls="--", color=SOLUK, lw=1)
    if satis > 80:
        ax.add_patch(patches.Rectangle((xs, 80), G, satis - 80, facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.4, hatch="//"))
    elif satis < 80:
        ax.add_patch(patches.Rectangle((xs, satis), G, 80 - satis, facecolor="none", edgecolor=KIRMIZI, lw=1.4, ls="--"))
    ax.text(x0 + 0.95, 112, ad, ha="center", va="bottom", fontsize=12, color=renk, fontweight="bold")
    ax.text(x0 + 0.95, -20, fark, ha="center", va="top", fontsize=12, color=renk, fontweight="bold")
ax.set_xlim(-0.4, 9.0); ax.set_ylim(-32, 125)
kaydet(fig, __file__)
