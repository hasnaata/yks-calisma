import sys; sys.path.insert(0, "tools")
from cizim import *

# İki öğrencinin 5 denemedeki matematik netleri (sütun grafiği).
AYSE = [20, 24, 22, 26, 18]
CAN = [14, 30, 22, 26, 18]
fig, ax = sekil(6, 3.6)
x = np.arange(1, 6)
g = 0.36
ax.bar(x - g / 2, AYSE, g, color=MAVI, label="Ayşe")
ax.bar(x + g / 2, CAN, g, color=SARI_ACIK, edgecolor=SARI, lw=1.4, label="Can")
for xi, a, c in zip(x, AYSE, CAN):
    ax.text(xi - g / 2, a + 0.5, str(a), ha="center", va="bottom", fontsize=11, color=MAVI)
    ax.text(xi + g / 2, c + 0.5, str(c), ha="center", va="bottom", fontsize=11, color=SARI)
ax.set_xticks(x); ax.set_xticklabels([f"{i}." for i in x])
ax.set_xlabel("Deneme"); ax.set_ylabel("Net")
ax.set_ylim(0, 40); ax.set_yticks(range(0, 36, 5))
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.legend(frameon=False, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.06), fontsize=12)
kaydet(fig, __file__)
