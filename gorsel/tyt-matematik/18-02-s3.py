import sys; sys.path.insert(0, "tools")
from cizim import *
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
def aciolc(k, p, q):
    return np.degrees(np.arccos(np.dot(p - k, q - k) / np.linalg.norm(p - k) / np.linalg.norm(q - k)))
def paraleller(ax, h, x0, x1, adlar=("d₁", "d₂"), okx=None):
    for y, ad in ((h, adlar[0]), (0, adlar[1])):
        ax.plot([x0, x1], [y, y], color=YAZI); ax.plot(okx if okx is not None else x1 - 0.8, y, ">", color=YAZI, markersize=7)
        if ad: ax.text(x0 - 0.3, y, ad, ha="right", va="center")

# Alıştırma 3: [AB] // [CD]. m(ABC) = 3x − 5, m(BCD) = 2x + 15 (iç ters). x = 20, açı 55°.
h = 3.0; B = np.array([4.0, h]); A = np.array([0.2, h])
C = B + h / np.sin(np.radians(55)) * yon(235); D = np.array([5.4, 0.0])
print("B", aciolc(B, A, C), "C", aciolc(C, D, B))
fig, ax = sekil(6, 4.0); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B), color=YAZI); ax.plot(*zip(B, C), color=YAZI); ax.plot(*zip(C, D), color=YAZI)
ax.plot(2.0, h, ">", color=YAZI, markersize=7); ax.plot(3.6, 0, ">", color=YAZI, markersize=7)
nokta(ax, *A, "A", dx=-0.2, dy=0.2); nokta(ax, *B, "B", dx=0.0, dy=0.2)
nokta(ax, *C, "C", dx=-0.25, dy=-0.55); nokta(ax, *D, "D", dx=-0.1, dy=-0.55)
aci(ax, B, A, C, r=0.7, renk=MAVI); ax.text(B[0] - 1.25, B[1] - 0.5, "3x − 5°", color=MAVI, ha="right", va="center")
aci(ax, C, D, B, r=0.7, renk=KIRMIZI); ax.text(C[0] + 1.25, C[1] + 0.45, "2x + 15°", color=KIRMIZI, ha="left", va="center")
ax.set_xlim(-1.0, 6.0); ax.set_ylim(-0.9, h + 0.8)
kaydet(fig, __file__)
