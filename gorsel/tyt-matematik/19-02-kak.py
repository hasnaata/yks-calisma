import sys; sys.path.insert(0, "tools")
from cizim import *

# K.A.K.: |AB|=6, |AC|=9, |DE|=4, |DF|=6, m(A)=m(D). |BC|=7,5 olacak biçimde A açısı seçildi; |EF|=5 çıkar.
cosA = (6**2 + 9**2 - 7.5**2) / (2 * 6 * 9); tA = np.degrees(np.arccos(cosA))
def ucgen(K, b, c, don=25.0):
    """K: A köşesi; AB yönü aşağı-sol, AC yönü aşağı-sağ, arada tA açısı."""
    a1 = -90 - tA / 2 - 10 + don * 0; a2 = a1 + tA
    return K, K + c * np.array([np.cos(np.radians(a1)), np.sin(np.radians(a1))]), K + b * np.array([np.cos(np.radians(a2)), np.sin(np.radians(a2))])
def kenar(ax, P, Q, metin, G, d=0.5, renk=YAZI):
    M = (P + Q) / 2; n = M - G; n = n / np.linalg.norm(n)
    ax.text(*(M + d * n), metin, ha="center", va="center", color=renk, fontsize=13)
A, B, C = ucgen(np.array([0.0, 0.0]), 9, 6)
D, E, F = ucgen(np.array([10.5, -2.5]), 6, 4)
print("A", tA, "BC", np.linalg.norm(B - C), "EF", np.linalg.norm(E - F))
fig, ax = sekil(6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
for P, Q, R in ((A, B, C), (D, E, F)):
    ax.plot(*zip(P, Q, R, P), color=YAZI)
aci(ax, A, B, C, r=0.7, ad="α", renk=MAVI); aci(ax, D, E, F, r=0.6, ad="α", renk=MAVI)
G1, G2 = (A + B + C) / 3, (D + E + F) / 3
nokta(ax, *A, "A", dx=-0.2, dy=0.3); nokta(ax, *B, "B", dx=-0.75, dy=-0.25); nokta(ax, *C, "C", dx=0.25, dy=-0.25)
nokta(ax, *D, "D", dx=-0.2, dy=0.3); nokta(ax, *E, "E", dx=-0.75, dy=-0.25); nokta(ax, *F, "F", dx=0.25, dy=-0.25)
kenar(ax, A, B, "6", G1, renk=KIRMIZI); kenar(ax, A, C, "9", G1, renk=KIRMIZI); kenar(ax, B, C, "7,5", G1)
kenar(ax, D, E, "4", G2, renk=KIRMIZI); kenar(ax, D, F, "6", G2, renk=KIRMIZI); kenar(ax, E, F, "?", G2)
xs = [p[0] for p in (A, B, C, D, E, F)]; ys = [p[1] for p in (A, B, C, D, E, F)]
ax.set_xlim(min(xs) - 1.0, max(xs) + 1.0); ax.set_ylim(min(ys) - 1.0, max(ys) + 0.9)
kaydet(fig, __file__)
