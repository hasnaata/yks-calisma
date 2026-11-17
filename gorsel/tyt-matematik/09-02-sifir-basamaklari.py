import sys; sys.path.insert(0, "tools")
from cizim import *

# n! sayısının sonundaki sıfır sayısı (n = 0, ..., 30). 25'te 2 birden artar.
z = lambda n: sum(n // 5 ** k for k in range(1, 4))
fig, ax = sekil(6, 3.4)
ns = list(range(0, 31))
ax.step(ns, [z(n) for n in ns], where="post", color=MAVI, lw=2.2)
for n in (5, 10, 15, 20, 25, 30):
    nokta(ax, n, z(n), renk=KIRMIZI if n == 25 else MAVI)
ax.annotate("", xy=(25, 6), xytext=(25, 4), arrowprops=dict(arrowstyle="->", color=KIRMIZI, lw=1.6))
ax.text(24.2, 5.0, "+2", ha="right", va="center", color=KIRMIZI, fontsize=13, fontweight="bold")
ax.text(13, 5.6, "25 = 5 · 5 iki tane 5 getirir:\n5 sıfır olan n! yoktur.", ha="center", va="center", fontsize=11, color=KIRMIZI)
ax.set_xlim(0, 31.5); ax.set_ylim(0, 7.8)
ax.set_xticks([0, 5, 10, 15, 20, 25, 30]); ax.set_yticks(range(0, 8))
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.grid(True, color=CIZGI, linewidth=0.6, alpha=0.7); ax.set_axisbelow(True)
ax.set_xlabel("n"); ax.set_ylabel("n! sonundaki sıfır")
kaydet(fig, __file__)
