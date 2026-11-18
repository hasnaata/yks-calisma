import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 9. Park ABCD; köşegen yollar |AC| = 55 m, |BD| = 35 m (1 birim = 10 m). Kenar orta noktaları E, F, G, H ip ile çevrili.
# Ç(EFGH) = 55 + 35 = 90 m. Şekilde uzunluk yazılı değildir.
def u(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
A, C = 2.3 * u(100), -3.2 * u(100)
B, D = -1.4 * u(15), 2.1 * u(15)
E, F, G, H = (A + B) / 2, (B + C) / 2, (C + D) / 2, (D + A) / 2
uz = lambda P, Q: float(np.linalg.norm(P - Q))
print("AC, BD (x10 m):", uz(A, C) * 10, uz(B, D) * 10, "ip:", 10 * (uz(E, F) + uz(F, G) + uz(G, H) + uz(H, E)))

fig, ax = sekil(4.6, 4.8)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=YESIL_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(A, C), color=SARI, lw=2.0, ls="--"); ax.plot(*zip(B, D), color=SARI, lw=2.0, ls="--")
ax.add_patch(patches.Polygon([E, F, G, H], closed=True, facecolor="none", edgecolor=KIRMIZI, lw=2.2))
merkez = (A + B + C + D) / 4
for k, v in zip("ABCDEFGH", (A, B, C, D, E, F, G, H)):
    d = v - merkez; d = d / np.linalg.norm(d)
    nokta(ax, *v, "", renk=KIRMIZI if k in "EFGH" else YAZI)
    ax.text(*(v + 0.35 * d), k, ha="center", va="center", fontsize=14, color=KIRMIZI if k in "EFGH" else YAZI)
ax.set_xlim(B[0] - 0.6, D[0] + 0.6); ax.set_ylim(C[1] - 0.6, A[1] + 0.6)
kaydet(fig, __file__)
