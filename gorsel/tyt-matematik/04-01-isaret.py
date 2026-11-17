import sys; sys.path.insert(0, "tools")
from cizim import *

# (−2)^n için n = 1, ..., 6: tek kuvvet negatif, çift kuvvet pozitif.
fig, ax = sekil(6, 3.8)
n = np.arange(1, 7)
d = (-2.0) ** n
renk = [KIRMIZI if v < 0 else YESIL for v in d]
ax.bar(n, d, width=0.6, color=renk, zorder=3)
ax.axhline(0, color=SOLUK, lw=1.2, zorder=4)
for k, v in zip(n, d):
    ax.text(k, v + (4 if v > 0 else -4), str(int(v)).replace("-", "−"), ha="center", va="bottom" if v > 0 else "top", fontsize=13, color=YAZI)
ax.set_xticks(n, [f"$(-2)^{k}$".replace("-", "−") for k in n], fontsize=13)
ax.tick_params(axis="x", length=0, pad=8)
ax.set_yticks([])
for s in ("top", "right", "left", "bottom"): ax.spines[s].set_visible(False)
ax.set_ylim(-48, 82)
ax.text(0.45, 70, "çift kuvvet: +", color=YESIL, fontsize=13, fontweight="bold")
ax.text(0.45, -42, "tek kuvvet: −", color=KIRMIZI, fontsize=13, fontweight="bold")
kaydet(fig, __file__)
