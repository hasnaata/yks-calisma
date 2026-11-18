import sys; sys.path.insert(0, "tools")
from cizim import *

# ABCD: A=120, B=90, C=70, D=80. [BE] ve [CE], B ve C açılarının açıortayları. m(BEC) = (120+80)/2 = 100.
def u(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def dortgen(a, b, c, d, L, p):
    B = np.array([0.0, 0.0]); C = np.array([L, 0.0]); A = p * u(b)
    u1, u2 = u(180 - c), u(360 - c - d)
    s, t = np.linalg.solve(np.column_stack([u1, u2]), A - C)
    return A, B, C, C + s * u1
def olc(P, Q, R):
    v, w = Q - P, R - P
    return np.degrees(np.arccos(v @ w / np.linalg.norm(v) / np.linalg.norm(w)))
def kesis(P, d1, Q, d2):
    s, t = np.linalg.solve(np.column_stack([d1, -d2]), Q - P); return P + s * d1

A, B, C, D = dortgen(120, 90, 70, 80, 6.0, 3.4)
E = kesis(B, u(45), C, u(180 - 35))
print("iç açılar:", [round(olc(*k), 2) for k in ((A, D, B), (B, A, C), (C, B, D), (D, C, A))], "BEC:", round(olc(E, B, C), 2))

u_ = lambda v: v / np.linalg.norm(v)
fig, ax = sekil(5.6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(B, E), color=YESIL, lw=2); ax.plot(*zip(C, E), color=YESIL, lw=2)
for k, v, d in (("A", A, (-0.3, 0.25)), ("B", B, (-0.3, -0.3)), ("C", C, (0.3, -0.3)), ("D", D, (0.3, 0.25)), ("E", E, (0.0, 0.38))):
    nokta(ax, *v, ""); ax.text(v[0] + d[0], v[1] + d[1], k, ha="center", va="center", fontsize=14)
aci(ax, A, B, D, r=0.45, renk=MAVI)
ma = (u_(B - A) + u_(D - A)); ma = ma / np.linalg.norm(ma)
ax.text(A[0] + 1.0 * ma[0], A[1] + 1.0 * ma[1], "120°", color=MAVI, fontsize=12, ha="center", va="center")
aci(ax, D, A, C, r=0.45, ad="80°", renk=MAVI)
# B'de iki eş parça (tek yay), C'de iki eş parça (çift yay)
aci(ax, B, A, E, r=0.7, ad="45°", renk=SARI); aci(ax, B, E, C, r=0.7, ad="45°", renk=SARI)
for r in (0.75, 0.85):
    aci(ax, C, B, E, r=r, renk=KIRMIZI); aci(ax, C, E, D, r=r, renk=KIRMIZI)
ax.text(*(C + 1.45 * u(180 - 17.5)), "35°", color=KIRMIZI, fontsize=12, ha="center", va="center")
ax.text(*(C + 1.45 * u(180 - 52.5)), "35°", color=KIRMIZI, fontsize=12, ha="center", va="center")
aci(ax, E, B, C, r=0.4, ad="100°", renk=YESIL)
ax.set_xlim(-0.7, C[0] + 0.7); ax.set_ylim(-0.6, max(A[1], D[1]) + 0.6)
kaydet(fig, __file__)
