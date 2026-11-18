import sys; sys.path.insert(0, "tools")
from cizim import *

# ABCDE düzgün beşgen, [AC] köşegeni. m(ACD) = 108 − 36 = 72.
n = 5; r = 2.6
t = np.radians(234 + 72 * np.arange(n))   # A sol alt, B sağ alt, saat yönünün tersine
V = np.column_stack([r * np.cos(t), r * np.sin(t)])
A, B, C, D, E = V
fig, ax = sekil(4.6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon(V, closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.4))
ax.plot(*zip(A, C), color=KIRMIZI, lw=2.2)
for i in range(n):
    P, Q = V[i], V[(i + 1) % n]; m = (P + Q) / 2; d = (Q - P) / np.linalg.norm(Q - P); nr = np.array([-d[1], d[0]])
    ax.plot(*zip(m - 0.15 * nr, m + 0.15 * nr), color=SOLUK, lw=1.6)
for k, v in zip("ABCDE", V):
    u = v / np.linalg.norm(v); nokta(ax, *v, ""); ax.text(*(v + 0.42 * u), k, ha="center", va="center", fontsize=14)
aci(ax, C, A, D, r=0.6, ad="?", renk=KIRMIZI)
ua = (A - C) / np.linalg.norm(A - C); ud = (D - C) / np.linalg.norm(D - C); print("ACD", np.degrees(np.arccos(ua @ ud)))
ax.set_xlim(-3.4, 3.4); ax.set_ylim(-2.9, 3.3)
kaydet(fig, __file__)
