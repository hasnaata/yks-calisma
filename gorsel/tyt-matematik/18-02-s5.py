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

# Alıştırma 5: [AB] // [CD]. m(BAE) = 40°, m(DCE) = x, m(AEC) = 2x + 5. x = 35, E'deki açı 75°.
h = 3.0
A = np.array([0.0, h]); B = np.array([5.8, h]); C = np.array([0.0, 0.0]); D = np.array([5.8, 0.0])
E = kesis(A, yon(-40), C, yon(35)); print("E", E, aciolc(E, A, C))
fig, ax = sekil(6, 4.0); ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B), color=YAZI); ax.plot(*zip(C, D), color=YAZI)
ax.plot(4.2, h, ">", color=YAZI, markersize=7); ax.plot(4.2, 0, ">", color=YAZI, markersize=7)
ax.plot(*zip(A, E, C), color=YAZI)
nokta(ax, *A, "A", dx=-0.45, dy=0.1); nokta(ax, *B, "B", dx=-0.1, dy=0.2)
nokta(ax, *C, "C", dx=-0.45, dy=-0.2); nokta(ax, *D, "D", dx=-0.1, dy=-0.55)
nokta(ax, *E, "E", dx=0.2, dy=-0.1)
aci(ax, A, B, E, r=1.0, ad="40°", renk=MAVI)
aci(ax, C, D, E, r=1.0, ad="x", renk=YESIL)
aci(ax, E, C, A, r=0.5, renk=KIRMIZI); ax.text(E[0] - 0.65, E[1], "2x + 5°", color=KIRMIZI, ha="right", va="center")
ax.set_xlim(-0.9, 6.4); ax.set_ylim(-0.9, h + 0.7)
kaydet(fig, __file__)
