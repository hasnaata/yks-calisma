import sys; sys.path.insert(0, "tools")
from cizim import *

# m(A)=50, m(B)=70, m(C)=60. B ve C'deki dış açıortaylar D'de kesişir: m(BDC) = 90 - 50/2 = 65.
B = np.array([0.0, 0.0]); C = np.array([5.0, 0.0])
t = 5 * np.sin(np.radians(60)) / np.sin(np.radians(50))
A = B + t * np.array([np.cos(np.radians(70)), np.sin(np.radians(70))])
a, b, c = np.linalg.norm(B - C), np.linalg.norm(A - C), np.linalg.norm(A - B)
D = (-a * A + b * B + c * C) / (-a + b + c)          # A'nın karşısındaki dış teğet çemberin merkezi
def derece(p, k, q):
    v, w = p - k, q - k
    return np.degrees(np.arccos(np.dot(v, w) / np.linalg.norm(v) / np.linalg.norm(w)))
Bx = B + 1.9 * (B - A) / c; Cx = C + 1.9 * (C - A) / b     # kenar uzantıları
print("BDC", derece(B, D, C), "dış B yarısı", derece(Bx, B, D), derece(D, B, C), "dış C yarısı", derece(Cx, C, D), derece(D, C, B))

def isaret(kose, p, q, rr, renk, n):
    aci(ax, kose, p, q, r=rr, renk=renk)
    a1 = np.arctan2(*(p - kose)[::-1]); a2 = np.arctan2(*(q - kose)[::-1])
    if (a2 - a1) % (2 * np.pi) > np.pi: a1, a2 = a2, a1
    o = a1 + ((a2 - a1) % (2 * np.pi)) / 2
    for k in range(n):
        oo = o + (k - (n - 1) / 2) * 0.08
        u = np.array([np.cos(oo), np.sin(oo)])
        ax.plot(*zip(kose + (rr - 0.12) * u, kose + (rr + 0.12) * u), color=renk, lw=1.6)

fig, ax = sekil(5.6, 5.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, Bx), color=YAZI, lw=1.6, ls="--"); ax.plot(*zip(C, Cx), color=YAZI, lw=1.6, ls="--")
ax.plot(*zip(B, D), color=MAVI, lw=2); ax.plot(*zip(C, D), color=MAVI, lw=2)
ax.plot(*zip(A, D), color=YESIL, lw=1.6, ls=":")
nokta(ax, *A, "A", dx=-0.12, dy=0.22); nokta(ax, *B, "B", dx=-0.5, dy=0.05); nokta(ax, *C, "C", dx=0.2, dy=0.05)
nokta(ax, *D, "D", dx=0.2, dy=-0.25, renk=MAVI)
isaret(B, Bx, D, 0.8, SARI, 1); isaret(B, D, C, 0.8, SARI, 1)
isaret(C, B, D, 0.8, KIRMIZI, 2); isaret(C, D, Cx, 0.8, KIRMIZI, 2)
aci(ax, A, B, C, r=0.6, renk=YAZI)
ax.text(A[0] - 0.05, A[1] - 1.05, "50°", color=YAZI, fontsize=11, ha="right")
aci(ax, D, B, C, r=0.6, renk=MAVI)
ax.text(D[0] - 0.45, D[1] + 0.25, "65°", color=MAVI, fontsize=12, ha="right")
ax.set_xlim(min(Bx[0], D[0]) - 0.8, max(Cx[0], C[0]) + 0.8); ax.set_ylim(D[1] - 0.6, A[1] + 0.6)
kaydet(fig, __file__)
