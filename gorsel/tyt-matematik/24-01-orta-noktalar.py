import sys; sys.path.insert(0, "tools")
from cizim import *

# ABCD: |AC| = 10, |BD| = 14. E, F, G, H sırasıyla [AB], [BC], [CD], [DA] kenarlarının orta noktaları.
# EFGH paralelkenar: |EF| = |HG| = 10/2 = 5, |FG| = |EH| = 14/2 = 7, Ç(EFGH) = 24 = |AC| + |BD|.
def u(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
A, C = 4 * u(100), -6 * u(100)
B, D = -5 * u(15), 9 * u(15)
E, F, G, H = (A + B) / 2, (B + C) / 2, (C + D) / 2, (D + A) / 2
uz = lambda P, Q: float(np.linalg.norm(P - Q))
print("AC, BD:", uz(A, C), uz(B, D), "EF, FG, GH, HE:", [round(uz(*k), 4) for k in ((E, F), (F, G), (G, H), (H, E))])

fig, ax = sekil(5.8, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(A, C), color=MAVI, lw=1.6, ls="--"); ax.plot(*zip(B, D), color=YESIL, lw=1.6, ls="--")
ax.add_patch(patches.Polygon([E, F, G, H], closed=True, facecolor="none", edgecolor=KIRMIZI, lw=2.2))
merkez = (A + B + C + D) / 4
for k, v in zip("ABCDEFGH", (A, B, C, D, E, F, G, H)):
    d = v - merkez; d = d / np.linalg.norm(d)
    nokta(ax, *v, "", renk=KIRMIZI if k in "EFGH" else YAZI)
    ax.text(*(v + 0.5 * d), k, ha="center", va="center", fontsize=14, color=KIRMIZI if k in "EFGH" else YAZI)
def etiket(P, Q, yazi, renk, k=0.45):
    m = (P + Q) / 2; n = np.array([-(Q - P)[1], (Q - P)[0]]); n = n / np.linalg.norm(n)
    if n @ (m - merkez) < 0: n = -n           # EFGH'nin dışına doğru
    ax.text(*(m + k * n), yazi, color=renk, fontsize=13, ha="center", va="center", fontweight="bold")
etiket(E, F, "5", MAVI); etiket(H, G, "5", MAVI); etiket(F, G, "7", YESIL); etiket(E, H, "7", YESIL)
ax.text(*(A + 0.86 * (C - A) + np.array([0.3, 0.0])), "10", color=MAVI, fontsize=12, ha="left", va="center")
ax.text(*(B + 0.9 * (D - B) + np.array([0.0, -0.4])), "14", color=YESIL, fontsize=12, ha="center", va="center")
ax.set_xlim(B[0] - 0.9, D[0] + 0.9); ax.set_ylim(C[1] - 0.9, A[1] + 0.9)
kaydet(fig, __file__)
