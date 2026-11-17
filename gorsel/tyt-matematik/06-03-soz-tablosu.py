import sys; sys.path.insert(0, "tools")
from cizim import *

# "90 alırsan bisiklet alırım" sözü: dört durum, yalnızca biri sözü bozar (p ⇒ q doğruluk tablosu).
fig, ax = sekil(6, 3.9)
ax.axis("off")
satirlar = [
    ("1", "1", "90 aldın, bisiklet geldi", "1", "Söz tutuldu"),
    ("1", "0", "90 aldın, bisiklet yok", "0", "Söz bozuldu"),
    ("0", "1", "90 yok, bisiklet geldi", "1", "Söz bozulmadı"),
    ("0", "0", "90 yok, bisiklet yok", "1", "Söz bozulmadı"),
]
xs = [0.35, 1.05, 3.35, 5.6]
ax.text(xs[0], 4.55, "p", ha="center", color=MAVI, fontsize=15, fontweight="bold")
ax.text(xs[1], 4.55, "q", ha="center", color=MAVI, fontsize=15, fontweight="bold")
ax.text(xs[2], 4.55, "Ne oldu?", ha="center", color=MAVI, fontsize=13, fontweight="bold")
ax.text(xs[3], 4.55, "p ⇒ q", ha="center", color=MAVI, fontsize=15, fontweight="bold")
for i, (p, q, olay, d, not_) in enumerate(satirlar):
    y = 3.6 - i * 1.0
    kotu = d == "0"
    ax.add_patch(patches.FancyBboxPatch((-0.05, y - 0.4), 6.5, 0.8, boxstyle="round,pad=0.02,rounding_size=0.12",
                 facecolor=KIRMIZI_ACIK if kotu else YESIL_ACIK, edgecolor=KIRMIZI if kotu else CIZGI, lw=1.4 if kotu else 0.8))
    ax.text(xs[0], y, p, ha="center", va="center", fontsize=14)
    ax.text(xs[1], y, q, ha="center", va="center", fontsize=14)
    ax.text(xs[2], y + 0.13, olay, ha="center", va="center", fontsize=11.5)
    ax.text(xs[2], y - 0.2, not_, ha="center", va="center", fontsize=10.5, color=KIRMIZI if kotu else SOLUK, style="italic")
    ax.text(xs[3], y, d, ha="center", va="center", fontsize=16, fontweight="bold", color=KIRMIZI if kotu else YESIL)
ax.text(3.2, -0.15, "p: 90 alırsın     q: bisiklet alırım", ha="center", fontsize=12, color=SOLUK)
ax.set_xlim(-0.1, 6.5); ax.set_ylim(-0.4, 4.9)
kaydet(fig, __file__)
