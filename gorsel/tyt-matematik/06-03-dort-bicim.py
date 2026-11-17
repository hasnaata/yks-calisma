import sys; sys.path.insert(0, "tools")
from cizim import *

# Koşullu önerme, karşıtı, tersi, karşıt tersi. Aynı renkteki kutular birbirine denktir.
fig, ax = sekil(6, 4.2)
ax.axis("off")
kutular = {
    "k":  (1.4, 3.0, "Koşullu", "p ⇒ q", YESIL, YESIL_ACIK),
    "kr": (6.0, 3.0, "Karşıtı", "q ⇒ p", SARI, SARI_ACIK),
    "t":  (1.4, 0.4, "Tersi", "p′ ⇒ q′", SARI, SARI_ACIK),
    "kt": (6.0, 0.4, "Karşıt tersi", "q′ ⇒ p′", YESIL, YESIL_ACIK),
}
W, H = 2.5, 1.25
for x, y, ad, ifade, renk, acik in kutular.values():
    ax.add_patch(patches.FancyBboxPatch((x - W / 2, y - H / 2), W, H, boxstyle="round,pad=0.02,rounding_size=0.15",
                 facecolor=acik, edgecolor=renk, lw=1.8))
    ax.text(x, y + 0.27, ad, ha="center", va="center", fontsize=12, color=renk, fontweight="bold")
    ax.text(x, y - 0.22, ifade, ha="center", va="center", fontsize=16, color=YAZI)
ok = dict(arrowstyle="<->", color=SOLUK, lw=1.4)
ax.annotate("", xy=(6.0 - W / 2 - 0.05, 3.0), xytext=(1.4 + W / 2 + 0.05, 3.0), arrowprops=ok)
ax.text(3.7, 3.22, "yer değiştir", ha="center", fontsize=11, color=SOLUK)
ax.annotate("", xy=(1.4, 0.4 + H / 2 + 0.05), xytext=(1.4, 3.0 - H / 2 - 0.05), arrowprops=ok)
ax.text(1.4 - W / 2 - 0.1, 1.7, "ikisini de\ndeğille", ha="right", va="center", fontsize=11, color=SOLUK)
ax.annotate("", xy=(6.0 - W / 2 - 0.05, 0.4 + 0.2), xytext=(1.4 + W / 2 + 0.05, 3.0 - 0.2),
            arrowprops=dict(arrowstyle="<->", color=YESIL, lw=1.8, ls="--"))
ax.text(3.7, 1.7, "≡", ha="center", va="center", fontsize=20, color=YESIL, fontweight="bold", bbox=dict(facecolor="white", edgecolor="none", pad=1))
ax.text(3.7, -0.65, "Aynı renk = denk", ha="center", fontsize=12, color=SOLUK)
ax.set_xlim(-0.6, 7.4); ax.set_ylim(-0.9, 3.8)
kaydet(fig, __file__)
