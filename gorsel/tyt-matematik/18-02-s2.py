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

# Alıştırma 2: d1 // d2, kesen yatayla 70°. A'da sağ üst açı 3x − 20, B'de sağ üst açı x + 40 (yöndeş). x = 30, açı 70°.
h = 3.0; B = np.array([0.0, 0.0]); A = B + h / np.sin(np.radians(70)) * yon(70)
fig, ax = sekil(6, 4.4); ax.set_aspect("equal"); ax.axis("off")
paraleller(ax, h, -3.0, 5.0)
u = yon(70); ax.plot(*zip(B - 1.4 * u, A + 1.4 * u), color=YAZI)
nokta(ax, *A, "A", dx=-0.5, dy=0.15); nokta(ax, *B, "B", dx=-0.5, dy=0.15)
aci(ax, A, A + yon(0), A + u, r=0.55, renk=MAVI); ax.text(A[0] + 0.75, A[1] + 0.35, "3x − 20°", color=MAVI, va="center")
aci(ax, B, B + yon(0), B + u, r=0.55, renk=KIRMIZI); ax.text(B[0] + 0.75, B[1] + 0.35, "x + 40°", color=KIRMIZI, va="center")
ax.text(5.2, 1.5, "d₁ ∥ d₂", ha="right", color=SOLUK)
ax.set_xlim(-3.8, 5.4); ax.set_ylim(-1.6, h + 1.6)
kaydet(fig, __file__)
