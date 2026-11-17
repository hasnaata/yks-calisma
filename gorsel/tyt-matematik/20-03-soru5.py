import sys; sys.path.insert(0, "tools")
from cizim import *

# m(B) = 90°, m(C) = 28°, E [AC]'nin orta noktası. Beklenen m(ABE) = 62°.
B = np.array([0.0, 0.0]); C = np.array([8.0, 0.0]); A = np.array([0.0, 8 * np.tan(np.radians(28))])
E = (A + C) / 2
u, v = A - B, E - B
print("ABE", np.degrees(np.arccos(u @ v / np.linalg.norm(u) / np.linalg.norm(v))))

def centik(P1, Q1, renk):
    M = (P1 + Q1) / 2; d = (Q1 - P1) / np.linalg.norm(Q1 - P1); n = np.array([-d[1], d[0]])
    ax.plot(*zip(M - 0.18 * n, M + 0.18 * n), color=renk, lw=1.6)

fig, ax = sekil(6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, E), color=MAVI)
k = 0.35
ax.plot([k, k, 0], [0, k, k], color=YAZI, lw=1.3)
centik(A, E, SOLUK); centik(E, C, SOLUK)
nokta(ax, *A, "A", dx=-0.25, dy=0.25); nokta(ax, *B, "B", dx=-0.55, dy=-0.45); nokta(ax, *C, "C", dx=0.15, dy=-0.45)
nokta(ax, *E, "E", dx=0.05, dy=0.3)
aci(ax, C, A, B, r=1.5, ad="", renk=YAZI)
ax.text(5.75, 0.33, "28°", fontsize=13, va="center")
aci(ax, B, A, E, r=1.0, ad="", renk=KIRMIZI)
ax.text(0.45, 1.55, "x", color=KIRMIZI, fontsize=15, ha="center", va="center")
ax.set_xlim(-0.8, 8.6); ax.set_ylim(-0.8, A[1] + 0.6)
kaydet(fig, __file__)
