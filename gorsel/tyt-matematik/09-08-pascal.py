import sys; sys.path.insert(0, "tools")
from cizim import *
from math import comb

# Pascal üçgeni, n = 0..6. Satır 4'teki 4 ve 6 toplanıp satır 5'teki 10'u verir.
# Sağda satır toplamları (2 üzeri n).
fig, ax = sekil(6.4, 4.4)
ax.set_aspect("equal"); ax.axis("off")
N, dx, dy, r = 6, 0.62, 0.78, 0.27
vurgu = {(4, 1): MAVI, (4, 2): MAVI, (5, 2): YESIL}
for n in range(N + 1):
    yy = -n * dy
    ax.text(-N * dx / 2 - 1.05, yy, f"n = {n}", ha="right", va="center", fontsize=11, color=SOLUK)
    for k in range(n + 1):
        xx = (k - n / 2) * dx
        renk = vurgu.get((n, k))
        ax.add_patch(patches.Circle((xx, yy), r, facecolor=(MAVI_ACIK if renk == MAVI else YESIL_ACIK) if renk else "white",
                                    edgecolor=renk or CIZGI, lw=1.8 if renk else 1.1, zorder=2))
        ax.text(xx, yy, str(comb(n, k)), ha="center", va="center", fontsize=11 if comb(n, k) < 10 else 10.5,
                color=renk or YAZI, fontweight="bold" if renk else "normal", zorder=3)
    ax.text(N * dx / 2 + 0.75, yy, str(2 ** n), ha="left", va="center", fontsize=11, color=SARI)
ax.text(N * dx / 2 + 0.75, dy * 0.95, "Toplam", ha="left", va="center", fontsize=11, color=SARI, fontweight="bold")
# 4 + 6 = 10 okları
hedef = ((2 - 5 / 2) * dx, -5 * dy)
for k in (1, 2):
    bas = ((k - 2) * dx, -4 * dy)
    ax.annotate("", xy=(hedef[0] + (bas[0] - hedef[0]) * 0.36, hedef[1] + (bas[1] - hedef[1]) * 0.36),
                xytext=(bas[0] + (hedef[0] - bas[0]) * 0.36, bas[1] + (hedef[1] - bas[1]) * 0.36),
                arrowprops=dict(arrowstyle="->", color=YESIL, lw=1.6), zorder=4)
ax.text(-N * dx / 2 - 0.3, -N * dy - 0.7, "4 + 6 = 10", ha="left", va="center", fontsize=12, color=YESIL)
ax.set_xlim(-N * dx / 2 - 1.9, N * dx / 2 + 1.9); ax.set_ylim(-N * dy - 1.0, 0.9)
kaydet(fig, __file__)
