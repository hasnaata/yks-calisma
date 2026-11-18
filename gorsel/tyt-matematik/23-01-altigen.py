import sys; sys.path.insert(0, "tools")
from cizim import *

# ABCDEF düzgün altıgen, [AC] köşegeni. ABC ikizkenar: m(B)=120°, m(BAC)=m(BCA)=30°. m(BCD)=120° -> m(ACD)=90°.
n = 6; r = 3.0
t = np.radians(210 + 60 * np.arange(n))     # A sol alt, saat yönünün tersine
V = np.column_stack([r * np.cos(t), r * np.sin(t)])
A, B, C, D, E, F = V
fig, ax = sekil(4.8, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.add_patch(patches.Polygon(V, closed=True, fill=False, edgecolor=YAZI, lw=2.4))
ax.plot(*zip(A, C), color=KIRMIZI, lw=2.2)
def centik(P, Q):
    m = (P + Q) / 2; d = (Q - P) / np.linalg.norm(Q - P); nrm = np.array([-d[1], d[0]])
    ax.plot(*zip(m - 0.16 * nrm, m + 0.16 * nrm), color=SOLUK, lw=1.6)
for i in range(n): centik(V[i], V[(i + 1) % n])
for k, v in zip("ABCDEF", V):
    u = v / np.linalg.norm(v); nokta(ax, *v, ""); ax.text(*(v + 0.45 * u), k, ha="center", va="center", fontsize=14)
aci(ax, B, C, A, r=0.5, ad="120°", renk=MAVI)
for P, Q, R in ((A, B, C), (C, A, B)):
    aci(ax, P, Q, R, r=1.1, ad="", renk=SARI)
    b = (Q - P) / np.linalg.norm(Q - P) + (R - P) / np.linalg.norm(R - P); b /= np.linalg.norm(b)
    ax.text(*(P + 1.65 * b), "30°", color=SARI, ha="center", va="center", fontsize=12)
# C'de dik açı işareti (CA ile CD arası)
ua = (A - C) / np.linalg.norm(A - C); ud = (D - C) / np.linalg.norm(D - C); k = 0.4
ax.plot(*zip(C + k * ua, C + k * ua + k * ud, C + k * ud), color=KIRMIZI, lw=1.6)
ax.text(*(C + 1.0 * (ua + ud) / np.linalg.norm(ua + ud)), "90°", color=KIRMIZI, ha="center", va="center", fontsize=12)
print("ACD:", np.degrees(np.arccos(ua @ ud)))
ax.set_xlim(-3.7, 3.7); ax.set_ylim(-3.5, 3.5)
kaydet(fig, __file__)
