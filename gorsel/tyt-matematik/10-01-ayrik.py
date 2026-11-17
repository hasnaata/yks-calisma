import sys; sys.path.insert(0, "tools")
from cizim import *

# Bir zar atılıyor, E = {1, 2, 3, 4, 5, 6}.
# Sol: A = {1, 2} (3'ten küçük), B = {5, 6} (4'ten büyük): ayrık.
# Sağ: A = {2, 4, 6} (çift), C = {2, 3, 5} (asal): ortak eleman 2, ayrık değil.
fig, eks = plt.subplots(1, 2, figsize=(6.4, 3.6))
def cerceve(ax, baslik, renk):
    ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.1, 6.1); ax.set_ylim(-0.9, 4.6)
    ax.add_patch(patches.Rectangle((0, 0), 6, 3.9, facecolor="none", edgecolor=SOLUK, lw=1.4))
    ax.text(0.15, 3.65, "E", fontsize=14, color=SOLUK, va="top")
    ax.text(3, 4.15, baslik, ha="center", fontsize=13, color=renk, fontweight="bold")
def daire(ax, m, r, renk, acik, ad, adx, ady):
    ax.add_patch(patches.Circle(m, r, facecolor=acik, edgecolor=renk, lw=2, alpha=0.75))
    ax.text(adx, ady, ad, color=renk, fontsize=15, fontweight="bold", ha="center")
def yaz(ax, x, y, s):
    ax.text(x, y, s, ha="center", va="center", fontsize=15, color=YAZI)

ax = eks[0]; cerceve(ax, "Ayrık", YESIL)
daire(ax, (1.55, 1.75), 1.05, MAVI, MAVI_ACIK, "A", 1.55, 2.95)
daire(ax, (4.45, 1.75), 1.05, SARI, SARI_ACIK, "B", 4.45, 2.95)
yaz(ax, 1.2, 1.6, "1"); yaz(ax, 1.9, 1.6, "2"); yaz(ax, 4.1, 1.6, "5"); yaz(ax, 4.8, 1.6, "6")
yaz(ax, 3, 0.45, "3   4")
ax.text(3, -0.55, "A ∩ B = ∅", ha="center", fontsize=14, color=YESIL)

ax = eks[1]; cerceve(ax, "Ayrık değil", KIRMIZI)
daire(ax, (2.25, 1.85), 1.2, MAVI, MAVI_ACIK, "A", 1.5, 3.2)
daire(ax, (3.75, 1.85), 1.2, SARI, SARI_ACIK, "C", 4.5, 3.2)
yaz(ax, 1.55, 2.25, "4"); yaz(ax, 1.55, 1.35, "6"); yaz(ax, 3, 1.85, "2")
yaz(ax, 4.45, 2.25, "3"); yaz(ax, 4.45, 1.35, "5"); yaz(ax, 5.6, 0.35, "1")
ax.text(3, -0.55, "A ∩ C = {2}", ha="center", fontsize=14, color=KIRMIZI)
fig.subplots_adjust(wspace=0.08)
kaydet(fig, __file__)
