import sys; sys.path.insert(0, "tools")
from cizim import *

# Baba 35, oğul 7 (fark 28). t yıl sonra: baba 35 + t, oğul 7 + t.
# t = 0: 35/7 = 5 kat; t = 7: 42/14 = 3 kat; t = 21: 56/28 = 2 kat. Fark hep 28.
fig, ax = sekil(6, 4.2)
t = np.array([0, 24])
ax.plot(t, 35 + t, color=MAVI, lw=2.4)
ax.plot(t, 7 + t, color=YESIL, lw=2.4)
ax.text(24.3, 59, "baba", color=MAVI, va="center", fontsize=13, fontweight="bold")
ax.text(24.3, 31, "oğul", color=YESIL, va="center", fontsize=13, fontweight="bold")
for s, kat in ((0, "5 kat"), (7, "3 kat"), (21, "2 kat")):
    b, o = 35 + s, 7 + s
    ax.annotate("", xy=(s, b - 0.6), xytext=(s, o + 0.6), arrowprops=dict(arrowstyle="<->", color=KIRMIZI, lw=1.5))
    ax.plot([s, s], [b, o], "o", color=YAZI, markersize=5, zorder=5)
    ax.text(s + 0.5, (b + o) / 2, "28", color=KIRMIZI, fontsize=12, va="center", fontweight="bold")
    ax.text(s, b + 2.2, f"{b}", ha="center", va="bottom", color=MAVI, fontsize=12)
    ax.text(s + 0.5, o - 2.4, f"{o}", ha="left", va="top", color=YESIL, fontsize=12)
    ax.text(s, 70, kat, ha="center", va="bottom", color=YAZI, fontsize=12)
ax.set_xlim(-1.5, 27.5); ax.set_ylim(0, 74)
ax.set_xticks([0, 7, 14, 21]); ax.set_yticks([0, 20, 40, 60])
ax.set_xlabel("kaç yıl sonra"); ax.set_ylabel("yaş")
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.grid(True, color=CIZGI, linewidth=0.6, alpha=0.7); ax.set_axisbelow(True)
kaydet(fig, __file__)
