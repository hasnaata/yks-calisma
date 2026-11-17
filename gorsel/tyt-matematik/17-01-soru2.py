import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 2: koşu kulübü, haftalık mesafe (km), genişlik 5.
GRUPLAR = ['5–9', '10–14', '15–19', '20–24', '25–29']
FREK = [4, 9, 7, 3, 2]
VURGU = []   # koyu renkli sütunlar (sıra no, 0'dan)
fig, ax = sekil(5.8, 3.6)
k = len(GRUPLAR)
for i, f in enumerate(FREK):
    sol = 0.8 + i
    ax.bar(sol, f, width=1, align="edge", color=MAVI if i in VURGU else MAVI_ACIK, edgecolor=MAVI, lw=1.4, zorder=3)
    ax.hlines(f, 0, sol, color=SOLUK, lw=0.8, ls=":", zorder=1)
    ax.text(sol + 0.5, -0.04 * max(FREK), GRUPLAR[i], ha="center", va="top", fontsize=12, color=YAZI)
# yatay eksen: başta veri olmayan bölge zikzakla gösterilir
z = [0, 0.18, 0.28, 0.38, 0.48, 0.58, 0.68]
zy = [0, 0, 0.025, -0.025, 0.025, -0.025, 0]
ax.plot(z, [v * max(FREK) for v in zy], color=SOLUK, lw=1.2, clip_on=False, zorder=4)
ax.annotate("", xy=(k + 1.3, 0), xytext=(0.68, 0), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.2))
ax.set_xlim(0, k + 1.35); ax.set_ylim(0, max(FREK) * 1.12)
ax.set_xticks([]); ax.set_yticks(sorted(set(FREK)))
for s in ("top", "right", "bottom"): ax.spines[s].set_visible(False)
ax.set_xlabel('Haftalık mesafe (km)', labelpad=26)
ax.set_ylabel('Üye sayısı')
kaydet(fig, __file__)
