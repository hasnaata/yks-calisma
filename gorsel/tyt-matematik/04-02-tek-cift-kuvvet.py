import sys; sys.path.insert(0, "tools")
from cizim import *

# Sol: y = x^3 ile y = 8 tek noktada kesişir (x = 2).
# Sağ: y = x^4 ile y = 16 iki noktada kesişir (x = −2 ve x = 2).
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.2, 3.8))
xs = np.linspace(-3, 3, 400)
for ax, n, c, baslik in ((a1, 3, 8, "Tek kuvvet: $x^3 = 8$"), (a2, 4, 16, "Çift kuvvet: $x^4 = 16$")):
    ust = 22
    eksenler(ax, x=(-3.2, 3.2), y=(-ust, ust), izgara=False)
    ax.set_xticks([-2, 2]); ax.set_yticks([])
    ax.set_xticklabels(["−2", "2"])
    ax.plot(xs, xs ** n, color=MAVI)
    ax.axhline(c, color=SARI, lw=1.6, ls="--")
    if n == 3:
        ax.text(-3.1, c + 1.5, "y = 8", color=SARI, fontsize=12)
    else:
        ax.text(0.2, c + 1.5, "y = 16", color=SARI, fontsize=12)
    kokler = [2] if n == 3 else [-2, 2]
    for k in kokler:
        ax.plot([k, k], [0, c], color=SOLUK, lw=1, ls=":")
        ax.plot(k, c, "o", color=KIRMIZI, markersize=8, zorder=5)
    ax.set_title(baslik, fontsize=13, pad=22)
fig.tight_layout(w_pad=2)
kaydet(fig, __file__)
