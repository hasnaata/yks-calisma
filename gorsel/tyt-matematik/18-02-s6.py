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

# Alıştırma 6: d1 // d2. m(DAB) = 110°, [AC, DAB açısının açıortayı. m(ACB) = 55°.
h = 3.0; A = np.array([1.0, h]); D = np.array([5.4, h])
B = A + h / np.sin(np.radians(70)) * yon(-110); C = A + h / np.sin(np.radians(55)) * yon(-55)
print("ACB", aciolc(C, A, B), "ABC", aciolc(B, A, C), "BAC", aciolc(A, B, C))
fig, ax = sekil(6, 4.0); ax.set_aspect("equal"); ax.axis("off")
paraleller(ax, h, -1.6, 6.0, okx=5.0)
ax.plot(*zip(A + 0.9 * (A - B) / np.linalg.norm(A - B), B - 0.9 * (A - B) / np.linalg.norm(A - B)), color=YAZI)
ax.plot(*zip(A, C), color=YESIL)
nokta(ax, *A, "A", dx=-0.15, dy=0.22); nokta(ax, *D, "D", dx=-0.1, dy=0.22)
nokta(ax, *B, "B", dx=-0.5, dy=-0.5); nokta(ax, *C, "C", dx=0.0, dy=-0.5)
aci(ax, A, D, B, r=0.9, renk=MAVI); ax.text(*(A + 1.45 * yon(-22)), "110°", color=MAVI, ha="center", va="center")
aci(ax, A, D, C, r=0.45, renk=YESIL); aci(ax, A, C, B, r=0.5, renk=YESIL)
aci(ax, C, A, B, r=0.6, ad="?", renk=KIRMIZI)
ax.set_xlim(-2.4, 6.2); ax.set_ylim(-1.0, h + 0.8)
kaydet(fig, __file__)
