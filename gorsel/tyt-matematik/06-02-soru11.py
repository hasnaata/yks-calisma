import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 11: p anahtarı seri, q ve r anahtarları birbirine paralel. Lamba: p ∧ (q ∨ r).
fig, ax = sekil(6, 3.6)

def tel(xs, ys):
    ax.plot(xs, ys, color=YAZI, lw=2, solid_capstyle="round")

def anahtar(x, y, ad):
    for xx in (x - 0.5, x + 0.5):
        ax.plot(xx, y, "o", markersize=7, markerfacecolor="white", markeredgecolor=YAZI, zorder=5)
    ax.plot([x - 0.5, x + 0.4], [y, y + 0.55], color=MAVI, lw=2.4, zorder=4)
    ax.text(x - 0.75, y + 0.45, ad, ha="center", va="center", fontsize=17, color=MAVI, fontweight="bold")

U, A, L = 4.0, 2.2, 1.6
tel([0, 1.5], [U, U]); tel([2.5, 4], [U, U])          # p seri
tel([4, 4], [U, A]); tel([8, 8], [U, A])               # paralel kol uçları
tel([4, 5.5], [U, U]); tel([6.5, 8], [U, U])           # q kolu
tel([4, 5.5], [A, A]); tel([6.5, 8], [A, A])           # r kolu
tel([8, 10], [U, U])
tel([10, 10], [U, L + 0.42]); tel([10, 10], [L - 0.42, 0]); tel([10, 0], [0, 0])
tel([0, 0], [0, L - 0.12]); tel([0, 0], [L + 0.12, U])
anahtar(2, U, "p"); anahtar(6, U, "q"); anahtar(6, A, "r")
ax.plot([-0.35, 0.35], [L + 0.12, L + 0.12], color=YAZI, lw=2.6)
ax.plot([-0.18, 0.18], [L - 0.12, L - 0.12], color=YAZI, lw=4)
ax.text(-0.55, L, "pil", ha="right", va="center", fontsize=12, color=SOLUK)
ax.add_patch(patches.Circle((10, L), 0.42, facecolor=SARI_ACIK, edgecolor=SARI, lw=2, zorder=4))
d = 0.42 * 0.7
ax.plot([10 - d, 10 + d], [L - d, L + d], color=SARI, lw=1.6, zorder=5)
ax.plot([10 - d, 10 + d], [L + d, L - d], color=SARI, lw=1.6, zorder=5)
ax.text(10.6, L, "lamba", ha="left", va="center", fontsize=12, color=SOLUK)

ax.set_xlim(-1.4, 12); ax.set_ylim(-0.3, 4.9); ax.set_aspect("equal"); ax.axis("off")
kaydet(fig, __file__)
