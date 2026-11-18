import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 10. İçbükey ABCD: A=40, B=54, C=50, D=216 (180'den büyük iç açı). D'deki iç açı B'dekinin 4 katı.
# Saat yönünde dolaşım: her köşede (180 - iç açı) kadar sağa dönülür.
def u(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
fi = 63.0
A = np.array([0.0, 0.0]); B = A + 4.0 * u(fi); C = B + 4.0 * u(fi - 126)
u1, u2 = u(fi - 256), u(fi - 220)        # C->D ve D->A yönleri
s, t = np.linalg.solve(np.column_stack([u1, u2]), A - C)
D = C + s * u1
def olc(P, Q, R):
    v, w = Q - P, R - P
    return np.degrees(np.arccos(v @ w / np.linalg.norm(v) / np.linalg.norm(w)))
print("A, B, C:", round(olc(A, B, D), 2), round(olc(B, A, C), 2), round(olc(C, B, D), 2), "D (küçük taraf):", round(olc(D, A, C), 2), "D iç:", round(360 - olc(D, A, C), 2))

fig, ax = sekil(5.0, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.2))
for k, v, d in (("A", A, (-0.3, -0.2)), ("B", B, (0.0, 0.3)), ("C", C, (0.3, -0.2)), ("D", D, (0.0, -0.35))):
    nokta(ax, *v, ""); ax.text(v[0] + d[0], v[1] + d[1], k, ha="center", va="center", fontsize=14)
aci(ax, A, B, D, r=0.55, ad="40°", renk=MAVI)
aci(ax, C, D, B, r=0.7, ad="50°", renk=MAVI)
aci(ax, B, A, C, r=0.6, ad="x", renk=KIRMIZI)
a1 = np.degrees(np.arctan2(*(A - D)[::-1])); a2 = np.degrees(np.arctan2(*(C - D)[::-1]))
ax.add_patch(patches.Arc(D, 0.8, 0.8, theta1=a2, theta2=a1, color=KIRMIZI, lw=1.6))   # içten geçen büyük yay
ax.text(D[0], D[1] + 0.65, "4x", color=KIRMIZI, fontsize=13, ha="center", va="center")
ax.set_xlim(-0.6, C[0] + 0.6); ax.set_ylim(-0.6, B[1] + 0.6)
kaydet(fig, __file__)
