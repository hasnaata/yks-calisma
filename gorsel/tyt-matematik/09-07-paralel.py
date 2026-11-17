import sys; sys.path.insert(0, "tools")
from cizim import *

# d1 üzerinde 3 nokta, d2 üzerinde 4 nokta (d1 ∥ d2).
# Sol: üçgen = d1'den 1, d2'den 2 nokta. Sağ: dörtgen = d1'den 2, d2'den 2 nokta.
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.9))
U = [(0.5, 1.6), (1.5, 1.6), (2.5, 1.6)]
A = [(0, 0), (1, 0), (2, 0), (3, 0)]
for ax, sec, baslik in ((axs[0], ([1], [0, 2]), "Üçgen: 1 üstten + 2 alttan"),
                        (axs[1], ([0, 2], [1, 3]), "Dörtgen: 2 üstten + 2 alttan")):
    ax.set_aspect("equal"); ax.axis("off")
    ax.plot([-0.5, 3.5], [1.6, 1.6], color=SOLUK, lw=1.6); ax.plot([-0.5, 3.5], [0, 0], color=SOLUK, lw=1.6)
    ax.text(3.55, 1.6, "d₁", va="center", color=SOLUK); ax.text(3.55, 0, "d₂", va="center", color=SOLUK)
    kose = [U[i] for i in sec[0]] + [A[i] for i in sec[1]][::-1]
    renk, acik = (YESIL, YESIL_ACIK) if len(kose) == 3 else (MAVI, MAVI_ACIK)
    ax.add_patch(patches.Polygon(kose, closed=True, facecolor=acik, edgecolor=renk, lw=2.2, zorder=2))
    for p in U + A: ax.plot(*p, "o", color=YAZI, markersize=7, zorder=5)
    ax.set_xlim(-0.6, 3.95); ax.set_ylim(-0.4, 2.0)
    ax.set_title(baslik, fontsize=12, color=YAZI)
fig.tight_layout()
kaydet(fig, __file__)
