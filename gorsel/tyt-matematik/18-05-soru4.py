import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 4: m(ABD)=60, m(ADB)=50, m(DBC)=45, m(BDC)=80 => m(A)=70, m(C)=55. En uzun: BC.
ABD, ADB, DBC, BDC = 60, 50, 45, 80; GOSTER_AC = False
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
B = np.array([0.0, 0.0]); D = np.array([5.0, 0.0])
A = kesis(B, yon(ABD), D, yon(180 - ADB))
C = kesis(B, yon(-DBC), D, yon(180 + BDC))
def olc(P, Q, R):
    u, v = Q - P, R - P; return np.degrees(np.arccos(u @ v / np.linalg.norm(u) / np.linalg.norm(v)))
print("A", olc(A, B, D), "C", olc(C, B, D))
for ad, P, Q in (("AB", A, B), ("AD", A, D), ("BD", B, D), ("BC", B, C), ("CD", C, D)):
    print(ad, round(np.linalg.norm(P - Q), 3))

fig, ax = sekil(5.2, 5.4)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(B, D), color=YAZI)
nokta(ax, *A, "A", dx=-0.12, dy=0.22); nokta(ax, *B, "B", dx=-0.45, dy=-0.12)
nokta(ax, *C, "C", dx=-0.12, dy=-0.5); nokta(ax, *D, "D", dx=0.18, dy=-0.12)
aci(ax, B, A, D, r=1.0, ad=f"{ABD}°", renk=MAVI)
aci(ax, B, D, C, r=0.75, ad=f"{DBC}°", renk=YESIL)
aci(ax, D, B, A, r=0.75, ad=f"{ADB}°", renk=SARI)
aci(ax, D, C, B, r=1.0, ad=f"{BDC}°", renk=KIRMIZI)
if GOSTER_AC:
    aci(ax, A, B, D, r=0.5, ad=f"{round(olc(A, B, D))}°", renk=SOLUK)
    aci(ax, C, B, D, r=0.5, ad=f"{round(olc(C, B, D))}°", renk=SOLUK)
xs = [p[0] for p in (A, B, C, D)]; ys = [p[1] for p in (A, B, C, D)]
ax.set_xlim(min(xs) - 0.8, max(xs) + 0.8); ax.set_ylim(min(ys) - 0.8, max(ys) + 0.6)
kaydet(fig, __file__)
