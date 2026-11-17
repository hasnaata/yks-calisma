import sys; sys.path.insert(0, "tools")
from cizim import *

# Eşit polinomlar: aynı dereceli terimlerin katsayıları karşılıklı eşlenir.
# (a+1)x² + 3x + c = 4x² + (b−2)x − 5  →  a+1 = 4, 3 = b−2, c = −5
fig, ax = sekil(6, 3.2)
ax.set_xlim(0, 10); ax.set_ylim(0, 4.6); ax.axis("off")
ust = [(2.3, r"$(a+1)x^{2}$"), (5.0, r"$+\ 3x$"), (7.9, r"$+\ c$")]
alt = [(2.3, r"$4x^{2}$"), (5.0, r"$+\ (b-2)x$"), (7.9, r"$-\ 5$")]
renk = [MAVI, YESIL, SARI]
for (xs, t), r in zip(ust, renk):
    ax.text(xs, 3.9, t, ha="center", va="center", fontsize=19, color=r)
for (xs, t), r in zip(alt, renk):
    ax.text(xs, 1.9, t, ha="center", va="center", fontsize=19, color=r)
ax.text(0.3, 2.9, "=", fontsize=22, va="center", color=YAZI)
for xs, r in zip([2.3, 5.0, 7.9], renk):
    ax.annotate("", xy=(xs, 2.35), xytext=(xs, 3.45), arrowprops=dict(arrowstyle="<->", color=r, lw=1.6))
for xs, t, r in zip([2.3, 5.0, 7.9], ["a + 1 = 4", "3 = b − 2", "c = −5"], renk):
    ax.text(xs, 0.6, t, ha="center", va="center", fontsize=14, color=r)
for xs, t, r in zip([2.3, 5.0, 7.9], ["a = 3", "b = 5", ""], renk):
    ax.text(xs, 0.05, t, ha="center", va="center", fontsize=14, color=r)
kaydet(fig, __file__)
