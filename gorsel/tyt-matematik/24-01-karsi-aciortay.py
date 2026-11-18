import sys; sys.path.insert(0, "tools")
from cizim import *

# ABCD: A=110, B=100, C=70, D=80. [BF], B açısının; [DE], D açısının açıortayı; B, E, F doğrusal.
# m(BED) = 160, m(DEF) = (110 - 70)/2 = 20.
def u(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def dortgen(a, b, c, d, L, p):
    B = np.array([0.0, 0.0]); C = np.array([L, 0.0]); A = p * u(b)
    u1, u2 = u(180 - c), u(360 - c - d)
    s, t = np.linalg.solve(np.column_stack([u1, u2]), A - C)
    return A, B, C, C + s * u1
def olc(P, Q, R):
    v, w = Q - P, R - P
    return np.degrees(np.arccos(v @ w / np.linalg.norm(v) / np.linalg.norm(w)))
def centik(kose, p1, p2, r, n, renk):
    """kose'deki p1-p2 açı yayının ortasına n tane küçük çentik (eş açı işareti)."""
    a1 = np.arctan2(*(p1 - kose)[::-1]); a2 = np.arctan2(*(p2 - kose)[::-1])
    if (a2 - a1) % (2 * np.pi) > np.pi: a1, a2 = a2, a1
    orta = a1 + ((a2 - a1) % (2 * np.pi)) / 2
    for k in range(n):
        t = orta + (k - (n - 1) / 2) * 0.12
        ax.plot([kose[0] + (r - 0.1) * np.cos(t), kose[0] + (r + 0.1) * np.cos(t)],
                [kose[1] + (r - 0.1) * np.sin(t), kose[1] + (r + 0.1) * np.sin(t)], color=renk, lw=1.6)
def kesis(P, d1, Q, d2):
    s, t = np.linalg.solve(np.column_stack([d1, -d2]), Q - P); return P + s * d1

A, B, C, D = dortgen(110, 100, 70, 80, 6.0, 3.6)
yDA = (A - D) / np.linalg.norm(A - D); yDC = (C - D) / np.linalg.norm(C - D)
E = kesis(B, u(50), D, yDA + yDC)
F = kesis(B, u(50), C, D - C)          # B açıortayı [CD] kenarını F'de keser
print("iç açılar:", [round(olc(*k), 2) for k in ((A, D, B), (B, A, C), (C, B, D), (D, C, A))],
      "BED:", round(olc(E, B, D), 2), "DEF:", round(olc(E, D, F), 2), "E-F:", np.linalg.norm(F - E))

u_ = lambda v: v / np.linalg.norm(v)
fig, ax = sekil(5.6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C, D], closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(B, F), color=YESIL, lw=2); ax.plot(*zip(D, E), color=YESIL, lw=2)
for k, v, d in (("A", A, (-0.3, 0.25)), ("B", B, (-0.3, -0.3)), ("C", C, (0.3, -0.3)), ("D", D, (0.3, 0.25)),
                ("E", E, (-0.3, 0.2)), ("F", F, (0.32, 0.05))):
    nokta(ax, *v, ""); ax.text(v[0] + d[0], v[1] + d[1], k, ha="center", va="center", fontsize=14)
aci(ax, A, B, D, r=0.45, renk=MAVI)
ma = (u_(B - A) + u_(D - A)); ma = ma / np.linalg.norm(ma)
ax.text(A[0] + 1.0 * ma[0], A[1] + 1.0 * ma[1], "110°", color=MAVI, fontsize=12, ha="center", va="center")
aci(ax, C, D, B, r=0.5, ad="70°", renk=MAVI)
aci(ax, B, A, F, r=0.6, renk=SARI); aci(ax, B, F, C, r=0.6, renk=SARI)
centik(B, A, F, 0.6, 1, SARI); centik(B, F, C, 0.6, 1, SARI)
aci(ax, D, A, E, r=0.6, renk=KIRMIZI); aci(ax, D, E, C, r=0.6, renk=KIRMIZI)
centik(D, A, E, 0.6, 2, KIRMIZI); centik(D, E, C, 0.6, 2, KIRMIZI)
aci(ax, E, D, F, r=0.9, renk=YESIL)
m = np.radians((np.degrees(np.arctan2(*(D - E)[::-1])) + np.degrees(np.arctan2(*(F - E)[::-1]))) / 2)
ax.text(E[0] + 1.6 * np.cos(m), E[1] + 1.6 * np.sin(m), "20°", color=YESIL, fontsize=12, ha="center", va="center")
ax.set_xlim(-1.0, C[0] + 0.7); ax.set_ylim(-0.6, max(A[1], D[1]) + 0.6)
kaydet(fig, __file__)
