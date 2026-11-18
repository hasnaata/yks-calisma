import sys; sys.path.insert(0, "tools")
from cizim import *

# ABCD dörtgeni: iç açılar A=95, B=70, C=110, D=85 (mavi). [AC] köşegeni (kesikli) dörtgeni iki üçgene böler.
# Her köşede bir kenar uzatılmış; dış açılar A=85, B=110, C=70, D=95 (kırmızı), toplam 360.
def u(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def dortgen(a, b, c, d, L, p):
    B = np.array([0.0, 0.0]); C = np.array([L, 0.0]); A = p * u(b)
    u1, u2 = u(180 - c), u(360 - c - d)          # C->D ve D->A yönleri
    s, t = np.linalg.solve(np.column_stack([u1, u2]), A - C)
    return A, B, C, C + s * u1
def olc(P, Q, R):
    v, w = Q - P, R - P
    return np.degrees(np.arccos(v @ w / np.linalg.norm(v) / np.linalg.norm(w)))

A, B, C, D = dortgen(95, 70, 110, 85, 5.0, 4.0)
print("iç açılar:", [round(olc(*k), 2) for k in ((A, D, B), (B, A, C), (C, B, D), (D, C, A))])

fig, ax = sekil(5.6, 5.0)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(A, C), color=SOLUK, lw=1.5, ls="--")
# Uzantılar: A->B->C->D->A yönünde gelen kenar köşenin ötesine uzatılır
uz = {}
for P, Q in ((D, A), (A, B), (B, C), (C, D)):
    e = Q + 1.4 * (Q - P) / np.linalg.norm(Q - P); uz[tuple(Q)] = e
    ax.plot(*zip(Q, e), color=KIRMIZI, lw=1.5, ls="--")
for k, v, d in (("A", A, (-0.35, 0.25)), ("B", B, (-0.35, -0.3)), ("C", C, (0.35, -0.3)), ("D", D, (0.35, 0.25))):
    nokta(ax, *v, ""); ax.text(v[0] + d[0], v[1] + d[1], k, ha="center", va="center", fontsize=14)
aci(ax, A, B, D, r=0.5, ad="", renk=MAVI); ax.text(*(A + 1.0 * u(-22)), "95°", color=MAVI, fontsize=12, ha="center", va="center")
aci(ax, B, C, A, r=0.55, ad="70°", renk=MAVI)
aci(ax, C, D, B, r=0.5, ad="", renk=MAVI); ax.text(*(C + 1.05 * u(164)), "110°", color=MAVI, fontsize=12, ha="center", va="center")
aci(ax, D, A, C, r=0.5, ad="85°", renk=MAVI)
aci(ax, A, uz[tuple(A)], B, r=0.45, ad="85°", renk=KIRMIZI)
aci(ax, B, uz[tuple(B)], C, r=0.45, ad="110°", renk=KIRMIZI)
aci(ax, C, uz[tuple(C)], D, r=0.45, ad="70°", renk=KIRMIZI)
aci(ax, D, uz[tuple(D)], A, r=0.45, ad="95°", renk=KIRMIZI)
xs = [p[0] for p in list(uz.values()) + [A, B, C, D]]; ys = [p[1] for p in list(uz.values()) + [A, B, C, D]]
ax.set_xlim(min(xs) - 0.5, max(xs) + 0.5); ax.set_ylim(min(ys) - 0.5, max(ys) + 0.5)
kaydet(fig, __file__)
