import sys; sys.path.insert(0, "tools")
from cizim import *
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
def aciolc(k, p, q):
    return np.degrees(np.arccos(np.dot(p - k, q - k) / np.linalg.norm(p - k) / np.linalg.norm(q - k)))

# Alıştırma 9: tavan (d1) // zemin (d2). İpler A'dan B ve C'ye; AB zeminle 65°, AC zeminle 45°. m(BAC) = 70°.
h = 3.0; A = np.array([2.0, h])
B = A + h / np.sin(np.radians(65)) * yon(-115); C = A + h / np.sin(np.radians(45)) * yon(-45)
print("BAC", aciolc(A, B, C))
fig, ax = sekil(6, 4.0); ax.set_aspect("equal"); ax.axis("off")
for y, ad in ((h, "tavan"), (0, "zemin")):
    ax.plot([-0.8, 6.4], [y, y], color=YAZI); ax.plot(5.6, y, ">", color=YAZI, markersize=7)
    ax.text(-1.0, y, ad, ha="right", va="center", fontsize=12, color=SOLUK)
ax.plot(*zip(B, A, C), color=MAVI)
nokta(ax, *A, "A", dx=-0.15, dy=0.22); nokta(ax, *B, "B", dx=-0.2, dy=-0.55); nokta(ax, *C, "C", dx=-0.1, dy=-0.55)
aci(ax, B, B + yon(0), A, r=0.55, ad="65°", renk=YESIL)
aci(ax, C, C + yon(180), A, r=0.6, ad="45°", renk=YESIL)
aci(ax, A, B, C, r=0.5, ad="?", renk=KIRMIZI)
ax.set_xlim(-2.4, 6.6); ax.set_ylim(-0.9, h + 0.7)
kaydet(fig, __file__)
