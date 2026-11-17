import sys; sys.path.insert(0, "tools")
from cizim import *

# A, O, B doğrusal; m(AOC)=70°, m(COB)=110°. [OD, AOC'nin; [OE, COB'nin açıortayı. m(DOE)=35+55=90°.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
O = np.array([0.0, 0.0]); L = 2.3
fig, ax = sekil(5.5, 3.2)
ax.set_aspect("equal"); ax.axis("off")
def isin(d, ad, renk=YAZI, ls="-", dxy=(0, 0)):
    P = O + L * yon(d)
    ax.annotate("", xy=P, xytext=O, arrowprops=dict(arrowstyle="-|>", color=renk, lw=2, ls=ls, mutation_scale=14))
    ax.text(*(P + 0.22 * yon(d) + np.array(dxy)), ad, color=renk, ha="center", va="center", fontsize=13)
isin(0, "A", dxy=(0, -0.3)); isin(180, "B", dxy=(0, -0.3)); isin(70, "C")
isin(35, "D", renk=MAVI); isin(125, "E", renk=KIRMIZI)
ax.plot(*O, "o", color=YAZI, markersize=6); ax.text(0, -0.35, "O", ha="center", fontsize=13)
for a1, a2, r, ad, renk in ((0, 35, 1.25, "35°", MAVI), (35, 70, 1.25, "35°", MAVI),
                            (70, 125, 1.0, "55°", KIRMIZI), (125, 180, 1.0, "55°", KIRMIZI)):
    ax.add_patch(patches.Arc(O, 2 * r, 2 * r, theta1=a1, theta2=a2, color=renk, lw=1.6))
    m = np.radians((a1 + a2) / 2)
    ax.text(*(O + (r + 0.32) * np.array([np.cos(m), np.sin(m)])), ad, color=renk, fontsize=12, ha="center", va="center")
# DOE dik açı işareti
s = 0.32; p1, p2 = s * yon(35), s * yon(125)
ax.plot([p1[0], p1[0] + p2[0], p2[0]], [p1[1], p1[1] + p2[1], p2[1]], color=YESIL, lw=1.6)
ax.set_xlim(-2.8, 2.8); ax.set_ylim(-0.6, 2.7)
kaydet(fig, __file__)
