import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders, kural 1: m(A)=75, m(B)=45, m(C)=60. Karşı kenarlar sinüsle orantılı: a > c > b.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
B = np.array([0.0, 0.0]); C = np.array([6.0, 0.0])
b_ = 6.0 * np.sin(np.radians(45)) / np.sin(np.radians(75))   # |AC|
A = C + b_ * yon(180 - 60)
for ad, P, Q, R in (("A", A, B, C), ("B", B, A, C), ("C", C, A, B)):
    u, v = Q - P, R - P
    print(ad, round(np.degrees(np.arccos(u @ v / np.linalg.norm(u) / np.linalg.norm(v))), 3))
print("a b c", np.linalg.norm(C - B), np.linalg.norm(C - A), np.linalg.norm(B - A))

fig, ax = sekil(5.6, 4.2)
ax.set_aspect("equal"); ax.axis("off")
G = (A + B + C) / 3
def kenar(P, Q, renk, ad, ofs=0.38):
    ax.plot(*zip(P, Q), color=renk, lw=3.2, solid_capstyle="round")
    m = (P + Q) / 2; n = m - G; n = n / np.linalg.norm(n)
    ax.text(*(m + ofs * n), ad, color=renk, ha="center", va="center", fontsize=14, fontweight="bold")
kenar(B, C, KIRMIZI, "a  (en uzun)", 0.45)
kenar(A, B, SARI, "c", 0.35)
kenar(A, C, YESIL, "b  (en kısa)", 0.0)
# b etiketini kenarın dışına, sağa yaz
m = (A + C) / 2
ax.texts[-1].remove()
ax.text(m[0] + 0.35, m[1] + 0.15, "b  (en kısa)", color=YESIL, ha="left", va="center", fontsize=14, fontweight="bold")
nokta(ax, *A, "A", dx=-0.12, dy=0.22); nokta(ax, *B, "B", dx=-0.42, dy=-0.15); nokta(ax, *C, "C", dx=0.15, dy=-0.15)
aci(ax, A, B, C, r=0.55, ad="75°", renk=KIRMIZI)
aci(ax, B, A, C, r=0.9, ad="45°", renk=YESIL)
aci(ax, C, A, B, r=0.7, ad="60°", renk=SARI)
ax.set_xlim(-0.8, 8.4); ax.set_ylim(-0.9, A[1] + 0.6)
kaydet(fig, __file__)
