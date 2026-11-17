import sys; sys.path.insert(0, "tools")
from cizim import *

# Ali işi yalnız 12 günde (günde %100/12), Bora 24 günde (günde %100/24) bitirir.
# 6. günde Ali %50, Bora %25. Birlikte 6 günde %75 -> tamamı 8 gün.
fig, ax = sekil(6, 3.8)
eksenler(ax, x=(0, 13.5), y=(0, 115), izgara=False)
for t in list(ax.texts): t.remove()  # x, y harflerini kaldır; eksen adları aşağıda
ax.set_xticks([0, 2, 4, 6, 8, 10, 12]); ax.set_yticks([0, 25, 50, 75, 100])
for y in (25, 50, 75, 100): ax.axhline(y, color=CIZGI, lw=0.6, zorder=0)
ax.plot([0, 12], [0, 100], color=MAVI)
ax.plot([0, 12], [0, 50], color=SARI)
ax.plot([6, 6], [0, 50], color=SOLUK, lw=1.1, ls="--")
nokta(ax, 6, 50, renk=MAVI); nokta(ax, 6, 25, renk=SARI)
ax.text(9.2, 86, "Ali", color=MAVI, fontsize=12, fontweight="bold")
ax.text(10.3, 34, "Bora", color=SARI, fontsize=12, fontweight="bold")
ax.text(13.8, 0, "gün", fontsize=11, color=SOLUK, va="center")
ax.text(0.3, 110, "yapılan iş (%)", fontsize=11, color=SOLUK)
kaydet(fig, __file__)
