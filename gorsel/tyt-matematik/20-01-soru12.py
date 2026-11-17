import sys; sys.path.insert(0, "tools")
from cizim import *

# Kâğıt ABC: m(A)=56, m(B)=72, m(C)=52. B ve C'nin kat izleri (iç açıortaylar) D'de kesişir: m(BDC)=90+28=118.
# A'nın kat izi [BC]'yi E'de keser: m(AEC) = 72 + 28 = 100.
B = np.array([0.0, 0.0]); C = np.array([6.5, 0.0])
t = 6.5 * np.sin(np.radians(52)) / np.sin(np.radians(56))
A = B + t * np.array([np.cos(np.radians(72)), np.sin(np.radians(72))])
a, b, c = np.linalg.norm(B - C), np.linalg.norm(A - C), np.linalg.norm(A - B)
D = (a * A + b * B + c * C) / (a + b + c)
E = B + (C - B) * c / (b + c)
def derece(p, k, q):
    v, w = p - k, q - k
    return np.degrees(np.arccos(np.dot(v, w) / np.linalg.norm(v) / np.linalg.norm(w)))
print("BDC", derece(B, D, C), "AEC", derece(A, E, C), "AEB", derece(A, E, B))

fig, ax = sekil(6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=SARI_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(B, D), color=MAVI, lw=1.8, ls="--"); ax.plot(*zip(C, D), color=MAVI, lw=1.8, ls="--")
ax.plot(*zip(A, E), color=YESIL, lw=1.8, ls="--")
nokta(ax, *A, "A", dx=-0.12, dy=0.22); nokta(ax, *B, "B", dx=-0.45, dy=-0.3); nokta(ax, *C, "C", dx=0.15, dy=-0.3)
nokta(ax, *D, "D", dx=0.2, dy=0.1, renk=MAVI); nokta(ax, *E, "E", dx=-0.1, dy=-0.5, renk=YESIL)
aci(ax, B, C, A, r=0.55, renk=YAZI)
ax.text(B[0] + 0.85, B[1] + 0.12, "72°", color=YAZI, fontsize=11, ha="left")
aci(ax, D, C, B, r=0.35, renk=MAVI)
ax.text(D[0] + 0.3, D[1] - 0.72, "118°", color=MAVI, fontsize=11, ha="left")
aci(ax, E, C, A, r=0.45, renk=YESIL)
ax.text(E[0] + 0.55, E[1] + 0.45, "?", color=YESIL, fontsize=14, ha="center")
ax.set_xlim(-0.7, 7.2); ax.set_ylim(-0.7, A[1] + 0.6)
kaydet(fig, __file__)
