import sys; sys.path.insert(0, "tools")
from cizim import *

# 5 kız, 4 erkek; 4 kişilik ekipler erkek sayısına göre: C(4,k)·C(5,4−k) = 5, 40, 60, 20, 1 (toplam 126).
fig, ax = sekil(6, 3.8)
k = [0, 1, 2, 3, 4]
say = [5, 40, 60, 20, 1]
renk = [KIRMIZI] + [YESIL] * 4
dolgu = [KIRMIZI_ACIK] + [YESIL_ACIK] * 4
ax.bar(k, say, width=0.62, color=dolgu, edgecolor=renk, linewidth=1.6)
for x, s, r in zip(k, say, renk):
    ax.text(x, s + 2, str(s), ha="center", va="bottom", fontsize=14, color=r, fontweight="bold")
ax.set_xticks(k)
ax.set_xticklabels(["0", "1", "2", "3", "4"], fontsize=13)
ax.set_xlabel("Ekipteki erkek sayısı", fontsize=13)
ax.set_yticks([])
for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
ax.set_ylim(0, 82)
ax.text(2.0, 76, "Toplam: 126 ekip", ha="center", fontsize=13, color=YAZI)
ax.text(0, 20, "çıkar", ha="center", fontsize=12, color=KIRMIZI)
ax.text(3.2, 52, "En az 1 erkek:\n126 − 5 = 121", ha="left", va="center", fontsize=13, color=YESIL)
kaydet(fig, __file__)
