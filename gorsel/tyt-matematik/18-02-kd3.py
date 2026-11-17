import sys; sys.path.insert(0, "tools")
from cizim import *

# Kendini dene 3: [AB] // [CD]. m(BAE) = 38°, m(DCE) = x, m(AEC) = 3x. Çözüm x = 19°, 3x = 57°.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
h = 3.0
A = np.array([0.0, h]); B = np.array([6.6, h]); C = np.array([0.0, 0.0]); D = np.array([6.6, 0.0])
E = kesis(A, yon(-38), C, yon(19))
print("E", E, "açı", np.degrees(np.arccos(np.dot(A - E, C - E) / np.linalg.norm(A - E) / np.linalg.norm(C - E))))
fig, ax = sekil(6, 3.8)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B), color=YAZI); ax.plot(*zip(C, D), color=YAZI)
ax.plot(2.0, h, ">", color=YAZI, markersize=7); ax.plot(2.0, 0, ">", color=YAZI, markersize=7)
ax.plot(*zip(A, E, C), color=YAZI)
nokta(ax, *A, "A", dx=-0.45, dy=0.1); nokta(ax, *B, "B", dx=-0.1, dy=0.2)
nokta(ax, *C, "C", dx=-0.45, dy=-0.2); nokta(ax, *D, "D", dx=-0.1, dy=-0.55)
nokta(ax, *E, "E", dx=0.2, dy=0.12)
aci(ax, A, B, E, r=1.2, ad="38°", renk=MAVI)
aci(ax, C, D, E, r=1.6, renk=YESIL); ax.text(*(C + 2.15 * yon(9.5)), "x", color=YESIL, ha="center", va="center", fontsize=12)
aci(ax, E, C, A, r=0.7, ad="3x", renk=KIRMIZI)
ax.set_xlim(-0.9, 7.2); ax.set_ylim(-0.9, h + 0.7)
kaydet(fig, __file__)
