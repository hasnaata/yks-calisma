import sys; sys.path.insert(0, "tools")
from cizim import *

# Tahta |AB| = 3,6 m, A yerde. Destek |SD| = 0,5 m, |AS| = 1,5 m (tahta boyunca).
# sin(eğim) = 0,5/1,5 = 1/3, B'nin yüksekliği |BH| = 3,6/3 = 1,2 m. ADS ~ AHB.
sn = 0.5 / 1.5; cs = np.sqrt(1 - sn**2); u = np.array([cs, sn])
A = np.array([0.0, 0.0]); S = A + 1.5 * u; B = A + 3.6 * u
D = np.array([S[0], 0.0]); H = np.array([B[0], 0.0])
print("S yük.", S[1], "B yük.", B[1])
fig, ax = sekil(5.4, 3.0)
ax.set_aspect("equal"); ax.axis("off")
ax.plot([-0.4, 3.9], [0, 0], color=SOLUK, lw=1.2)
ax.plot(*zip(A, B), color=SARI, lw=4.5, solid_capstyle="round")
ax.plot(*zip(D, S), color=YAZI, lw=3.5)
ax.plot(*zip(B, H), color=MAVI, lw=1.8, ls="--")
s = 0.09
ax.plot([D[0] - s, D[0] - s, D[0]], [0, s, s], color=YAZI, lw=1.2)
ax.plot([H[0] - s, H[0] - s, H[0]], [0, s, s], color=YAZI, lw=1.2)
nokta(ax, *A, "A", dx=-0.2, dy=-0.25); nokta(ax, *S, "S", dx=-0.1, dy=0.12); nokta(ax, *D, "D", dx=-0.06, dy=-0.25)
nokta(ax, *B, "B", dx=0.07, dy=0.05); nokta(ax, *H, "H", dx=-0.05, dy=-0.25)
n = np.array([-sn, cs]) * 0.17
ax.text(*((A + S) / 2 + n), "1,5 m", ha="center", va="center", fontsize=12, rotation=np.degrees(np.arcsin(sn)))
ax.text(*((S + B) / 2 + n), "2,1 m", ha="center", va="center", fontsize=12, rotation=np.degrees(np.arcsin(sn)))
ax.text(D[0] + 0.07, 0.22, "0,5 m", ha="left", va="center", fontsize=12)
ax.text(H[0] + 0.07, B[1] / 2, "?", ha="left", va="center", color=MAVI, fontsize=14)
ax.set_xlim(-0.4, 3.9); ax.set_ylim(-0.35, 1.45)
kaydet(fig, __file__)
