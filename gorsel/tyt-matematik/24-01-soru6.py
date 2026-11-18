import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 6. Köşegenleri O'da dik kesişen ABCD. |OB| = 4 seçildi: |OA| = √105, |OC| = 3, |OD| = √91.
# |AB| = 11, |BC| = 5, |CD| = 10, |AD| = 14  (11² + 10² = 5² + 14² = 221).
O = np.array([0.0, 0.0])
A = np.array([0.0, np.sqrt(105)]); B = np.array([-4.0, 0.0]); C = np.array([0.0, -3.0]); D = np.array([np.sqrt(91), 0.0])
V = [A, B, C, D]
print("kenarlar:", [round(float(np.linalg.norm(V[i] - V[(i + 1) % 4])), 4) for i in range(4)])

fig, ax = sekil(5.0, 4.8)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon(V, closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(A, C), color=SOLUK, lw=1.6, ls="--"); ax.plot(*zip(B, D), color=SOLUK, lw=1.6, ls="--")
s = 0.55
ax.plot([s, s, 0], [0, s, s], color=SOLUK, lw=1.4)
for k, v, d in (("A", A, (0, 0.5)), ("B", B, (-0.5, 0)), ("C", C, (0, -0.5)), ("D", D, (0.5, 0)), ("O", O, (-0.4, -0.45))):
    nokta(ax, *v, ""); ax.text(v[0] + d[0], v[1] + d[1], k, ha="center", va="center", fontsize=14)
merkez = sum(V) / 4
for P, Q, yazi, renk in ((A, B, "11", MAVI), (B, C, "5", MAVI), (C, D, "10", MAVI), (D, A, "?", KIRMIZI)):
    m = (P + Q) / 2; n = np.array([-(Q - P)[1], (Q - P)[0]]); n = n / np.linalg.norm(n)
    if n @ (m - merkez) < 0: n = -n
    ax.text(*(m + 0.6 * n), yazi, color=renk, fontsize=14, ha="center", va="center", fontweight="bold")
ax.set_xlim(-5.4, D[0] + 1.1); ax.set_ylim(C[1] - 1.1, A[1] + 1.0)
kaydet(fig, __file__)
