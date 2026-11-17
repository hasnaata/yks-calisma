import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders: 72 = 2^3 · 3^2 sayısının 12 pozitif böleni, 4 satır × 3 sütun.
fig, ax = sekil(5.2, 4.2)
ax.axis("off"); ax.set_aspect("equal")
w, h = 1.3, 0.9
sutun = ["1", "3", "9"]
satir = ["1", "2", "4", "8"]
for j, s in enumerate(sutun):
    ax.text(j * w + w / 2, 0.45, "×" + s, ha="center", va="center", fontsize=14, color=YESIL, fontweight="bold")
for i, s in enumerate(satir):
    y = -i * h
    ax.text(-0.35, y - h / 2, s, ha="center", va="center", fontsize=14, color=MAVI, fontweight="bold")
    for j in range(3):
        deger = int(s) * int(sutun[j])
        tek = i == 0
        ax.add_patch(patches.FancyBboxPatch((j * w + 0.06, y - h + 0.06), w - 0.12, h - 0.12,
                     boxstyle="round,pad=0,rounding_size=0.08",
                     facecolor=SARI_ACIK if tek else "white", edgecolor=SARI if tek else CIZGI, lw=1.3))
        ax.text(j * w + w / 2, y - h / 2, str(deger), ha="center", va="center", fontsize=15, color=YAZI)
ax.text(3 * w + 0.2, -h / 2, "tek bölenler", ha="left", va="center", fontsize=12, color=SARI)
ax.text(3 * w + 0.2, -2.5 * h, "çift\nbölenler", ha="left", va="center", fontsize=12, color=SOLUK)
ax.plot([3 * w + 0.1, 3 * w + 0.1], [-h - 0.05, -4 * h + 0.05], color=SOLUK, lw=1.2)
ax.text(1.5 * w, -4 * h - 0.45, "4 satır × 3 sütun = 12 bölen", ha="center", va="center", fontsize=13, color=YAZI)
ax.text(-0.35, 0.45, r"$2^a$", ha="center", va="center", fontsize=12, color=MAVI)
ax.set_xlim(-0.8, 3 * w + 1.5); ax.set_ylim(-4 * h - 0.8, 0.8)
kaydet(fig, __file__)
