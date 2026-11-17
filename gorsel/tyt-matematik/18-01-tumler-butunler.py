import sys; sys.path.insert(0, "tools")
from cizim import *

# Sol: komşu tümler açılar 35° + 55° = 90°. Sağ: komşu bütünler açılar 35° + 145° = 180°.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def isin(ax, O, d, L=2.0):
    P = O + L * yon(d)
    ax.annotate("", xy=P, xytext=O, arrowprops=dict(arrowstyle="-|>", color=YAZI, lw=2, mutation_scale=14))
    return P
def etiket(ax, O, d1, d2, r, yazi, renk):
    m = np.radians((d1 + d2) / 2)
    ax.text(O[0] + r * np.cos(m), O[1] + r * np.sin(m), yazi, color=renk, fontsize=12, ha="center", va="center")

fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.5, 3.0), gridspec_kw={"width_ratios": [1, 1.5]})
for ax in (a1, a2): ax.set_aspect("equal"); ax.axis("off")

O = np.array([0.0, 0.0])
A = isin(a1, O, 0); C = isin(a1, O, 35); B = isin(a1, O, 90)
nokta(a1, *O, "O", dx=-0.3, dy=-0.3)
a1.text(*(A + [-0.05, -0.35]), "A"); a1.text(*(C + [0.08, 0.0]), "C"); a1.text(*(B + [-0.35, -0.1]), "B")
aci(a1, O, A, C, r=0.6, renk=MAVI); etiket(a1, O, 0, 35, 1.05, "35°", MAVI)
aci(a1, O, C, B, r=0.8, renk=KIRMIZI); etiket(a1, O, 35, 90, 1.25, "55°", KIRMIZI)
a1.set_xlim(-0.5, 2.4); a1.set_ylim(-0.5, 2.3)
a1.set_title("Komşu tümler: 90°", fontsize=12, color=YAZI)

A = isin(a2, O, 0); C = isin(a2, O, 35); B = isin(a2, O, 180)
nokta(a2, *O, "O", dx=-0.1, dy=-0.4)
a2.text(*(A + [-0.05, -0.35]), "A"); a2.text(*(C + [0.08, 0.0]), "C"); a2.text(*(B + [0.0, -0.35]), "B")
aci(a2, O, A, C, r=0.6, renk=MAVI); etiket(a2, O, 0, 35, 1.05, "35°", MAVI)
aci(a2, O, C, B, r=0.5, renk=KIRMIZI); etiket(a2, O, 35, 180, 0.9, "145°", KIRMIZI)
a2.set_xlim(-2.3, 2.4); a2.set_ylim(-0.5, 1.6)
a2.set_title("Komşu bütünler: 180°", fontsize=12, color=YAZI)

fig.tight_layout()
kaydet(fig, __file__)
