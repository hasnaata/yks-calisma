import sys; sys.path.insert(0, "tools")
from cizim import *

# Seri bağlı anahtarlar "ve", paralel bağlı anahtarlar "veya" gibi çalışır.
fig, ax = sekil(6, 7.2)

def tel(xs, ys):
    ax.plot(xs, ys, color=YAZI, lw=2, solid_capstyle="round")

def anahtar(x, y, ad, renk=MAVI):
    """x-0.5 ile x+0.5 arasında, açık çizilmiş anahtar; adı üstünde."""
    for xx in (x - 0.5, x + 0.5):
        ax.plot(xx, y, "o", markersize=7, markerfacecolor="white", markeredgecolor=YAZI, zorder=5)
    ax.plot([x - 0.5, x + 0.4], [y, y + 0.55], color=renk, lw=2.4, zorder=4)
    ax.text(x - 0.75, y + 0.45, ad, ha="center", va="center", fontsize=17, color=renk, fontweight="bold")

def pil(x, y):
    ax.plot([x - 0.35, x + 0.35], [y + 0.12, y + 0.12], color=YAZI, lw=2.6)
    ax.plot([x - 0.18, x + 0.18], [y - 0.12, y - 0.12], color=YAZI, lw=4)
    ax.text(x - 0.55, y, "pil", ha="right", va="center", fontsize=12, color=SOLUK)

def lamba(x, y):
    ax.add_patch(patches.Circle((x, y), 0.42, facecolor=SARI_ACIK, edgecolor=SARI, lw=2, zorder=4))
    d = 0.42 * 0.7
    ax.plot([x - d, x + d], [y - d, y + d], color=SARI, lw=1.6, zorder=5)
    ax.plot([x - d, x + d], [y + d, y - d], color=SARI, lw=1.6, zorder=5)
    ax.text(x + 0.6, y, "lamba", ha="left", va="center", fontsize=12, color=SOLUK)

# Üst: seri (y = 6 ile 9 arası)
Y0, Y1 = 6.2, 9.2
tel([0, 2.5], [Y1, Y1]); tel([3.5, 5.5], [Y1, Y1]); tel([6.5, 9], [Y1, Y1])
tel([9, 9], [Y1, 7.7 + 0.42]); tel([9, 9], [7.7 - 0.42, Y0]); tel([9, 0], [Y0, Y0])
tel([0, 0], [Y0, 7.7 - 0.12]); tel([0, 0], [7.7 + 0.12, Y1])
anahtar(3, Y1, "p"); anahtar(6, Y1, "q")
pil(0, 7.7); lamba(9, 7.7)
ax.text(4.5, 8.0, "Seri bağlı:  p ∧ q", ha="center", va="center", fontsize=15, color=MAVI, fontweight="bold")
ax.text(4.5, 7.25, "İkisi de kapalıysa yanar.", ha="center", va="center", fontsize=12, color=YAZI)

# Alt: paralel (y = 0 ile 4 arası)
U, A = 4.0, 2.2
tel([0, 2], [U, U]); tel([7, 9], [U, U])
tel([2, 2], [U, A]); tel([7, 7], [U, A])
tel([2, 4], [U, U]); tel([5, 7], [U, U])
tel([2, 4], [A, A]); tel([5, 7], [A, A])
tel([9, 9], [U, 2.1 + 0.42]); tel([9, 9], [2.1 - 0.42, 0]); tel([9, 0], [0, 0])
tel([0, 0], [0, 2.1 - 0.12]); tel([0, 0], [2.1 + 0.12, U])
anahtar(4.5, U, "p", YESIL); anahtar(4.5, A, "q", YESIL)
pil(0, 2.1); lamba(9, 2.1)
ax.text(4.5, 1.2, "Paralel bağlı:  p ∨ q", ha="center", va="center", fontsize=15, color=YESIL, fontweight="bold")
ax.text(4.5, 0.5, "En az biri kapalıysa yanar.", ha="center", va="center", fontsize=12, color=YAZI)

ax.set_xlim(-1.4, 11); ax.set_ylim(-0.3, 10.1); ax.set_aspect("equal"); ax.axis("off")
kaydet(fig, __file__)
