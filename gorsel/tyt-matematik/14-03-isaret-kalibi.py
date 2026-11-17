import sys; sys.path.insert(0, "tools")
from cizim import *

# Küp toplamı ve farkı: parantez içindeki işaretlerin kalıbı.
# Her satır parça parça yazılır; işaretlerin altına ne olduklarını gösteren etiket konur.
fig, ax = sekil(6.2, 3.0)
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 5)
fig.canvas.draw()
r = fig.canvas.get_renderer()
inv = ax.transData.inverted()

def satir(y, parcalar, renkler):
    x = 0.1
    merkez = {}
    for i, (t, ad) in enumerate(parcalar):
        h = ax.text(x, y, t, fontsize=19, va="baseline", ha="left", color=renkler.get(ad, YAZI))
        bb = h.get_window_extent(renderer=r)
        (x0, _), (x1, _) = inv.transform((bb.x0, 0)), inv.transform((bb.x1, 0))
        if ad: merkez[ad] = (x0 + x1) / 2
        x = x1 + 0.08
    return merkez

ETIKET = {"ayni": ("aynı", MAVI), "ters": ("ters", KIRMIZI), "hep": ("hep +", YESIL)}
renk = {"bas": MAVI, "ayni": MAVI, "ters": KIRMIZI, "hep": YESIL}
for y, isaret, ters in ((3.6, "+", "−"), (0.9, "−", "+")):
    parca = [(r"$a^3$", ""), (isaret, "bas"), (r"$b^3\ =\ (a$", ""), (isaret, "ayni"),
             (r"$b)(a^2$", ""), (ters, "ters"), (r"$ab$", ""), ("+", "hep"), (r"$b^2)$", "")]
    m = satir(y, parca, renk)
    for ad in ("ayni", "ters", "hep"):
        yazi, rk = ETIKET[ad]
        ax.annotate(yazi, xy=(m[ad], y - 0.15), xytext=(m[ad], y - 1.05), ha="center", va="center",
                    fontsize=12, color=rk, arrowprops=dict(arrowstyle="-|>", color=rk, lw=1.2))
kaydet(fig, __file__)
