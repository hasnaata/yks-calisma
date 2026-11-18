import sys; sys.path.insert(0, "tools")
from cizim import *

# ABCDE düzgün beşgen, ABFG kare (beşgenin dışında, [AB] ortak). [EG] çizilir.
# m(EAG) = 360 − 108 − 90 = 162, AEG ikizkenar -> m(AGE) = 9, x = m(EGF) = 90 + 9 = 99.
a = 2.4
A = np.array([0.0, 0.0]); B = np.array([a, 0.0])
def u(t): return np.array([np.cos(np.radians(t)), np.sin(np.radians(t))])
C = B + a * u(72); D = C + a * u(144); E = D + a * u(216)
F = B + a * u(-90); G = A + a * u(-90)
fig, ax = sekil(4.4, 5.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C, D, E], closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.4))
ax.add_patch(patches.Polygon([A, B, F, G], closed=True, facecolor=SARI_ACIK, edgecolor=YAZI, lw=2.4))
ax.plot(*zip(E, G), color=KIRMIZI, lw=2.2)
k = 0.28
for Pk, p1, p2 in ((F, G, B),):
    d1 = (p1 - Pk) / a; d2 = (p2 - Pk) / a
    ax.plot(*zip(Pk + k * d1, Pk + k * (d1 + d2), Pk + k * d2), color=SARI, lw=1.5)
aci(ax, G, F, E, r=0.62, ad="", renk=KIRMIZI)
ge = (E - G) / np.linalg.norm(E - G); gf = (F - G) / a
b = ge + gf; b /= np.linalg.norm(b)
ax.text(*(G + 1.0 * b), "x", color=KIRMIZI, ha="center", va="center", fontsize=15)
print("EGF", np.degrees(np.arccos(ge @ gf)), "AGE", np.degrees(np.arccos(ge @ ((A - G) / a))), "EAG", 360 - 108 - 90)
for k_, v, d in (("A", A, (0.3, -0.3)), ("B", B, (0.3, 0.18)), ("C", C, (0.32, 0)), ("D", D, (0, 0.32)), ("E", E, (-0.35, 0)),
                 ("F", F, (0.3, -0.25)), ("G", G, (-0.3, -0.25))):
    nokta(ax, *v, ""); ax.text(v[0] + d[0], v[1] + d[1], k_, ha="center", va="center", fontsize=14)
ax.set_xlim(E[0] - 0.7, C[0] + 0.7); ax.set_ylim(G[1] - 0.6, D[1] + 0.6)
kaydet(fig, __file__)
