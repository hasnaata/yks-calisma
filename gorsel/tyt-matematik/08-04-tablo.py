import sys; sys.path.insert(0, "tools")
from cizim import *

# A = {1, 2, 3}, B = {4, 5}: A×B tablosu. Satır = birinci bileşen (A), sütun = ikinci bileşen (B).
# 3 satır × 2 sütun = 6 hücre = s(A×B).
fig, ax = sekil(4.6, 3.2)
ax.axis("off"); ax.set_xlim(0, 3); ax.set_ylim(0, 4); ax.invert_yaxis()
A, B = [1, 2, 3], [4, 5]
for i in range(4):
    for j in range(3):
        if i == 0 and j == 0:
            renk, yazi, rk = "white", "A × B", SOLUK
        elif i == 0:
            renk, yazi, rk = YESIL_ACIK, str(B[j - 1]), YESIL
        elif j == 0:
            renk, yazi, rk = MAVI_ACIK, str(A[i - 1]), MAVI
        else:
            renk, yazi, rk = "white", f"({A[i - 1]}, {B[j - 1]})", YAZI
        ax.add_patch(patches.Rectangle((j, i), 1, 1, facecolor=renk, edgecolor=CIZGI, lw=1.2))
        ax.text(j + 0.5, i + 0.5, yazi, ha="center", va="center", fontsize=14, color=rk,
                fontweight="bold" if (i == 0 or j == 0) else "normal")
ax.text(1.5, -0.25, "B (ikinci bileşen)", ha="center", va="bottom", fontsize=12, color=YESIL)
ax.text(-0.08, 2.5, "A (birinci bileşen)", ha="right", va="center", fontsize=12, color=MAVI, rotation=90)
kaydet(fig, __file__)
