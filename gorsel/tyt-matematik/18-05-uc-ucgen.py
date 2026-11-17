import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders, kural 3: b=|AC|=4, c=|AB|=5 sabit; alfa = m(A) 60, 90, 120. a^2 = 41 - 40 cos(alfa) = 21, 41, 61.
fig, axs = plt.subplots(3, 1, figsize=(5.6, 7.6))
satir = [(60, "dar açı", "a² = 21 < 41", MAVI), (90, "dik açı", "a² = 41", YESIL), (120, "geniş açı", "a² = 61 > 41", KIRMIZI)]
for ax, (al, tur, sonuc, renk) in zip(axs, satir):
    ax.set_aspect("equal"); ax.axis("off")
    A = np.array([0.0, 0.0]); B = np.array([5.0, 0.0])
    C = 4 * np.array([np.cos(np.radians(al)), np.sin(np.radians(al))])
    print(al, "a^2 =", round(np.sum((B - C) ** 2), 6))
    ax.plot(*zip(A, B), color=YAZI); ax.plot(*zip(A, C), color=YAZI)
    ax.plot(*zip(B, C), color=renk, lw=3)
    nokta(ax, *A, "A", dx=-0.75, dy=-0.2); nokta(ax, *B, "B", dx=0.3, dy=-0.2); nokta(ax, *C, "C", dx=-0.15, dy=0.2)
    if al == 90:
        ax.plot([0.45, 0.45, 0], [0, 0.45, 0.45], color=SOLUK, lw=1.4)
        ax.text(0.65, 0.7, "α", color=SOLUK, fontsize=13)
    else:
        aci(ax, A, B, C, r=0.55, ad="α", renk=SOLUK)
    ax.text(2.5, -0.35, "5", ha="center", va="top")
    ax.text(*(C / 2 + np.array([-0.35 if al <= 90 else -0.3, 0.1 if al <= 90 else -0.25])), "4", ha="center", va="center")
    m = (B + C) / 2
    ax.text(m[0] + 0.25, m[1] + 0.3, "a", color=renk, fontsize=14, fontweight="bold")
    ax.text(6.4, 2.3, f"α = {al}° ({tur})", fontsize=13, va="center")
    ax.text(6.4, 1.3, sonuc, fontsize=14, color=renk, fontweight="bold", va="center")
    ax.set_xlim(-2.6, 11.5); ax.set_ylim(-0.9, 4.3)
fig.subplots_adjust(hspace=0.05)
kaydet(fig, __file__)
