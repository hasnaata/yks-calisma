import sys; sys.path.insert(0, "tools")
from cizim import *

# 12 eş dilimli çark. Kırmızı: 1, 4, 6, 9, 11; mavi: 2, 5, 7, 12; sarı: 3, 8, 10.
renk = {}
for n in (1, 4, 6, 9, 11): renk[n] = (KIRMIZI, KIRMIZI_ACIK)
for n in (2, 5, 7, 12): renk[n] = (MAVI, MAVI_ACIK)
for n in (3, 8, 10): renk[n] = (SARI, SARI_ACIK)
koyu = {KIRMIZI: "#e8a49e", MAVI: "#9dbbe8", SARI: "#f0cf7a"}
fig, ax = sekil(6, 4.4)
ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-1.35, 3.1); ax.set_ylim(-1.3, 1.5)
for i in range(12):
    n = i + 1
    t1 = 105 - 30 * (i + 1); t2 = 105 - 30 * i     # ok 1'in ortasını gösterir, sayılar saat yönünde
    c, a = renk[n]
    ax.add_patch(patches.Wedge((0, 0), 1.15, t1, t2, facecolor=koyu[c], edgecolor="white", lw=2))
    orta = np.radians((t1 + t2) / 2)
    ax.text(0.78 * np.cos(orta), 0.78 * np.sin(orta), str(n), ha="center", va="center", fontsize=15,
            color=YAZI, fontweight="bold")
ax.add_patch(patches.Circle((0, 0), 1.15, facecolor="none", edgecolor=SOLUK, lw=1.4))
ax.add_patch(patches.Circle((0, 0), 0.08, color=YAZI, zorder=5))
ax.annotate("", xy=(0, 1.0), xytext=(0, 1.42), arrowprops=dict(arrowstyle="-|>", color=YAZI, lw=2.4, mutation_scale=22), zorder=6)
for j, (ad, c) in enumerate((("Kırmızı", KIRMIZI), ("Mavi", MAVI), ("Sarı", SARI))):
    y = 0.5 - 0.5 * j
    ax.add_patch(patches.Rectangle((1.6, y - 0.13), 0.3, 0.26, facecolor=koyu[c], edgecolor=c, lw=1.4))
    ax.text(2.0, y, ad, va="center", fontsize=14, color=YAZI)
kaydet(fig, __file__)
