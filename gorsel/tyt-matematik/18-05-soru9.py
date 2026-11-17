import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 9: D, [BC] üzerinde. m(B)=55, m(BAD)=60, m(DAC)=25 => m(ADB)=65, m(ADC)=115, m(C)=40.
# Sıralama: |DC| < |AD| < |BD| < |AB| < |AC|.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
B = np.array([0.0, 0.0]); C = np.array([6.0, 0.0])
A = kesis(B, yon(55), C, yon(180 - 40))
D = kesis(A, yon(55 + 180 + 60), B, yon(0))   # AB yönünden 60° dönerek AD
def olc(P, Q, R):
    u, v = Q - P, R - P; return np.degrees(np.arccos(u @ v / np.linalg.norm(u) / np.linalg.norm(v)))
print("BAD", olc(A, B, D), "DAC", olc(A, D, C), "ADB", olc(D, A, B), "C", olc(C, A, B))
for ad, P, Q in (("DC", D, C), ("AD", A, D), ("BD", B, D), ("AB", A, B), ("AC", A, C)):
    print(ad, round(np.linalg.norm(P - Q), 3))

fig, ax = sekil(5.4, 3.8)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI); ax.plot(*zip(A, D), color=YAZI)
nokta(ax, *A, "A", dx=-0.12, dy=0.22); nokta(ax, *B, "B", dx=-0.42, dy=-0.12)
nokta(ax, *C, "C", dx=0.15, dy=-0.12); nokta(ax, *D, "D", dx=-0.12, dy=-0.45)
aci(ax, B, A, C, r=0.6, ad="55°", renk=MAVI)
aci(ax, A, B, D, r=0.85, ad="60°", renk=YESIL)
aci(ax, A, D, C, r=1.25, ad="25°", renk=KIRMIZI)
ax.set_xlim(-0.7, 6.7); ax.set_ylim(-0.7, A[1] + 0.6)
kaydet(fig, __file__)
