import sys; sys.path.insert(0, "tools")
from cizim import *

# 8 eş dilimli çark. K: kırmızı {1, 3, 6}, M: mavi {2, 5, 8}, S: sarı {4, 7}.
RENK = {1: "K", 2: "M", 3: "K", 4: "S", 5: "M", 6: "K", 7: "S", 8: "M"}
DOLGU = {"K": (KIRMIZI_ACIK, KIRMIZI), "M": (MAVI_ACIK, MAVI), "S": (SARI_ACIK, SARI)}
AD = {"K": "kırmızı", "M": "mavi", "S": "sarı"}
fig, ax = sekil(5, 4.6)
ax.axis("off"); ax.set_aspect("equal")
for n in range(1, 9):
    t1 = 90 - 45 * n; t2 = t1 + 45          # 1 tepeden sağa, saat yönünde
    ac, koyu = DOLGU[RENK[n]]
    ax.add_patch(patches.Wedge((0, 0), 2, t1, t2, facecolor=ac, edgecolor=YAZI, lw=1.4))
    orta = np.radians((t1 + t2) / 2)
    ax.text(1.3 * np.cos(orta), 1.3 * np.sin(orta), str(n), ha="center", va="center", fontsize=18, color=koyu, fontweight="bold")
    ax.text(0.72 * np.cos(orta), 0.72 * np.sin(orta), RENK[n], ha="center", va="center", fontsize=11, color=koyu)
ax.add_patch(patches.Circle((0, 0), 0.12, color=YAZI))
ax.annotate("", xy=(0, 2.0), xytext=(0, 2.45), arrowprops=dict(arrowstyle="-|>", color=YAZI, lw=2))
for i, k in enumerate("KMS"):
    ac, koyu = DOLGU[k]
    ax.add_patch(patches.Rectangle((2.5, 0.6 - 0.65 * i), 0.4, 0.4, facecolor=ac, edgecolor=koyu, lw=1.4))
    ax.text(3.05, 0.8 - 0.65 * i, f"{k}: {AD[k]}", va="center", fontsize=13, color=YAZI)
ax.set_xlim(-2.2, 4.8); ax.set_ylim(-2.2, 2.6)
kaydet(fig, __file__)
