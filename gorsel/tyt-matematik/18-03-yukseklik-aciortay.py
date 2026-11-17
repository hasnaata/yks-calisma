import sys; sys.path.insert(0, "tools")
from cizim import *

# m(B)=72, m(C)=38, m(A)=70. [AH] yükseklik, [AE] açıortay: m(HAE)=(72-38)/2=17.
B = np.array([0.0, 0.0]); C = np.array([7.0, 0.0])
t = 7 * np.sin(np.radians(38)) / np.sin(np.radians(70))
A = B + t * np.array([np.cos(np.radians(72)), np.sin(np.radians(72))])
H = np.array([A[0], 0.0])
# açıortay: BE/EC = AB/AC
AB, AC = np.linalg.norm(A - B), np.linalg.norm(A - C)
E = B + (C - B) * AB / (AB + AC)
v1, v2 = H - A, E - A
print("HAE", np.degrees(np.arccos(np.dot(v1, v2) / np.linalg.norm(v1) / np.linalg.norm(v2))))

fig, ax = sekil(6, 4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(B, C, A, B), color=YAZI)
ax.plot(*zip(A, H), color=MAVI, lw=1.8)
ax.plot(*zip(A, E), color=YESIL, lw=1.8)
k = 0.28
ax.plot([H[0] + k, H[0] + k, H[0]], [0, k, k], color=MAVI, lw=1.3)
nokta(ax, *A, "A", dx=-0.12, dy=0.2); nokta(ax, *B, "B", dx=-0.4, dy=-0.35); nokta(ax, *C, "C", dx=0.12, dy=-0.35)
nokta(ax, *H, "H", dx=-0.2, dy=-0.5, renk=MAVI); nokta(ax, *E, "E", dx=-0.1, dy=-0.5, renk=YESIL)
aci(ax, B, C, A, r=0.6, ad="72°", renk=YAZI)
aci(ax, C, A, B, r=0.9, ad="38°", renk=YAZI)
aci(ax, A, H, E, r=1.3, ad="", renk=KIRMIZI)
ax.text(A[0] + 0.33, A[1] - 1.75, "α", color=KIRMIZI, fontsize=13, ha="center")
ax.set_xlim(-0.7, 7.6); ax.set_ylim(-0.8, A[1] + 0.6)
kaydet(fig, __file__)
