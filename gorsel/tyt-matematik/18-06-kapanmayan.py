import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders, kural 1: taban 6 sabit. Sol: çubuklar 2 ve 3 (2 + 3 < 6, yaylar kesişmez). Sağ: çubuklar 4 ve 3 (4 + 3 > 6, yaylar A'da kesişir).
def kesisim(r1, r2, d):
    x = (d * d + r1 * r1 - r2 * r2) / (2 * d); return np.array([x, np.sqrt(r1 * r1 - x * x)])

fig, axs = plt.subplots(2, 1, figsize=(5.6, 6.4))
for ax, (r1, r2, renk, baslik) in zip(axs, [(2, 3, KIRMIZI, "2 + 3 < 6 → üçgen yok"), (4, 3, YESIL, "4 + 3 > 6 → üçgen var")]):
    ax.set_aspect("equal"); ax.axis("off")
    B = np.array([0.0, 0.0]); C = np.array([6.0, 0.0])
    t = np.linspace(0, np.pi, 200)
    ax.plot(r1 * np.cos(t), r1 * np.sin(t), "--", color=CIZGI, lw=1.4)
    ax.plot(6 + r2 * np.cos(t), r2 * np.sin(t), "--", color=CIZGI, lw=1.4)
    ax.plot(*zip(B, C), color=YAZI, lw=2.6)
    ax.text(3, -0.35, "6", ha="center", va="top")
    if r1 + r2 > 6:
        A = kesisim(r1, r2, 6.0); print("A", A, np.linalg.norm(A - C))
        ax.plot(*zip(B, A, C), color=renk, lw=2.6)
        nokta(ax, *A, "A", dx=-0.1, dy=0.2)
        ax.text(*(A / 2 + np.array([-0.35, 0.1])), str(r1), color=renk, ha="center", fontsize=14)
        ax.text(*((A + C) / 2 + np.array([0.35, 0.1])), str(r2), color=renk, ha="center", fontsize=14)
    else:
        P = r1 * np.array([np.cos(np.radians(50)), np.sin(np.radians(50))])
        Q = C + r2 * np.array([np.cos(np.radians(125)), np.sin(np.radians(125))])
        ax.plot(*zip(B, P), color=renk, lw=2.6); ax.plot(*zip(C, Q), color=renk, lw=2.6)
        ax.text(*(P / 2 + np.array([-0.35, 0.15])), str(r1), color=renk, ha="center", fontsize=14)
        ax.text(*((Q + C) / 2 + np.array([0.35, 0.15])), str(r2), color=renk, ha="center", fontsize=14)
        ax.annotate("", xy=(2.0, 0.25), xytext=(3.0, 0.25), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
        ax.text(2.5, 0.4, "1", color=SOLUK, ha="center", fontsize=12)
    nokta(ax, *B, "B", dx=-0.5, dy=-0.3); nokta(ax, *C, "C", dx=0.15, dy=-0.3)
    ax.text(3, 4.3, baslik, ha="center", fontsize=14, color=renk, fontweight="bold")
    ax.set_xlim(-4.2, 9.4); ax.set_ylim(-0.8, 4.7)
fig.subplots_adjust(hspace=0.08)
kaydet(fig, __file__)
