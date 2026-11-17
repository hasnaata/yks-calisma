import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders, kural 1: |BC| = 7 ve |BA| = 4 sabit, B'deki açı 20°, 90°, 160°. x = |AC| = sqrt(65 - 56 cos B) = 3,52 / 8,06 / 10,85.
fig, axs = plt.subplots(3, 1, figsize=(5.8, 6.6))
for ax, (al, renk) in zip(axs, [(20, MAVI), (90, YESIL), (160, KIRMIZI)]):
    ax.set_aspect("equal"); ax.axis("off")
    B = np.array([0.0, 0.0]); C = np.array([7.0, 0.0])
    A = 4 * np.array([np.cos(np.radians(al)), np.sin(np.radians(al))])
    x = np.linalg.norm(A - C); print(al, x)
    ax.plot(*zip(B, C), color=YAZI); ax.plot(*zip(B, A), color=YAZI)
    ax.plot(*zip(A, C), color=renk, lw=3)
    nokta(ax, *B, "B", dx=0.0 if al == 160 else -0.75, dy=-0.55 if al == 160 else -0.2)
    nokta(ax, *C, "C", dx=0.25, dy=-0.3); nokta(ax, *A, "A", dx=-0.45 if al == 160 else (-0.6 if al == 90 else -0.2), dy=0.15 if al == 160 else 0.3)
    ax.text(3.5, -0.25, "7", ha="center", va="top")
    if al == 90:
        ax.plot([0.35, 0.35, 0], [0, 0.35, 0.35], color=SOLUK, lw=1.4)
        ax.text(-0.35, 2, "4", ha="center", va="center")
    elif al == 20:
        ax.text(1.8, 1.05, "4", ha="center", va="center")
    else:
        ax.text(-1.8, 0.95, "4", ha="center", va="center")
    m = (A + C) / 2
    deger = f"{x:.1f}".replace(".", ",")
    ax.text(m[0] + 0.3, m[1] + 0.35, f"x ≈ {deger}", color=renk, fontsize=13, fontweight="bold")
    ax.text(8.6, 0.6, f"B = {al}°", fontsize=13, va="center", color=SOLUK)
    ax.set_xlim(-4.4, 10.8); ax.set_ylim(-0.9, 4.4)
fig.subplots_adjust(hspace=0.04)
kaydet(fig, __file__)
