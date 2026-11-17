import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = 3x − 2, f: A -> B, A = {1, 2, 3}, B = {1, 4, 7}. Solda f (A'dan B'ye), sağda f⁻¹ (B'den A'ya).
fig, ax = sekil(6.4, 3.4)
ax.axis("off"); ax.set_xlim(-0.3, 9.3); ax.set_ylim(-0.6, 4.7)
A, B = ["1", "2", "3"], ["1", "4", "7"]
def yk(i): return 2.85 - i * 0.85
def kume(x, ad, el):
    ax.add_patch(patches.Ellipse((x, 2.0), 1.2, 3.6, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.6))
    ax.text(x, 4.1, ad, ha="center", fontsize=16, color=MAVI, fontweight="bold")
    for i, e in enumerate(el): ax.text(x, yk(i), e, ha="center", va="center", fontsize=14)
def ok(x1, x2, i, renk):
    ax.annotate("", xy=(x2 - 0.38, yk(i)), xytext=(x1 + 0.38, yk(i)),
                arrowprops=dict(arrowstyle="->", color=renk, lw=1.7, shrinkA=0, shrinkB=0))
# sol: f
kume(0.8, "A", A); kume(3.6, "B", B)
for i in range(3): ok(0.8, 3.6, i, YESIL)
ax.text(2.2, 4.1, "f", ha="center", fontsize=16, color=YESIL, fontweight="bold")
# sağ: f⁻¹
kume(5.6, "B", B); kume(8.4, "A", A)
for i in range(3): ok(5.6, 8.4, i, SARI)
ax.text(7.0, 4.1, "f⁻¹", ha="center", fontsize=16, color=SARI, fontweight="bold")
ax.plot([4.6, 4.6], [0.0, 4.3], color=CIZGI, lw=1.2, ls="--")
ax.text(2.2, -0.35, "f(2) = 4", ha="center", fontsize=13, color=YESIL)
ax.text(7.0, -0.35, "f⁻¹(4) = 2", ha="center", fontsize=13, color=SARI)
kaydet(fig, __file__)
