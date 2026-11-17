import sys; sys.path.insert(0, "tools")
from cizim import *

# İki ayna O'da 50° açıyla birleşir. Işın 1. aynaya 70° açıyla gelir ve 70° açıyla yansır,
# 2. aynaya çarpar (OPQ üçgeninde Q açısı 60°) ve aynı açıyla yansır.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
O = np.array([0.0, 0.0]); P = np.array([4.5, 0.0])
m2 = yon(50)
Q = kesis(P, yon(110), O, m2)
print("Q açısı", np.degrees(np.arccos(np.dot(O - Q, P - Q) / np.linalg.norm(O - Q) / np.linalg.norm(P - Q))))
gel = P + 2.6 * yon(70)                    # gelen ışının başlangıcı
# Q'dan çıkan ışın: 2. aynayla (O'dan uzak yönde) 60°
cik_yon = yon(2 * 50 - 110)               # yansıma: ayna doğrultusu 50°, gelen 110° → çıkan −10°
cik = Q + 2.8 * cik_yon

fig, ax = sekil(6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
for u, L in ((yon(0), 7.0), (m2, 6.6)):
    ax.plot(*zip(O, O + L * u), color=MAVI, lw=4, solid_capstyle="butt")
ax.text(*(O + 6.9 * yon(0) + np.array([0, -0.45])), "1. ayna", color=MAVI, fontsize=12, ha="right")
ax.text(*(O + 6.5 * m2 + np.array([-0.25, 0])), "2. ayna", color=MAVI, fontsize=12, ha="right")
ok = dict(arrowstyle="-|>", color=KIRMIZI, lw=2, mutation_scale=16)
ax.annotate("", xy=P, xytext=gel, arrowprops=ok)
ax.annotate("", xy=Q, xytext=P, arrowprops=ok)
ax.annotate("", xy=cik, xytext=Q, arrowprops=ok)
nokta(ax, *O, "O", dx=-0.4, dy=-0.35); nokta(ax, *P, "P", dx=-0.1, dy=-0.5); nokta(ax, *Q, "Q", dx=-0.45, dy=0.05)
aci(ax, O, P, Q, r=0.8, ad="50°", renk=YAZI)
aci(ax, P, O + np.array([7, 0]), gel, r=0.6, ad="70°", renk=KIRMIZI)
aci(ax, P, Q, O, r=0.6, ad="70°", renk=KIRMIZI)
aci(ax, Q, Q + m2, cik, r=0.6, ad="?", renk=YESIL)
ax.set_xlim(-0.6, 7.3); ax.set_ylim(-0.8, 5.6)
kaydet(fig, __file__)
