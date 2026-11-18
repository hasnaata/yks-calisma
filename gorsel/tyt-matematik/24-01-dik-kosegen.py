import sys; sys.path.insert(0, "tools")
from cizim import *

# Köşegenleri O'da dik kesişen ABCD. |OB| = 3 seçildi: |OA| = √55, |OC| = √7, |OD| = √114.
# |AB| = 8, |BC| = 4, |CD| = 11, |AD| = 13  (8² + 11² = 4² + 13² = 185).
O = np.array([0.0, 0.0])
A = np.array([0.0, np.sqrt(55)]); B = np.array([-3.0, 0.0]); C = np.array([0.0, -np.sqrt(7)]); D = np.array([np.sqrt(114), 0.0])
V = [A, B, C, D]
print("kenarlar:", [round(float(np.linalg.norm(V[i] - V[(i + 1) % 4])), 4) for i in range(4)])

fig, ax = sekil(5.8, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon(V, closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(A, C), color=KIRMIZI, lw=1.8); ax.plot(*zip(B, D), color=KIRMIZI, lw=1.8)
s = 0.45
ax.plot([s, s, 0], [0, s, s], color=KIRMIZI, lw=1.4)   # dik açı işareti
for k, v, d in (("A", A, (0, 0.45)), ("B", B, (-0.45, 0)), ("C", C, (0, -0.45)), ("D", D, (0.45, 0)), ("O", O, (-0.35, -0.4))):
    nokta(ax, *v, ""); ax.text(v[0] + d[0], v[1] + d[1], k, ha="center", va="center", fontsize=14)
merkez = sum(V) / 4
for P, Q, yazi, renk in ((A, B, "8", MAVI), (B, C, "4", YESIL), (C, D, "11", MAVI), (D, A, "x", YESIL)):
    m = (P + Q) / 2; n = np.array([-(Q - P)[1], (Q - P)[0]]); n = n / np.linalg.norm(n)
    if n @ (m - merkez) < 0: n = -n
    ax.text(*(m + 0.5 * n), yazi, color=renk, fontsize=14, ha="center", va="center", fontweight="bold")
ax.set_xlim(-4.2, D[0] + 1.0); ax.set_ylim(C[1] - 1.0, A[1] + 0.9)
kaydet(fig, __file__)
