import sys; sys.path.insert(0, "tools")
from cizim import *

# Direkler: |AB| = 6 m (x=0), |CD| = 3 m (x=9). İpler A->D ve C->B, P'de kesişir.
# h = 6*3/(6+3) = 2, P'nin x'i = 6.
A = np.array([0.0, 6.0]); B = np.array([0.0, 0.0]); C = np.array([9.0, 3.0]); D = np.array([9.0, 0.0])
t = np.linalg.solve(np.array([D - A, -(B - C)]).T, C - A); P = A + t[0] * (D - A); H = np.array([P[0], 0.0])
print("P", P)
fig, ax = sekil(5.0, 3.8)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-1, 10], [0, 0], color=SOLUK, lw=1.2)
ax.plot(*zip(A, B), color=YAZI, lw=3.5); ax.plot(*zip(C, D), color=YAZI, lw=3.5)
ax.plot(*zip(A, D), color=MAVI, lw=1.8); ax.plot(*zip(C, B), color=YESIL, lw=1.8)
ax.plot(*zip(P, H), color=KIRMIZI, lw=1.8, ls="--")
s = 0.3
ax.plot([H[0] - s, H[0] - s, H[0]], [0, s, s], color=YAZI, lw=1.1)
nokta(ax, *A, "A", dx=-0.65, dy=0.0); nokta(ax, *B, "B", dx=-0.65, dy=-0.55); nokta(ax, *C, "C", dx=0.2, dy=0.0)
nokta(ax, *D, "D", dx=0.2, dy=-0.55); nokta(ax, *P, "P", dx=-0.2, dy=0.35, renk=KIRMIZI); nokta(ax, *H, "H", dx=-0.2, dy=-0.65)
ax.text(-0.3, 3.0, "6 m", ha="right", va="center", fontsize=12)
ax.text(9.3, 1.5, "3 m", ha="left", va="center", fontsize=12)
ax.text(H[0] + 0.15, 0.9, "h", ha="left", va="center", color=KIRMIZI, fontsize=14)
ax.annotate("", xy=(9, -1.0), xytext=(0, -1.0), arrowprops=dict(arrowstyle="<->", color=YAZI, lw=1.2))
ax.text(4.5, -1.4, "9 m", ha="center", va="center", fontsize=12)
ax.set_xlim(-1.3, 10.2); ax.set_ylim(-1.8, 6.6)
kaydet(fig, __file__)
