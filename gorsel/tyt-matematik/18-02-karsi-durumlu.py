import sys; sys.path.insert(0, "tools")
from cizim import *

# d1 // d2. Kesenin sağında, iki paralelin arasında kalan açılar karşı durumludur.
# x = 40 için: A'daki açı 2x + 20 = 100°, B'deki açı 3x − 40 = 80°; toplam 180°.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
h = 3.0
A = np.array([2.0, h]); B = A + h / np.sin(np.radians(80)) * yon(-100)
fig, ax = sekil(6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
for y, ad in ((h, "d₁"), (0, "d₂")):
    ax.plot([-2.6, 5.4], [y, y], color=YAZI); ax.plot(4.6, y, ">", color=YAZI, markersize=7)
    ax.text(-2.9, y, ad, ha="right", va="center")
u = yon(-100); ax.plot(*zip(A - 1.3 * u, B + 1.3 * u), color=YAZI)
nokta(ax, *A, "A", dx=-0.45, dy=0.15); nokta(ax, *B, "B", dx=-0.45, dy=-0.5)
aci(ax, A, A + yon(0), A + yon(-100), r=0.55, renk=MAVI)
aci(ax, B, B + yon(0), B + yon(80), r=0.55, renk=KIRMIZI)
ax.text(A[0] + 0.75, A[1] - 0.6, "2x + 20°", color=MAVI, ha="left", va="center")
ax.text(B[0] + 0.85, B[1] + 0.45, "3x − 40°", color=KIRMIZI, ha="left", va="center")
ax.text(5.6, 1.5, "d₁ ∥ d₂", ha="right", color=SOLUK)
ax.set_xlim(-3.3, 5.8); ax.set_ylim(-1.6, h + 1.6)
kaydet(fig, __file__)
