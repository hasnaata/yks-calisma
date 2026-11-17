import sys; sys.path.insert(0, "tools")
from cizim import *

# Depodaki su miktarı f(t) = 120 − 15t (t saat, f litre). t = 0'da 120 L, t = 8'de 0 L.
fig, ax = sekil(5.4, 4)
eksenler(ax, x=(-0.8, 10.2), y=(-14, 150), izgara=False)
for _y in list(ax.texts): _y.remove()  # x/y yerine t ve f(t) adları
ax.set_xticks([8]); ax.set_xticklabels(["8"]); ax.set_yticks([120]); ax.set_yticklabels(["120"])
ax.plot([0, 8], [120, 0], color=MAVI)
nokta(ax, 0, 120, renk=MAVI); nokta(ax, 8, 0, renk=MAVI)
ax.text(10.4, 0, "t (saat)", ha="left", va="center", fontsize=12, color=SOLUK)
ax.text(0, 157, "f(t) (litre)", ha="center", va="bottom", fontsize=12, color=SOLUK)
kaydet(fig, __file__)
