import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 5. ABCD: A=130, B=85, C=70, D=75. [BF], B'nin; [DE], D'nin açıortayı; B, E, F doğrusal. m(DEF) = (130-70)/2 = 30.
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

A, B, C, D = dortgen(130, 85, 70, 75, 6.0, 3.2)
yDA = (A - D) / np.linalg.norm(A - D); yDC = (C - D) / np.linalg.norm(C - D)
E = kesis(B, u(42.5), D, yDA + yDC)
F = kesis(B, u(42.5), C, D - C)
print("iç açılar:", [round(olc(*k), 2) for k in ((A, D, B), (B, A, C), (C, B, D), (D, C, A))],
      "DEF:", round(olc(E, D, F), 2), "F CD üzerinde mi:", 0 <= (F - C) @ (D - C) / ((D - C) @ (D - C)) <= 1,
      "E BF arasında mı:", 0 < (E - B) @ (F - B) / ((F - B) @ (F - B)) < 1)

fig, ax = sekil(5.6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(B, F), color=YESIL, lw=2); ax.plot(*zip(D, E), color=YESIL, lw=2)
for k, v, d in (("A", A, (-0.3, 0.25)), ("B", B, (-0.3, -0.3)), ("C", C, (0.3, -0.3)), ("D", D, (0.3, 0.25)),
                ("E", E, (-0.32, 0.18)), ("F", F, (0.32, 0.05))):
    nokta(ax, *v, ""); ax.text(v[0] + d[0], v[1] + d[1], k, ha="center", va="center", fontsize=14)
aci(ax, A, B, D, r=0.45, renk=MAVI)
ya = (B - A) / np.linalg.norm(B - A) + (D - A) / np.linalg.norm(D - A); ax.text(*(A + 0.95 * ya / np.linalg.norm(ya)), "130°", color=MAVI, fontsize=12, ha="center", va="center")
aci(ax, C, D, B, r=0.5, ad="70°", renk=MAVI)
aci(ax, B, A, F, r=0.6, renk=SARI); aci(ax, B, F, C, r=0.6, renk=SARI)
centik(B, A, F, 0.6, 1, SARI); centik(B, F, C, 0.6, 1, SARI)
aci(ax, D, A, E, r=0.7, renk=KIRMIZI); aci(ax, D, E, C, r=0.7, renk=KIRMIZI)
centik(D, A, E, 0.7, 2, KIRMIZI); centik(D, E, C, 0.7, 2, KIRMIZI)
aci(ax, E, D, F, r=0.7, renk=YESIL)
m = np.radians((np.degrees(np.arctan2(*(D - E)[::-1])) + np.degrees(np.arctan2(*(F - E)[::-1]))) / 2)
ax.text(E[0] + 1.15 * np.cos(m), E[1] + 1.15 * np.sin(m), "x", color=YESIL, fontsize=14, ha="center", va="center")
ax.set_xlim(-1.0, C[0] + 0.7); ax.set_ylim(-0.6, max(A[1], D[1]) + 0.6)
kaydet(fig, __file__)
