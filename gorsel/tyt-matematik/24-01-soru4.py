import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 4. ABCD: A=115, B=85, C=75, D=85. [BE] ve [CE] açıortay, m(BEC) = 100. Sorulan: m(D) = 2*100 - 115 = 85.
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
def centik(kose, p1, p2, r, n, renk):
    a1 = np.arctan2(*(p1 - kose)[::-1]); a2 = np.arctan2(*(p2 - kose)[::-1])
    if (a2 - a1) % (2 * np.pi) > np.pi: a1, a2 = a2, a1
    orta = a1 + ((a2 - a1) % (2 * np.pi)) / 2
    for k in range(n):
        t = orta + (k - (n - 1) / 2) * 0.12
        ax.plot([kose[0] + (r - 0.1) * np.cos(t), kose[0] + (r + 0.1) * np.cos(t)],
                [kose[1] + (r - 0.1) * np.sin(t), kose[1] + (r + 0.1) * np.sin(t)], color=renk, lw=1.6)

A, B, C, D = dortgen(115, 85, 75, 85, 6.0, 3.6)
E = kesis(B, u(42.5), C, u(180 - 37.5))
print("iç açılar:", [round(olc(*k), 2) for k in ((A, D, B), (B, A, C), (C, B, D), (D, C, A))], "BEC:", round(olc(E, B, C), 2))

fig, ax = sekil(5.6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(B, E), color=YESIL, lw=2); ax.plot(*zip(C, E), color=YESIL, lw=2)
for k, v, d in (("A", A, (-0.3, 0.25)), ("B", B, (-0.3, -0.3)), ("C", C, (0.3, -0.3)), ("D", D, (0.3, 0.25)), ("E", E, (0.0, 0.38))):
    nokta(ax, *v, ""); ax.text(v[0] + d[0], v[1] + d[1], k, ha="center", va="center", fontsize=14)
aci(ax, A, B, D, r=0.45, ad="115°", renk=MAVI)
aci(ax, D, A, C, r=0.45, ad="?", renk=KIRMIZI)
aci(ax, B, A, E, r=0.7, renk=SARI); aci(ax, B, E, C, r=0.7, renk=SARI)
centik(B, A, E, 0.7, 1, SARI); centik(B, E, C, 0.7, 1, SARI)
aci(ax, C, B, E, r=0.7, renk=SARI); aci(ax, C, E, D, r=0.7, renk=SARI)
centik(C, B, E, 0.7, 2, SARI); centik(C, E, D, 0.7, 2, SARI)
aci(ax, E, B, C, r=0.4, ad="100°", renk=YESIL)
ax.set_xlim(-0.7, C[0] + 0.7); ax.set_ylim(-0.6, max(A[1], D[1]) + 0.6)
kaydet(fig, __file__)
