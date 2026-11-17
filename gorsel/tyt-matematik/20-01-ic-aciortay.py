import sys; sys.path.insert(0, "tools")
from cizim import *

# m(A)=70, m(B)=60, m(C)=50. İç açıortaylar D'de kesişir: m(BDC) = 90 + 70/2 = 125.
B = np.array([0.0, 0.0]); C = np.array([7.0, 0.0])
t = 7 * np.sin(np.radians(50)) / np.sin(np.radians(70))
A = B + t * np.array([np.cos(np.radians(60)), np.sin(np.radians(60))])
a, b, c = np.linalg.norm(B - C), np.linalg.norm(A - C), np.linalg.norm(A - B)
D = (a * A + b * B + c * C) / (a + b + c)
r = D[1]                                   # D'nin [BC]'ye uzaklığı = iç teğet çemberin yarıçapı
S = B + (C - B) * c / (b + c)              # A'dan çıkan açıortayın [BC]'yi kestiği nokta
def derece(p, k, q):
    v, w = p - k, q - k
    return np.degrees(np.arccos(np.dot(v, w) / np.linalg.norm(v) / np.linalg.norm(w)))
print("BDC", derece(B, D, C), "BAD", derece(B, A, D), "DAC", derece(D, A, C))

def isaret(kose, p, q, rr, renk, n):
    aci(ax, kose, p, q, r=rr, renk=renk)
    a1 = np.arctan2(*(p - kose)[::-1]); a2 = np.arctan2(*(q - kose)[::-1])
    o = (a1 + a2) / 2
    for k in range(n):
        oo = o + (k - (n - 1) / 2) * 0.07
        u = np.array([np.cos(oo), np.sin(oo)])
        ax.plot(*zip(kose + (rr - 0.12) * u, kose + (rr + 0.12) * u), color=renk, lw=1.6)

fig, ax = sekil(6, 4.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Circle(D, r, fill=False, edgecolor=SOLUK, lw=1.3, ls="--"))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, D), color=MAVI, lw=2); ax.plot(*zip(C, D), color=MAVI, lw=2)
ax.plot(*zip(A, S), color=YESIL, lw=1.8, ls="--")
nokta(ax, *A, "A", dx=-0.15, dy=0.22); nokta(ax, *B, "B", dx=-0.45, dy=-0.3); nokta(ax, *C, "C", dx=0.15, dy=-0.3)
nokta(ax, *D, "D", dx=0.18, dy=0.12, renk=MAVI)
isaret(B, C, D, 1.0, SARI, 1); isaret(B, D, A, 1.0, SARI, 1)
isaret(C, A, D, 1.3, KIRMIZI, 2); isaret(C, D, B, 1.3, KIRMIZI, 2)
aci(ax, A, B, C, r=0.6, renk=YAZI)
ax.text(A[0] + 0.12, A[1] - 1.05, "70°", color=YAZI, fontsize=11, ha="left")
aci(ax, D, C, B, r=0.4, renk=MAVI)
ax.text(D[0] + 0.15, D[1] - 0.8, "125°", color=MAVI, fontsize=12, ha="left")
ax.set_xlim(-0.8, 7.7); ax.set_ylim(-0.7, A[1] + 0.6)
kaydet(fig, __file__)
