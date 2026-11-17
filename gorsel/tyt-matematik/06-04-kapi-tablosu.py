import sys; sys.path.insert(0, "tools")
from cizim import *

# "Kapı ancak ve ancak kart okutulursa açılır": dört durum, iki tanesi kuralı bozar (p ⇔ q doğruluk tablosu).
fig, ax = sekil(6, 3.9)
ax.axis("off")
satirlar = [
    ("1", "1", "Kart okutuldu, kapı açıldı", "1", "Kural işledi"),
    ("1", "0", "Kart okutuldu, kapı açılmadı", "0", "Arıza"),
    ("0", "1", "Kart yok, kapı açıldı", "0", "Arıza"),
    ("0", "0", "Kart yok, kapı kapalı", "1", "Kural işledi"),
]
xs = [0.35, 1.05, 3.35, 5.75]
ax.text(xs[0], 4.55, "p", ha="center", color=MAVI, fontsize=15, fontweight="bold")
ax.text(xs[1], 4.55, "q", ha="center", color=MAVI, fontsize=15, fontweight="bold")
ax.text(xs[2], 4.55, "Ne oldu?", ha="center", color=MAVI, fontsize=13, fontweight="bold")
ax.text(xs[3], 4.55, "p ⇔ q", ha="center", color=MAVI, fontsize=15, fontweight="bold")
for i, (p, q, olay, d, not_) in enumerate(satirlar):
    y = 3.6 - i * 1.0
    kotu = d == "0"
    ax.add_patch(patches.FancyBboxPatch((-0.05, y - 0.4), 6.6, 0.8, boxstyle="round,pad=0.02,rounding_size=0.12",
                 facecolor=KIRMIZI_ACIK if kotu else YESIL_ACIK, edgecolor=KIRMIZI if kotu else CIZGI, lw=1.4 if kotu else 0.8))
    ax.text(xs[0], y, p, ha="center", va="center", fontsize=14)
    ax.text(xs[1], y, q, ha="center", va="center", fontsize=14)
    ax.text(xs[2], y + 0.13, olay, ha="center", va="center", fontsize=11.5)
    ax.text(xs[2], y - 0.2, not_, ha="center", va="center", fontsize=10.5, color=KIRMIZI if kotu else SOLUK, style="italic")
    ax.text(xs[3], y, d, ha="center", va="center", fontsize=16, fontweight="bold", color=KIRMIZI if kotu else YESIL)
ax.text(3.25, -0.15, "p: kart okutuldu     q: kapı açıldı", ha="center", fontsize=12, color=SOLUK)
ax.set_xlim(-0.1, 6.6); ax.set_ylim(-0.4, 4.9)
kaydet(fig, __file__)
