import sys; sys.path.insert(0, "tools")
from cizim import *

# m(A)=64, m(B)=56, m(C)=60. [BE iç açıortay, [CD dış açıortay: m(BDC) = 64/2 = 32.
B = np.array([0.0, 0.0]); C = np.array([4.6, 0.0])
t = 4.6 * np.sin(np.radians(60)) / np.sin(np.radians(64))
A = B + t * np.array([np.cos(np.radians(56)), np.sin(np.radians(56))])
a, b, c = np.linalg.norm(B - C), np.linalg.norm(A - C), np.linalg.norm(A - B)
D = (a * A - b * B + c * C) / (a - b + c)          # B'nin karşısındaki dış teğet çemberin merkezi
E = A + (C - A) * c / (a + c)                       # [BE ile [AC]'nin kesişimi (AE/EC = AB/BC)
P = np.array([D[0] + 1.2, 0.0])
def derece(p, k, q):
    v, w = p - k, q - k
    return np.degrees(np.arccos(np.dot(v, w) / np.linalg.norm(v) / np.linalg.norm(w)))
print("BDC", derece(B, D, C), "ACD", derece(A, C, D), "DCP", derece(D, C, P), "ABE", derece(A, B, E), "EBC", derece(E, B, C))
print("E BD üzerinde mi", (D - B)[0] * (E - B)[1] - (D - B)[1] * (E - B)[0])

def isaret(kose, p, q, rr, renk, n):
    aci(ax, kose, p, q, r=rr, renk=renk)
    a1 = np.arctan2(*(p - kose)[::-1]); a2 = np.arctan2(*(q - kose)[::-1])
    if (a2 - a1) % (2 * np.pi) > np.pi: a1, a2 = a2, a1
    o = a1 + ((a2 - a1) % (2 * np.pi)) / 2
    for k in range(n):
        oo = o + (k - (n - 1) / 2) * 0.08
        u = np.array([np.cos(oo), np.sin(oo)])
        ax.plot(*zip(kose + (rr - 0.12) * u, kose + (rr + 0.12) * u), color=renk, lw=1.6)

fig, ax = sekil(6, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(C, P), color=YAZI, lw=1.6, ls="--")
ax.plot(*zip(B, D), color=MAVI, lw=2); ax.plot(*zip(C, D), color=KIRMIZI, lw=2)
nokta(ax, *A, "A", dx=-0.15, dy=0.2); nokta(ax, *B, "B", dx=-0.45, dy=-0.3); nokta(ax, *C, "C", dx=-0.1, dy=-0.5)
nokta(ax, *P, "P", dx=-0.1, dy=-0.5); nokta(ax, *E, "E", dx=-0.45, dy=0.05, renk=MAVI)
nokta(ax, *D, "D", dx=0.15, dy=0.12, renk=KIRMIZI)
isaret(B, C, E, 1.3, SARI, 1); isaret(B, E, A, 1.3, SARI, 1)
isaret(C, A, D, 0.55, KIRMIZI, 2); isaret(C, D, P, 0.55, KIRMIZI, 2)
aci(ax, A, B, C, r=0.5, renk=YAZI)
ax.text(A[0] + 0.05, A[1] - 0.9, "64°", color=YAZI, fontsize=11, ha="center")
aci(ax, D, B, C, r=0.8, renk=MAVI)
ax.text(D[0] - 1.15, D[1] - 1.2, "32°", color=MAVI, fontsize=12, ha="center")
ax.set_xlim(-0.7, P[0] + 0.4); ax.set_ylim(-0.7, max(A[1], D[1]) + 0.6)
kaydet(fig, __file__)
