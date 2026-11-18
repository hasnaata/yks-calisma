import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 8. Uçurtma: [AC] ve [BD] çıtaları O'da dik. |OA| = 2 seçildi: |OB| = √45, |OC| = √76, |OD| = √5.
# İp parçaları: |AB| = 7, |BC| = 11, |CD| = 9, |DA| = 3 (toplam 30). Şekilde yalnızca 7 ve 9 yazılı.
O = np.array([0.0, 0.0])
A = np.array([0.0, 2.0]); B = np.array([-np.sqrt(45), 0.0]); C = np.array([0.0, -np.sqrt(76)]); D = np.array([np.sqrt(5), 0.0])
V = [A, B, C, D]
print("ipler:", [round(float(np.linalg.norm(V[i] - V[(i + 1) % 4])), 4) for i in range(4)])

fig, ax = sekil(4.6, 5.2)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon(V, closed=True, facecolor=SARI_ACIK, edgecolor=KIRMIZI, lw=2.0))
ax.plot(*zip(A, C), color=SARI, lw=3.2, solid_capstyle="round"); ax.plot(*zip(B, D), color=SARI, lw=3.2, solid_capstyle="round")
s = 0.5
ax.plot([s, s, 0], [0, s, s], color=YAZI, lw=1.4)
for k, v, d in (("A", A, (0, 0.45)), ("B", B, (-0.45, 0)), ("C", C, (0, -0.45)), ("D", D, (0.45, 0)), ("O", O, (-0.35, -0.4))):
    nokta(ax, *v, ""); ax.text(v[0] + d[0], v[1] + d[1], k, ha="center", va="center", fontsize=14)
merkez = sum(V) / 4
for P, Q, yazi in ((A, B, "7"), (C, D, "9")):
    m = (P + Q) / 2; n = np.array([-(Q - P)[1], (Q - P)[0]]); n = n / np.linalg.norm(n)
    if n @ (m - O) < 0: n = -n
    ax.text(*(m + 0.5 * n), yazi, color=KIRMIZI, fontsize=14, ha="center", va="center", fontweight="bold")
ax.set_xlim(B[0] - 0.9, D[0] + 0.9); ax.set_ylim(C[1] - 0.8, A[1] + 0.8)
kaydet(fig, __file__)
