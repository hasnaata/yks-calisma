import sys; sys.path.insert(0, "tools")
from cizim import *

# 51 sayısının sağına 7 yazmak: rakamlar bir basamak sola kayar (×10), birler basamağına 7 gelir.
fig, ax = sekil(6, 3.2)
ax.axis("off"); ax.set_aspect("equal")
G, H, X0 = 1.3, 1.0, 2.2
for j, ad in enumerate(["Yüzler", "Onlar", "Birler"]):
    ax.text(X0 + j * G + G / 2, 0.35, ad, ha="center", va="center", fontsize=12, color=SOLUK)

def kutu(j, y, rakam, renk=YAZI, dolgu="white"):
    ax.add_patch(patches.Rectangle((X0 + j * G, y), G, H, facecolor=dolgu, edgecolor=CIZGI, lw=1.2))
    if rakam != "":
        ax.text(X0 + j * G + G / 2, y + H / 2, rakam, ha="center", va="center", fontsize=20, color=renk, fontweight="bold")

Y1, Y2 = -1.0, -3.4
ax.text(X0 - 0.25, Y1 + H / 2, "x = 51", ha="right", va="center", fontsize=14)
ax.text(X0 - 0.25, Y2 + H / 2, "517", ha="right", va="center", fontsize=14)
for j, r in enumerate(["", "5", "1"]): kutu(j, Y1, r, MAVI, MAVI_ACIK if r else "white")
for j, r in enumerate(["5", "1"]): kutu(j, Y2, r, MAVI, MAVI_ACIK)
kutu(2, Y2, "7", YESIL, YESIL_ACIK)
for j in (1, 2):
    ax.annotate("", xy=(X0 + (j - 1) * G + G / 2, Y2 + H + 0.05), xytext=(X0 + j * G + G / 2, Y1 - 0.05),
                arrowprops=dict(arrowstyle="->", color=MAVI, lw=1.6))
ax.text(X0 + 3 * G + 0.3, (Y1 + Y2 + H) / 2, "bir basamak sola:\n51 · 10 = 510", ha="left", va="center", fontsize=12, color=MAVI)
ax.text(X0 + 3 * G + 0.3, Y2 + H / 2, "+ 7 → 517", ha="left", va="center", fontsize=13, color=YESIL, fontweight="bold")
ax.set_xlim(0.6, X0 + 3 * G + 3.4); ax.set_ylim(Y2 - 0.1, 0.65)
kaydet(fig, __file__)
