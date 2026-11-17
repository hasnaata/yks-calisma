import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders: aynı veri iki farklı dikey eksenle. A 52, B 48, C 56. Solda eksen 0'dan, sağda 45'ten başlar.
ad = ["A", "B", "C"]; v = [52, 48, 56]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.2, 3.4))
for ax, alt, baslik in ((a1, 0, "Eksen 0'dan başlıyor"), (a2, 45, "Eksen 45'ten başlıyor")):
    ax.bar(ad, [x - alt for x in v], bottom=alt, width=0.55, color=MAVI_ACIK, edgecolor=MAVI, lw=1.4, zorder=3)
    for i, x in enumerate(v): ax.text(i, x + (0.4 if alt else 1.5), str(x), ha="center", va="bottom", fontsize=12)
    ax.set_ylim(alt, 64 if alt == 0 else 58.5)
    ax.set_yticks(range(0, 61, 20) if alt == 0 else range(45, 58, 3))
    ax.set_title(baslik, fontsize=12, color=SOLUK)
    for k in ("top", "right"): ax.spines[k].set_visible(False)
    ax.grid(axis="y", color=CIZGI, lw=0.6); ax.set_axisbelow(True)
fig.tight_layout(w_pad=2)
kaydet(fig, __file__)
