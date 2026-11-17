import sys; sys.path.insert(0, "tools")
from cizim import *

# İkizkenar üçgen teoremi: |AB| = |AC| verilir (hipotez), B ve C açılarının eşitliği gösterilir (hüküm).
fig, ax = sekil(6, 4.2)
ax.axis("off"); ax.set_aspect("equal")
A, B, C = np.array([2.0, 3.4]), np.array([0.0, 0.0]), np.array([4.0, 0.0])
ax.plot(*zip(A, B, C, A), color=YAZI, lw=2)
def cizik(p, q):
    m = (p + q) / 2; d = q - p; n = np.array([-d[1], d[0]]) / np.linalg.norm(d) * 0.16
    ax.plot([m[0] - n[0], m[0] + n[0]], [m[1] - n[1], m[1] + n[1]], color=MAVI, lw=2.6)
cizik(A, B); cizik(A, C)
aci(ax, B, C, A, r=0.55, ad="?", renk=YESIL)
aci(ax, C, A, B, r=0.55, ad="?", renk=YESIL)
ax.text(A[0], A[1] + 0.15, "A", ha="center", va="bottom", fontsize=14)
ax.text(B[0] - 0.15, B[1] - 0.05, "B", ha="right", va="top", fontsize=14)
ax.text(C[0] + 0.15, C[1] - 0.05, "C", ha="left", va="top", fontsize=14)
# açıklama kutuları
ax.add_patch(patches.FancyBboxPatch((4.9, 2.15), 4.3, 1.1, boxstyle="round,pad=0.05,rounding_size=0.12", facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.5))
ax.text(7.05, 2.95, "Hipotez (verilen)", ha="center", va="center", fontsize=11, color=MAVI, fontweight="bold")
ax.text(7.05, 2.45, "|AB| = |AC|", ha="center", va="center", fontsize=13, color=YAZI)
ax.add_patch(patches.FancyBboxPatch((4.9, 0.35), 4.3, 1.1, boxstyle="round,pad=0.05,rounding_size=0.12", facecolor=YESIL_ACIK, edgecolor=YESIL, lw=1.5))
ax.text(7.05, 1.15, "Hüküm (gösterilecek)", ha="center", va="center", fontsize=11, color=YESIL, fontweight="bold")
ax.text(7.05, 0.65, "m(B) = m(C)", ha="center", va="center", fontsize=13, color=YAZI)
ax.set_xlim(-0.6, 9.4); ax.set_ylim(-0.5, 4.0)
kaydet(fig, __file__)
