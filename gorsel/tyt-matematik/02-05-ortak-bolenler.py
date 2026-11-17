import sys; sys.path.insert(0, "tools")
from cizim import *

# 36 ve 48'in bölenleri; ortak olanlar yeşil. Ortak bölenler tam olarak 12'nin bölenleridir.
fig, ax = sekil(6.2, 2.9)
ax.axis("off"); ax.set_aspect("equal")
b36 = [d for d in range(1, 37) if 36 % d == 0]
b48 = [d for d in range(1, 49) if 48 % d == 0]
ortak = set(b36) & set(b48)
satirlar = [("36", b36, MAVI), ("48", b48, SARI), ("12", sorted(ortak), YESIL)]
for i, (ad, liste, renk) in enumerate(satirlar):
    y = -1.3 * i
    ax.text(-0.3, y, ad + (" →" if i == 2 else ""), ha="right", va="center", fontsize=14, color=renk, fontweight="bold")
    for j, d in enumerate(liste):
        o = d in ortak
        ax.add_patch(patches.Rectangle((j, y - 0.5), 1, 1, fc=YESIL_ACIK if o else "white", ec=YESIL if o else CIZGI, lw=1.4 if o else 1))
        ax.text(j + 0.5, y, str(d), ha="center", va="center", fontsize=13,
                color=KIRMIZI if d == 12 else YAZI, fontweight="bold" if d == 12 else "normal")
ax.text(-0.3, 0.95, "bölenler", ha="right", va="center", fontsize=11, color=SOLUK)
ax.set_xlim(-2.6, 10.2); ax.set_ylim(-3.2, 1.3)
kaydet(fig, __file__)
