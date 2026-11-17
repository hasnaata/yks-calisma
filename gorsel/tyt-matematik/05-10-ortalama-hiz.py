import sys; sys.path.insert(0, "tools")
from cizim import *

# 120 km'lik yol: gidiş 60 km/sa (2 saat), dönüş 40 km/sa (3 saat). Toplam yol 240 km, toplam süre 5 saat.
# Ortalama hız 240 / 5 = 48 km/sa: başlangıçtan sona çizilen kesikli doğrunun eğimi.
fig, ax = sekil(6, 3.9)
eksenler(ax, x=(0, 5.8), y=(0, 280), izgara=False)
for t in list(ax.texts): t.remove()
ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([0, 60, 120, 180, 240])
for y in (60, 120, 180, 240): ax.axhline(y, color=CIZGI, lw=0.6, zorder=0)
for x in (1, 2, 3, 4, 5): ax.axvline(x, color=CIZGI, lw=0.6, zorder=0)
ax.plot([0, 2], [0, 120], color=MAVI)
ax.plot([2, 5], [120, 240], color=SARI)
ax.plot([0, 5], [0, 240], color=KIRMIZI, ls="--", lw=1.8)
nokta(ax, 2, 120, renk=YAZI); nokta(ax, 5, 240, renk=YAZI)
ax.text(0.15, 112, "gidiş\n60 km/sa", color=MAVI, fontsize=11, va="bottom")
ax.text(3.6, 162, "dönüş\n40 km/sa", color=SARI, fontsize=11, va="top")
ax.text(2.55, 82, "ortalama\n240 ÷ 5 = 48 km/sa", color=KIRMIZI, fontsize=11, va="top")
ax.text(5.95, 0, "saat", fontsize=11, color=SOLUK, va="center")
ax.text(0.1, 268, "alınan toplam yol (km)", fontsize=11, color=SOLUK)
kaydet(fig, __file__)
