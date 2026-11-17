import sys; sys.path.insert(0, "tools")
from cizim import *

# Ters işaretli iki sayının toplamı: sıfıra uzak olan (mutlak değerce büyük) sayının işaretini alır.
SATIRLAR = [(-2, 5, YESIL, "−2 + 5 = 3"), (-5, 2, KIRMIZI, "−5 + 2 = −3"), (-4, 4, MAVI, "−4 + 4 = 0")]
fig, eks = plt.subplots(len(SATIRLAR), 1, figsize=(6, 4.2))
for ax, (a, b, renk, yazi) in zip(eks, SATIRLAR):
    sayi_dogrusu(ax, -5, 5)
    ax.set_ylim(-0.95, 1.05)
    ax.hlines(0.28, a, 0, color=KIRMIZI, lw=4, alpha=0.55)
    ax.hlines(0.28, 0, b, color=YESIL, lw=4, alpha=0.55)
    ax.plot(a, 0, "o", color=KIRMIZI, markersize=9, zorder=5)
    ax.plot(b, 0, "o", color=YESIL, markersize=9, zorder=5)
    ax.plot(a + b, 0, "D", color=renk, markersize=9, zorder=6, markeredgecolor="white")
    ax.text(-5.5, 0.78, yazi, ha="left", va="center", fontsize=13, color=renk)
kaydet(fig, __file__)
