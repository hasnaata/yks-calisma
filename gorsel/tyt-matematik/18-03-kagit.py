import sys; sys.path.insert(0, "tools")
from cizim import *

# Kâğıt ABC üçgeni: m(B)=65, m(C)=70, m(A)=45. A köşesi [DE] boyunca kesilir; geriye BCED dörtgeni kalır.
B = np.array([0.0, 0.0]); C = np.array([6.0, 0.0])
t = 6 * np.sin(np.radians(70)) / np.sin(np.radians(45))
A = B + t * np.array([np.cos(np.radians(65)), np.sin(np.radians(65))])
D = B + 0.62 * (A - B); E = C + 0.5 * (A - C)

fig, ax = sekil(5.5, 4.8)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([B, C, E, D], closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.2))
ax.add_patch(patches.Polygon([D, E, A], closed=True, facecolor=KIRMIZI_ACIK, edgecolor=KIRMIZI, lw=1.6, ls="--"))
ax.text(*(D + E + A) / 3 + np.array([0, -0.1]), "kesilen\nparça", color=KIRMIZI, fontsize=11, ha="center", va="center")
nokta(ax, *A, "A", dx=-0.12, dy=0.2, renk=KIRMIZI); nokta(ax, *B, "B", dx=-0.4, dy=-0.3); nokta(ax, *C, "C", dx=0.12, dy=-0.3)
nokta(ax, *D, "D", dx=-0.45, dy=0.0); nokta(ax, *E, "E", dx=0.18, dy=0.0)
aci(ax, B, C, A, r=0.7, ad="65°", renk=MAVI)
aci(ax, C, A, B, r=0.7, ad="70°", renk=MAVI)
aci(ax, D, B, E, r=0.4, ad="", renk=YESIL)
aci(ax, E, D, C, r=0.4, ad="", renk=YESIL)
ax.set_xlim(-0.7, 6.7); ax.set_ylim(-0.6, A[1] + 0.6)
kaydet(fig, __file__)
