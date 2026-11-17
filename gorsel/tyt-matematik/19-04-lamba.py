import sys; sys.path.insert(0, "tools")
from cizim import *

# Lamba direği |AL| = 6 m, kişi |BK| = 1,5 m, |AB| = 6 m. Gölge |BC| = x = 2 m.
# C, K, L doğrusal: CBK ~ CAL (oran 1/4).
A = np.array([0.0, 0.0]); L = np.array([0.0, 6.0]); B = np.array([6.0, 0.0]); K = np.array([6.0, 1.5]); C = np.array([8.0, 0.0])
print("K doğru üzerinde mi:", np.isclose((K - C)[0] * (L - C)[1] - (K - C)[1] * (L - C)[0], 0))
fig, ax = sekil(5.2, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-1, 9.3], [0, 0], color=SOLUK, lw=1.2)
ax.add_patch(patches.Polygon([A, L, C], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.plot(*zip(A, L), color=YAZI, lw=3)
ax.plot(L[0], L[1], "o", color=SARI, markersize=14, zorder=6)
ax.plot(*zip(L, C), color=SARI, lw=1.8, ls="--")
ax.plot(*zip(B, K), color=MAVI, lw=4)
ax.plot(*zip(B, C), color=YAZI, lw=5, alpha=0.75)
s = 0.35
ax.plot([A[0], A[0] + s, A[0] + s], [s, s, 0], color=YAZI, lw=1.2)
ax.plot([B[0], B[0] - s, B[0] - s], [s, s, 0], color=YAZI, lw=1.2)
nokta(ax, *L, "L", dx=-0.75, dy=0.1); nokta(ax, *A, "A", dx=-0.5, dy=-0.7)
nokta(ax, *B, "B", dx=-0.25, dy=-0.75); nokta(ax, *K, "K", dx=0.15, dy=0.25, renk=MAVI); nokta(ax, *C, "C", dx=0.1, dy=-0.75)
ax.text(-0.35, 3.0, "6 m", ha="right", va="center", fontsize=12)
ax.text(5.75, 0.8, "1,5 m", ha="right", va="center", color=MAVI, fontsize=12)
ax.text(3.0, -0.55, "6 m", ha="center", va="center", fontsize=12)
ax.text(7.0, -0.55, "x", ha="center", va="center", fontsize=13)
ax.text(7.2, 2.4, "ışın", ha="center", va="center", color=SARI, fontsize=11)
ax.set_xlim(-1.3, 9.3); ax.set_ylim(-1.1, 6.8)
kaydet(fig, __file__)
