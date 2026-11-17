import sys; sys.path.insert(0, "tools")
from cizim import *

# Sol: y = 2^x artan; üs büyürse değer büyür (1 < 3, 2 < 8).
# Sağ: y = (1/2)^x azalan; üs büyürse değer küçülür (−3 < −1, 8 > 2).
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.2, 3.8))
xs = np.linspace(-3.3, 3.3, 400)
satirlar = ((a1, 2, "$y = 2^x$  (taban > 1)", MAVI, (1, 3)),
            (a2, 0.5, "$y = (1/2)^x$  (taban < 1)", KIRMIZI, (-3, -1)))
for ax, taban, baslik, renk, usler in satirlar:
    eksenler(ax, x=(-3.5, 3.5), y=(-0.6, 9.8), izgara=False)
    ax.plot(xs, taban ** xs, color=renk)
    ax.set_xticks([-3, -1, 1, 3]); ax.set_xticklabels(["−3", "−1", "1", "3"])
    ax.set_yticks([])
    for u in usler:
        d = taban ** u
        ax.plot([u, u], [0, d], color=SOLUK, lw=1, ls=":")
        ax.plot(u, d, "o", color=renk, markersize=7, zorder=5)
        ax.text(u + (0.22 if taban > 1 else -0.22), d - 0.25, str(int(d)), ha="left" if taban > 1 else "right",
                va="top", fontsize=12, color=renk)
    ax.set_title(baslik, fontsize=12, pad=22)
a1.text(-3.3, 6.0, "Üs büyür,\ndeğer büyür", fontsize=11, color=YAZI)
a2.text(0.5, 6.0, "Üs büyür,\ndeğer küçülür", fontsize=11, color=YAZI)
fig.tight_layout(w_pad=2)
kaydet(fig, __file__)
