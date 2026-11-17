import sys; sys.path.insert(0, "tools")
from cizim import *
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
def aciolc(k, p, q):
    return np.degrees(np.arccos(np.dot(p - k, q - k) / np.linalg.norm(p - k) / np.linalg.norm(q - k)))

# Alıştırma 12: [AB] // [CD], B ve D solda; E sağda. m(BAE) = 130°, m(DCE) = 120°, m(AEC) = 110°.
h = 3.0
A = np.array([3.0, h]); B = np.array([-0.5, h]); C = np.array([3.0, 0.0]); D = np.array([-0.5, 0.0])
E = kesis(A, yon(-50), C, yon(60)); print("E", E, aciolc(E, A, C), aciolc(A, B, E), aciolc(C, D, E))
fig, ax = sekil(6, 4.0); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, A), color=SARI, lw=4, solid_capstyle="butt"); ax.plot(*zip(D, C), color=SARI, lw=4, solid_capstyle="butt")
ax.plot(1.0, h, "<", color=YAZI, markersize=7); ax.plot(1.0, 0, "<", color=YAZI, markersize=7)
ax.plot(*zip(A, E, C), color=KIRMIZI, lw=2.4)
nokta(ax, *A, "A", dx=-0.15, dy=0.22); nokta(ax, *B, "B", dx=-0.15, dy=0.22)
nokta(ax, *C, "C", dx=-0.15, dy=-0.55); nokta(ax, *D, "D", dx=-0.15, dy=-0.55)
nokta(ax, *E, "E", dx=0.2, dy=-0.1)
aci(ax, A, B, E, r=0.45, renk=MAVI); ax.text(A[0] - 0.55, A[1] - 0.6, "130°", color=MAVI, ha="right", va="center")
aci(ax, C, E, D, r=0.45, renk=MAVI); ax.text(C[0] - 0.55, C[1] + 0.6, "120°", color=MAVI, ha="right", va="center")
aci(ax, E, A, C, r=0.45, ad="?", renk=YESIL)
ax.set_xlim(-1.0, 6.0); ax.set_ylim(-0.9, h + 0.7)
kaydet(fig, __file__)
