import sys; sys.path.insert(0, "tools")
from cizim import *

# 3x + 5y = 47: y'yi büyükten küçüğe dene, 47 - 5y 3'e bölünüyor mu?
# Geçerli satırlar y = 7, 4, 1 (x = 4, 9, 14). y her seferinde 3 azalır.
fig, ax = sekil(6.2, 3.2)
ax.axis("off")
ys = list(range(9, -1, -1))
w = 0.62
x0 = 1.5
ax.text(x0 - 0.15, 2.0, "y", ha="right", va="center", fontsize=14, fontweight="bold")
ax.text(x0 - 0.15, 1.2, "47 − 5y", ha="right", va="center", fontsize=13)
ax.text(x0 - 0.15, 0.4, "x", ha="right", va="center", fontsize=14, fontweight="bold")
for i, y in enumerate(ys):
    k = 47 - 5 * y
    gecer = k % 3 == 0
    x = x0 + i * w
    renk, acik = (YESIL, YESIL_ACIK) if gecer else (CIZGI, "white")
    for yy in (2.0, 1.2, 0.4):
        ax.add_patch(patches.Rectangle((x, yy - 0.35), w, 0.7, facecolor=acik, edgecolor=renk if gecer else CIZGI, lw=1.4 if gecer else 0.8))
    ax.text(x + w / 2, 2.0, str(y), ha="center", va="center", fontsize=13)
    ax.text(x + w / 2, 1.2, str(k), ha="center", va="center", fontsize=13, color=YESIL if gecer else SOLUK)
    ax.text(x + w / 2, 0.4, str(k // 3) if gecer else "–", ha="center", va="center", fontsize=13,
            color=YESIL if gecer else SOLUK, fontweight="bold" if gecer else "normal")
gec = [i for i, y in enumerate(ys) if (47 - 5 * y) % 3 == 0]
for a, b in zip(gec[:-1], gec[1:]):
    xa, xb = x0 + a * w + w / 2, x0 + b * w + w / 2
    ax.annotate("", xy=(xb, 2.45), xytext=(xa, 2.45), arrowprops=dict(arrowstyle="->", color=SARI, lw=1.6,
                                                                       connectionstyle="arc3,rad=-0.35"))
    ax.text((xa + xb) / 2, 2.95, "y: −3", ha="center", va="bottom", fontsize=11, color=SARI)
ax.text(x0 + 5 * w, -0.25, "Yeşil sütunlar: 47 − 5y sayısı 3'e bölünüyor", ha="center", va="top", fontsize=12, color=YESIL)
ax.set_xlim(0, x0 + 10 * w + 0.1); ax.set_ylim(-0.7, 3.4)
kaydet(fig, __file__)
