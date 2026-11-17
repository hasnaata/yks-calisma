import sys; sys.path.insert(0, "tools")
from cizim import *

# 12'ye bölümden kalan r için 3'e ve 4'e kalanlar; her (3'e, 4'e) çifti bir kez görünür. r = 10 vurgulu.
fig, ax = sekil(6.2, 2.4)
ax.axis("off"); ax.set_aspect("equal")
satirlar = [("12'ye kalan", lambda r: r, MAVI), ("3'e kalan", lambda r: r % 3, YESIL), ("4'e kalan", lambda r: r % 4, SARI)]
for i, (ad, f, renk) in enumerate(satirlar):
    y = -i
    ax.text(-0.3, y, ad, ha="right", va="center", fontsize=12, color=renk)
    for r in range(12):
        vurgu = r == 10
        ax.add_patch(patches.Rectangle((r, y - 0.5), 1, 1, fc=KIRMIZI_ACIK if vurgu else ("white" if i else MAVI_ACIK),
                                       ec=CIZGI, lw=1))
        ax.text(r + 0.5, y, str(f(r)), ha="center", va="center", fontsize=13,
                color=KIRMIZI if vurgu else YAZI, fontweight="bold" if vurgu else "normal")
ax.add_patch(patches.Rectangle((10, -2.5), 1, 3, fill=False, ec=KIRMIZI, lw=2.2))
ax.set_xlim(-3.6, 12.2); ax.set_ylim(-2.7, 0.7)
kaydet(fig, __file__)
