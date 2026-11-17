import sys; sys.path.insert(0, "tools")
from cizim import *

# [AB] // [CD]. Kırılma noktası E sağda. m(BAE) = 35°, m(DCE) = 50°, m(AEC) = 85°.
# E'den çizilen kesikli paralel, E'deki açıyı 35° ve 50° olarak böler.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
h = 3.0
A = np.array([0.0, h]); B = np.array([5.6, h]); C = np.array([0.0, 0.0]); D = np.array([5.6, 0.0])
E = kesis(A, yon(-35), C, yon(50))
print("E", E, "açı", np.degrees(np.arccos(np.dot(A - E, C - E) / np.linalg.norm(A - E) / np.linalg.norm(C - E))))
fig, ax = sekil(6, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B), color=YAZI); ax.plot(*zip(C, D), color=YAZI)
ax.plot(4.0, h, ">", color=YAZI, markersize=7); ax.plot(4.0, 0, ">", color=YAZI, markersize=7)
ax.plot(*zip(A, E, C), color=YAZI)
ax.plot([E[0] - 1.6, E[0] + 1.6], [E[1], E[1]], color=SOLUK, lw=1.5, ls="--")
nokta(ax, *A, "A", dx=-0.45, dy=0.1); nokta(ax, *B, "B", dx=-0.1, dy=0.2)
nokta(ax, *C, "C", dx=-0.45, dy=-0.2); nokta(ax, *D, "D", dx=-0.1, dy=-0.55)
nokta(ax, *E, "E", dx=0.2, dy=0.1)
aci(ax, A, B, E, r=0.9, ad="35°", renk=MAVI)
aci(ax, C, D, E, r=0.8, ad="50°", renk=YESIL)
aci(ax, E, E + yon(180), A, r=0.75, ad="35°", renk=MAVI)
aci(ax, E, C, E + yon(180), r=0.6, ad="50°", renk=YESIL)
ax.set_xlim(-0.9, 6.2); ax.set_ylim(-0.9, h + 0.7)
kaydet(fig, __file__)
