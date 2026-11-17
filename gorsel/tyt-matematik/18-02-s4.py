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

# Alıştırma 4: d1 // d2. Kesenin sağında iç bölgede: A'da 3x + 10 = 115°, B'de x + 30 = 65°. Karşı durumlu.
h = 3.0; A = np.array([2.2, h]); B = A + h / np.sin(np.radians(65)) * yon(-115)
fig, ax = sekil(6, 4.4); ax.set_aspect("equal"); ax.axis("off")
paraleller(ax, h, -2.4, 5.4)
u = yon(-115); ax.plot(*zip(A - 1.3 * u, B + 1.3 * u), color=YAZI)
nokta(ax, *A, "A", dx=-0.5, dy=0.15); nokta(ax, *B, "B", dx=-0.5, dy=-0.5)
aci(ax, A, A + yon(0), A + u, r=0.55, renk=MAVI); ax.text(A[0] + 0.75, A[1] - 0.6, "3x + 10°", color=MAVI, va="center")
aci(ax, B, B + yon(0), B - u, r=0.55, renk=KIRMIZI); ax.text(B[0] + 0.85, B[1] + 0.4, "x + 30°", color=KIRMIZI, va="center")
ax.text(5.6, 1.5, "d₁ ∥ d₂", ha="right", color=SOLUK)
ax.set_xlim(-3.2, 5.8); ax.set_ylim(-1.6, h + 1.6)
kaydet(fig, __file__)
