import sys; sys.path.insert(0, "tools")
from cizim import *
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
def aciolc(k, p, q):
    return np.degrees(np.arccos(np.dot(p - k, q - k) / np.linalg.norm(p - k) / np.linalg.norm(q - k)))

# Alıştırma 8 (masa lambası): lamba başı [AB] masaya [CD] paralel. m(BAE) = x = 45°, m(DCE) = 50°, m(AEC) = 95°.
h = 3.2
A = np.array([0.6, h]); B = np.array([3.4, h]); C = np.array([0.0, 0.0]); D = np.array([5.6, 0.0])
E = kesis(A, yon(-45), C, yon(50)); print("E", E, aciolc(E, A, C))
fig, ax = sekil(6, 4.2); ax.set_aspect("equal"); ax.axis("off")
ax.plot([-0.6, 6.2], [0, 0], color=SOLUK, lw=5, solid_capstyle="butt")
ax.text(6.2, -0.45, "masa", color=SOLUK, ha="right", va="top", fontsize=12)
ax.plot(*zip(A, B), color=SARI, lw=5, solid_capstyle="butt")
ax.text(B[0] + 0.15, B[1] + 0.05, "lamba başı", color=SARI, ha="left", va="center", fontsize=12)
ax.plot(*zip(A, E, C), color=YAZI, lw=3)
nokta(ax, *A, "A", dx=-0.45, dy=0.1); nokta(ax, *B, "B", dx=-0.1, dy=0.25)
nokta(ax, *C, "C", dx=-0.45, dy=0.15); nokta(ax, *E, "E", dx=0.2, dy=-0.1)
ax.text(D[0] - 0.4, 0.2, "D", ha="center", va="bottom")
aci(ax, A, B, E, r=0.8, ad="x", renk=MAVI)
aci(ax, C, D, E, r=0.8, ad="50°", renk=YESIL)
aci(ax, E, C, A, r=0.5, ad="95°", renk=KIRMIZI)
ax.set_xlim(-0.9, 6.4); ax.set_ylim(-1.0, h + 0.7)
kaydet(fig, __file__)
